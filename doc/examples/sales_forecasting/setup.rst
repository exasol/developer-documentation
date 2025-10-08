Setup
======

You will use `AI-Lab <https://github.com/exasol/ai-lab>`_ and an Exasol database. You can choose the Docker DB that comes with AI-Lab or
use `Exasol SaaS <https://cloud.exasol.com>`_ and start with the free trial.

Once you have finished setting up with `AI-Lab <https://github.com/exasol/ai-lab>`_, we can proceed.

Beginner to `AI-Lab <https://github.com/exasol/ai-lab>`_
------------------------------------------------------------

If this is your first time using `AI-Lab <https://github.com/exasol/ai-lab>`_, follow these steps:

* Start with the `main_config` file.
* Go through all of the cells in the `main_config` file.
* You have multiple database options: Docker (recommended), SaaS, and On-Prem.
* The last cell creates a **schema** for you and ensures that you are connected to a database.

Download the Sales Forecasting Demo File
------------------------------------------

* :ref:`download` from the link below.
* **Extract** the contents of the .zip file using your file explorer.
* **Create** a folder inside the root folder of AI-Lab and name it "sales_forecasting".
* **Upload** the files inside extracted folder into the "sales_forecasting" folder. Using the import button on the top right. 
* **Alternatively** you just upload the .zip file to JupyterLabs and unzip it using :ref:`below`.
* **Congratulations!** You’re all set, and now **we shall meet in AI-Lab**.
* The notebooks are **numbered** so you can know which one to visit **first**.

.. _below:

Unzip Files in JupyterLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import zipfile as zf
    files = zf.ZipFile("sales_forecasting.zip", 'r')
    files.extractall('sales_forecasting')
    files.close()

.. _download:

Download the .zip file
^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <a href="downloadable/sales_forecasting.zip" download>Download</a>


