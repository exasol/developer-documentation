Exasol's AI-Lab
================

Exasol has significant capabilities for implementing data science workflows - from classic machine learning to Gen AI and language model solutions.


What is AI-Lab?
-----------------

AI-Lab is a collection of interactive computational notebooks created by Exasol to showcase and demonstrate the capabilities of Exasol and its infrastructure in the context of Machine Learning and AI.

Reasons why you should try the Exasol's AI-Lab
------------------------------------------------

* Learn how Exasol uses it's infrastructure for AI and Machine Learning Algorithims.
* Learn how `User Defined Functions (UDFs) <https://docs.exasol.com/db/latest/database_concepts/udf_scripts.htm>`_ work in Exasol.
* Experience the MPP Architecture (how the exasol database allows running a predictive model on multiple nodes in parallel).
* Learn how to store models in `BucketFS <https://docs.exasol.com/db/latest/database_concepts/bucketfs/bucketfs.htm>`_. (Exasol proprietary replicated file system).

What AI-Lab can be used for?
--------------------------------

Here are some use cases for AI-Lab:

Train Models with Data from Exasol and do Inference inside the Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This means using Exasol as the source for training machine learning models externally (e.g., with scikit-learn, TensorFlow, or PyTorch) and then deploying those models inside the database. Inference is done through User Defined Functions (UDFs), enabling efficient predictions directly via SQL without moving data out of Exasol.

Use Transformers Extension and Text-AI to do Text Analytics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This means applying Exasol’s Transformers and Text-AI extensions to run advanced NLP tasks (e.g., sentiment analysis, classification, entity recognition) directly within the database. By leveraging pre-trained transformer models, text analytics can be integrated into SQL workflows without moving data out of Exasol.

Build Custom SLCs to Add New Python Packages to Exasol UDFs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This means creating a custom script language container in Exasol to include additional Python packages that are not available by default. It allows you to extend the functionality of User Defined Functions (UDFs) with the specific libraries needed for your machine learning or data processing tasks.

Use S3 Document Virtual Schema to Analyze Semi-Structured Data from S3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This means leveraging Exasol’s S3 Document Virtual Schema to directly query and analyze semi-structured data (like JSON or Parquet) stored in Amazon S3. It enables seamless access to S3 data through SQL without needing to load or transform it into the database first.


try it out here: `Exasol's AI-Lab <https://github.com/exasol/ai-lab>`_.



This video walks through `getting started with AI Lab <https://www.youtube.com/watch?v=LkqdLlRF2Go>`_.

AI Lab includes various workbooks that you can run to load data into Exasol. 
This video walks through `loading data <https://www.youtube.com/watch?v=-t1q6CeswJs&t=1s>`_ in more detail.

If you want to leverage Exasol to build Gen AI and LM-based solutions we recommend starting with the Exasol `Transformers Extension <https://github.com/exasol/transformers-extension>`_.

This video showcases the potential `applications of the Exasol Transformers Extension <https://www.youtube.com/watch?v=sHSnCR71kyc>`_ .