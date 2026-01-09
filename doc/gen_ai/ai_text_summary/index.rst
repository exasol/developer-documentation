=================================
Self-Hosted AI Text Summarization
=================================

Overview
========

Learn how to invoke open source large language models (LLMs) directly from your Exasol database using UDFs and Ollama. This tutorial demonstrates a fully self-hosted AI pipeline where your data never leaves your infrastructure.

Why Self-Hosted?
----------------

Running open-source AI models in your own environment offers significant advantages:

**Cost Savings**
   * No per-token API fees
   * No usage-based pricing
   * One-time model download, unlimited use

**Data Privacy & Security**
   * Data never leaves your infrastructure
   * No third-party API calls
   * Full compliance control

**Open Source Freedom**
   * Apache 2.0 licensed models (Mistral 7B)
   * No vendor lock-in
   * Modify and fine-tune as needed

**Performance Control**
   * Predictable latency (~1-2 seconds per summary)
   * No rate limits
   * Scale on your own hardware

Architecture
============

.. code-block:: text

                     ┌─────────────────┐      HTTP Request     ┌─────────────────┐
                     │   Exasol DB     │ ────────────────────> │ Mistral model   │
   AI text   <─────  │  (Docker)       │      (Python UDF)     │   (Ollama)      │
   Summary     SQL   │                 │ <──────────────────── │                 │
                     └─────────────────┘       JSON Response   └─────────────────┘

Prerequisites
=============

**Required:**

* Docker (for Exasol database)
* Ollama installed locally
* Basic SQL and Python knowledge
* ~4GB disk space (for Mistral model)
* ~15 minutes

Step 1: Start Exasol Database
==============================
If you don't have an Exasol database running, set one up quickly using Docker. 
Exasol provides a free Docker image for development and testing which supports up to 10GB of data (plenty for this tutorial).
Full instructions for deploying the Exasol Docker image can be found in the `Exasol Docker repository <https://github.com/exasol/docker-db>`_.

Run Exasol in Docker:

.. code-block:: bash

   docker run -d \
     --name exasol \
     -p 8563:8563 \
     exasol/docker-db:latest

`Connect using your SQL client <https://docs.exasol.com/db/latest/connect_exasol/sql_clients/db_visualizer.htm>`_ using the default credentials for the Docker image. Unless you are using a prod instance or have modified the credentials, they are as follows:

* **Host**: ``localhost:8563`` (you will need to append the unique fingerprint for your instance - follow above documentation)
* **User**: ``sys``
* **Password**: ``exasol``

DBvisualizer is the preferred client for Exasol, but you can use any SQL client of your choice including DBeaver, SQL Workbench, Visual Stutio or any JDBC-compatible tool.

Step 2: Prepare Sample Data
============================

Create Schema and Table
------------------------

.. code-block:: sql

   -- Create a dedicated schema for the demo
   CREATE SCHEMA IF NOT EXISTS DEMO;

   -- Create the articles table
   CREATE OR REPLACE TABLE DEMO.ARTICLES (
       article VARCHAR(20000),      -- Full article text
       article_date VARCHAR(100),   -- Publication date
       heading VARCHAR(1000),       -- Article headline
       news_type VARCHAR(100)       -- Category (e.g., business, sports)
   );

Import CSV Data
---------------

:download:`Download articles_data.csv <./articles_data.csv>` and import it:

.. code-block:: sql

   IMPORT INTO DEMO.ARTICLES
   FROM LOCAL CSV FILE '/path/to/articles_data.csv'
   COLUMN SEPARATOR = ','
   SKIP = 1;  -- Skip header row

Verify the import:

.. code-block:: sql

   SELECT COUNT(*) as total_articles FROM DEMO.ARTICLES;

Step 3: Set Up Ollama
======================
`Ollama <https://ollama.com/>`_ is a local LLM management tool that makes it easy to download, run, and serve open-source models.

Install Ollama
--------------

.. code-block:: bash

   # macOS
   brew install ollama

   # Linux
   curl -fsSL https://ollama.com/install.sh | sh

   # Windows
   # Download installer from ollama.com

Download the Model
------------------

We chose **Mistral 7B** for the best balance of speed, quality, and open source licensing:

.. list-table:: Model Comparison
   :header-rows: 1
   :widths: 20 15 15 50

   * - Model
     - Speed
     - Quality
     - Notes
   * - qwen3:4b
     - ⚡⚡⚡ Fast (~1s)
     - Good
     - Includes verbose "thinking" output
   * - **mistral:latest**
     - ⚡⚡ Medium (~1-2s)
     - Excellent
     - **Clean output, recommended**
   * - gpt-oss:20b
     - ⚡ Slow (~5s+)
     - Best
     - Too slow for real-time use

Download Mistral:

.. code-block:: bash

   ollama pull mistral:latest

This downloads approximately 4GB. The model is **fully open source** under Apache 2.0 license.

Step 4: Test Ollama API
========================

Find Your Local IP Address
---------------------------

Since Exasol runs in Docker, it needs to access Ollama via your machine's local network IP (not ``localhost``):

.. code-block:: bash

   # macOS
   ipconfig getifaddr en0

   # Linux
   hostname -I | awk '{print $1}'

Example output: ``10.0.0.186``

Test the Endpoint
-----------------

.. code-block:: bash

   curl http://YOUR_IP:11434/api/generate -d '{
     "model": "mistral:latest",
     "prompt": "Summarize in one sentence: This is a test article about AI.",
     "stream": false
   }'

Expected response (truncated):

.. code-block:: json

   {
     "model": "mistral:latest",
     "created_at": "2024-01-07T19:23:24.548236Z",
     "response": "This article discusses AI technology.",
     "done": true,
     "total_duration": 1068666750
   }

If you see this JSON response, Ollama is working correctly!

.. note::
   Ollama is accessible on your local network by default. The UDF running in Docker 
   can reach it using your machine's IP address.

Step 5: Create UDFs
===================

We will create Python UDFs in Exasol that call the Ollama API to summarize articles.
Exasol's `User Defined Functions (UDF) <https://docs.exasol.com/db/latest/database_concepts/udf_scripts.htm>`_ framework allows us to run Python code directly within the database.
UDFs support various languages: Python, R, Lua and Java. UDFs also have default `access to a variety of packages <https://docs.exasol.com/db/latest/database_concepts/udf_scripts/python3.htm#Auxiliarylibraries>`_ including `requests`, which we will use to make HTTP calls to Ollama.
UDFs can be either simple scalar functions or more advanced SET functions that emit multiple columns.
We will write both a simple SET function and a more complex EMITS function to tackle different use cases.

Simple UDF: Summary Only
-------------------------

Returns just the summarized text. Best for:
* Ad-hoc queries
* Simple SELECT statements  

**Create the UDF:**

.. code-block:: text

   CREATE OR REPLACE PYTHON3 SCALAR SCRIPT DEMO.SUMMARIZE_ARTICLE(article_text VARCHAR(20000))
   RETURNS VARCHAR(2000) AS

   import requests
   import json

   def run(ctx):
       """
       Summarizes article text using a local Ollama model.
       
       Returns:
           str: One-sentence summary, or error message if processing fails
       """
       text = ctx.article_text
       
       # Handle NULL or empty input
       if text is None or text.strip() == '':
           return None
       
       try:
           # Prepare request to Ollama API
           payload = {
               'model': 'mistral:latest',
               'prompt': 'Summarize this news article in exactly one brief sentence: ' + text,
               'stream': False,
               'options': {
                   'temperature': 0.3,     # Lower = more focused
                   'num_predict': 50       # Limit to ~50 tokens
               }
           }
           
           # IMPORTANT: Replace 10.0.0.186 with YOUR machine's IP
           response = requests.post(
               'http://10.0.0.186:11434/api/generate',
               json=payload,
               timeout=15
           )
           response.raise_for_status()
           
           result = response.json()
           return result['response'].strip()
           
       except Exception as e:
           return 'ERROR: ' + str(e)
   /

.. important::
   Replace ``10.0.0.186`` with your actual machine's IP address from Step 4.

**Test the UDF:**

.. code-block:: sql

   SELECT 
       HEADING,
       DEMO.SUMMARIZE_ARTICLE(ARTICLE) as summary
   FROM DEMO.ARTICLES
   LIMIT 5;

.. note::
   The first time you call the UDF, Ollama may take a few extra seconds to load the model into memory.

Advanced UDF: Summary + Timing
-------------------------------

Returns both summary and execution duration. Best for:

* Performance monitoring
* Batch processing workflows
* Production deployments
* Analyzing model performance

**Create the UDF:**

.. code-block:: text

   CREATE OR REPLACE PYTHON3 SET SCRIPT DEMO.SUMMARIZE_ARTICLE_WITH_TIMING(article_text VARCHAR(20000))
   EMITS (summary VARCHAR(2000), duration_seconds DOUBLE) AS

   import requests
   import json

   def run(ctx):
       """
       Summarizes articles and tracks execution time.
       
       Emits:
           summary (str): One-sentence summary
           duration_seconds (float): Processing time from Ollama
       """
       while True:
           text = ctx.article_text
           
           # Handle NULL input
           if text is None:
               ctx.emit(None, None)
               if not ctx.next():
                   break
               continue
           
           try:
               payload = {
                   'model': 'mistral:latest',
                   'prompt': 'Summarize this news article in exactly one brief sentence: ' + text,
                   'stream': False,
                   'options': {
                       'temperature': 0.3,
                       'num_predict': 50
                   }
               }
               
               # IMPORTANT: Replace 10.0.0.186 with YOUR IP
               response = requests.post(
                   'http://10.0.0.186:11434/api/generate',
                   json=payload,
                   timeout=15
               )
               response.raise_for_status()
               result = response.json()
               
               # Extract timing (nanoseconds → seconds)
               duration = float(result.get('total_duration', 0)) / 1000000000.0
               summary = result['response'].strip()
               
               ctx.emit(summary, duration)
               
           except Exception as e:
               ctx.emit('ERROR: ' + str(e), 0.0)
           
           if not ctx.next():
               break
   /

.. warning::
   SET scripts with EMITS process the **entire input table**. You must explicitly 
   limit the data before calling the UDF using temp tables or WHERE clauses.

Results
=======

Sample output from our test run with 5 articles:

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Duration (s)
     - Summary
   * - 2.83
     - Saina Nehwal attributes her success in badminton to hard work and dedication.
   * - 2.07
     - Video shows Cristiano Ronaldo throwing reporter's microphone into lake.
   * - 2.34
     - Pakistan cricket team will offer full support to Mohammad Amir's return.
   * - 1.37
     - Barcelona do not plan to sell Neymar to Paris Saint Germain.
   * - 1.89
     - Portugal and Hungary advance to Euro 2016 after exciting 3-3 draw.

**Performance Metrics:**

* Average: ~2.1 seconds per article
* Range: 1.37s to 2.83s
* Consistent quality across different article types

Example Queries
===============

Simple Summarization
--------------------

.. code-block:: sql

   -- Summarize sports articles
   SELECT 
       HEADING,
       DEMO.SUMMARIZE_ARTICLE(ARTICLE) as summary
   FROM DEMO.ARTICLES
   WHERE news_type = 'sports'
   LIMIT 10;

Batch Processing with Timing
-----------------------------

.. code-block:: sql

   -- Process business news in controlled batch
   CREATE OR REPLACE TABLE DEMO.BUSINESS_SAMPLE AS
   SELECT * FROM DEMO.ARTICLES 
   WHERE news_type = 'business'
   LIMIT 20;

   SELECT 
       SUMMARIZE_ARTICLE_WITH_TIMING(ARTICLE)
   FROM DEMO.BUSINESS_SAMPLE;

Performance Analysis
--------------------

.. code-block:: sql

   -- Analyze relationship between article length and processing time
   CREATE OR REPLACE TABLE DEMO.PERF_ANALYSIS AS
   SELECT 
       LENGTH(ARTICLE) as article_length,
       ARTICLE
   FROM DEMO.ARTICLES
   LIMIT 50;

   SELECT 
       MIN(s.duration_seconds) as min_duration,
       AVG(s.duration_seconds) as avg_duration,
       MAX(s.duration_seconds) as max_duration,
       AVG(LENGTH(a.ARTICLE)) as avg_article_length
   FROM DEMO.PERF_ANALYSIS a,
        TABLE(DEMO.SUMMARIZE_ARTICLE_WITH_TIMING(a.ARTICLE)) s;

Production Considerations
=========================

Error Handling
--------------

For production use you can add enhanced error handling to your functions:

.. code-block:: python

   try:
       response = requests.post(...)
   except requests.exceptions.Timeout:
       return 'TIMEOUT: Request exceeded 15 seconds'
   except requests.exceptions.ConnectionError:
       return 'CONNECTION_ERROR: Cannot reach Ollama'
   except requests.exceptions.HTTPError as e:
       return f'HTTP_ERROR: {e.response.status_code}'
   except Exception as e:
       return f'UNKNOWN_ERROR: {str(e)}'

Caching Strategy
----------------

Cache summaries to avoid reprocessing:

.. code-block:: sql

   -- Create cache table
   CREATE TABLE DEMO.SUMMARY_CACHE (
       article_hash VARCHAR(64),
       summary VARCHAR(2000),
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       PRIMARY KEY (article_hash)
   );

   -- Check cache before calling UDF
   SELECT 
       CASE 
           WHEN c.summary IS NOT NULL THEN c.summary
           ELSE DEMO.SUMMARIZE_ARTICLE(a.ARTICLE)
       END as summary
   FROM DEMO.ARTICLES a
   LEFT JOIN DEMO.SUMMARY_CACHE c 
       ON HASH_SHA256(a.ARTICLE) = c.article_hash;

Monitoring
----------

Track UDF performance over time:

.. code-block:: sql

   -- Create metrics table
   CREATE TABLE DEMO.UDF_METRICS (
       execution_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       article_id VARCHAR(100),
       duration_seconds DOUBLE,
       success BOOLEAN
   );

   -- Log each execution (modify UDF to emit metrics)

Resource Management
-------------------

**Ollama Configuration:**

Limit Ollama's resource usage:

.. code-block:: bash

   # Limit to 4 CPU cores
   export OLLAMA_NUM_THREADS=4
   
   # Set max memory (in GB)
   export OLLAMA_MAX_LOADED_MODELS=1

**Batch Processing:**

Process large datasets in manageable chunks:

.. code-block:: sql

   -- Process 100 articles at a time
   CREATE OR REPLACE TABLE DEMO.BATCH_1 AS
   SELECT * FROM DEMO.ARTICLES WHERE ROWNUM BETWEEN 1 AND 100;
   
   SELECT SUMMARIZE_ARTICLE_WITH_TIMING(ARTICLE) FROM DEMO.BATCH_1;
   
   -- Wait, then process next batch
   CREATE OR REPLACE TABLE DEMO.BATCH_2 AS
   SELECT * FROM DEMO.ARTICLES WHERE ROWNUM BETWEEN 101 AND 200;

Security Considerations
-----------------------

**Network Security:**

* Use firewall rules to restrict Ollama port access
* Consider VPN for multi-machine setups
* Don't expose Ollama to public internet

**Data Privacy:**

* All processing happens locally—no data sent to external APIs
* Models are downloaded once and run offline
* Audit data access through Exasol's built-in logging

Next Steps
==========

Extend the Concept
------------------

This pattern works for many AI tasks:

**Text Classification**
   Categorize documents, detect sentiment, identify topics

**Entity Extraction**
   Pull out names, dates, locations from unstructured text

**Question Answering**
   Query your data in natural language

**SQL Generation**
   Use models like ``sqlcoder`` to generate queries from descriptions

**Data Quality**
   Detect anomalies, fix formatting, validate content

Try Different Models
--------------------

Explore Ollama's model library:

.. code-block:: bash

   # Specialized for SQL
   ollama pull sqlcoder

   # Code generation
   ollama pull codellama

   # Multilingual support
   ollama pull aya

   # Smaller, faster models
   ollama pull phi3

Optimize Performance
--------------------

**Fine-tune model parameters:**

.. code-block:: python

   'options': {
       'temperature': 0.1,      # More deterministic
       'top_p': 0.9,            # Nucleus sampling
       'top_k': 40,             # Limit vocabulary
       'repeat_penalty': 1.1,   # Reduce repetition
       'num_predict': 100       # Max output tokens
   }

**Use quantized models** for faster inference:

.. code-block:: bash

   # Q4 quantization (4-bit, very fast)
   ollama pull mistral:7b-q4

Scale Up
--------

**Multiple Models:**

You can run different models best suited different tasks:

.. code-block:: sql

   -- Summarization
   CREATE SCRIPT SUMMARIZE_WITH_MISTRAL(...)
   
   -- SQL generation  
   CREATE SCRIPT GENERATE_SQL_WITH_SQLCODER(...)
   
   -- Classification
   CREATE SCRIPT CLASSIFY_WITH_LLAMA(...)

It is also straightforward to modify the UDF to accept model name as a parameter, making it easier to reuse and switch models on the fly.

**Distributed Processing:**

For large-scale deployments, consider:

* Multiple Ollama instances with load balancing
* GPU acceleration for faster inference
* Dedicated inference servers

Resources
=========

**Documentation:**

* `Exasol UDF Documentation <https://docs.exasol.com/db/latest/database_concepts/udf_scripts.htm>`_
* `Ollama GitHub <https://github.com/ollama/ollama>`_
* `Ollama API Reference <https://github.com/ollama/ollama/blob/main/docs/api.md>`_
* `Mistral AI Documentation <https://docs.mistral.ai/>`_

**Community:**

* `Exasol Community <https://community.exasol.com/>`_
* `Ollama Discord <https://discord.gg/ollama>`_

Feedback
========

* Contact us on the `Exasol Community <https://community.exasol.com/>`_

---

*Last updated: January 2026*