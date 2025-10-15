.. _setup-sf:


Setup
======

You will be needing `AI-Lab <https://github.com/exasol/ai-lab>`_ and an Exasol database. You can use the Docker DB that comes with AI-Lab or an onPrem one.

Once you have finished setting up with `AI-Lab <https://github.com/exasol/ai-lab>`_, we can proceed.

Beginner to `AI-Lab <https://github.com/exasol/ai-lab>`_
------------------------------------------------------------

If this is your first time using `AI-Lab <https://github.com/exasol/ai-lab>`_, follow these steps:

* Start with the `main_config` notebook.
* Go through all of the cells in the `main_config` notebook.
* You have multiple database options: Docker DB(recommended) and On-Prem.
* The last cell creates a **schema** for you and ensures that you are connected to a database.
* We can now proceed with our demo.


Download the Sales Forecasting Demo File
------------------------------------------

* :download:`Download the .zip file<./sales_forecasting.zip>`.
* **Extract** the contents of the .zip file using your file explorer.
* **Create** a folder inside the root folder of AI-Lab and name it "sales_forecasting".
* **Upload** the files inside extracted folder into the "sales_forecasting" folder. Using the import button on the top right. 
* **Alternatively** you can just upload the .zip file to JupyterLabs and unzip it using the :ref:`below`.
* **Congratulations!** You’re all set, and now **we shall meet in AI-Lab**.
* Start from the `export_store_data` notebook and then move onto the `main`` notebook.

.. _below:

Code to Unzip Files in JupyterLab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import zipfile as zf

    # Open the zip file
    with zf.ZipFile("sales_forecasting.zip", 'r') as files:
    # Extract all contents directly to the current directory
    files.extractall()



