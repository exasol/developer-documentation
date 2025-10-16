=========================
Sales Forecasting
=========================

.. toctree::
   :maxdepth: 2

   setup.rst
  

Overview
========

In this section, we will perform sales forecasting using Exasol's AI architecture. This means predicting sales on future dates based on the learning from our sales data. You can use your own dataset for this demo, or we have conveniently provided a dataset for you.

This demo will cover all the necessary concepts that are part of Exasol’s AI architecture. Please note that while this demo doesn't showcase best practices for forecasting, it highlights how Exasol and its AI architecture can be used for forecasting within the database.

Prerequisites
-------------

* Familiarity with Python.
* Familiarity with the pandas DataFrame API.
* Familiarity with Exasol.
* Familiarity with SQL.

What You'll Need
----------------

You’ll need to:

* Set up `AI-Lab <https://github.com/exasol/ai-lab>`_ (We recommend the Docker version because it comes with the Docker database. Alternatively, you can use onPrem DB).
* This version of the demo is not compatible with SaaS database.
* Download and import the notebooks zip file from :ref:`setup-sf`.

What You'll Learn
-----------------

In this demo, you will learn how to:

* **Build a forecasting model**: Train a sales forecasting model using XGBoost in JupyterLab.
* **Integrate with Exasol**: Connect JupyterLab to Exasol and use it as both a data source and deployment target.
* **Deploy ML models inside the database**: Upload a trained model into :ref:`bucket-fs`.
* **Run predictions (UDFs) with SQL queries**: Execute forecasts directly within Exasol using standard SQL, without moving data outside the database using :ref:`overview-label`.
* **Leverage Exasol’s AI architecture**: Understand how Exasol enables in-database machine learning workflows for speed, scalability, and simplicity.

What You'll Build
-----------------

In this demo, you will build a complete in-database machine learning workflow for sales forecasting:

* A **sales forecasting model** trained with XGBoost in JupyterLab.
* A deployment pipeline to **upload the trained model** into :ref:`bucket-fs`.
* A :ref:`overview-label` inside Exasol that encapsulates the model logic.
* A way to run predictions directly in the database using SQL queries.
* An end-to-end example of Exasol’s AI architecture in action — from model saving to in-database predictions.
