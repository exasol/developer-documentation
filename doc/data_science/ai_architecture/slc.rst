SLC (Script Language Containers)
===========================================

A script language container consists of a Linux container with a complete Linux distribution and all required libraries and a script client. The script client is responsible for the communication with the database and for executing the UDF code.

SLCs are the containers for libraries that you use to execute UDFs. Some libraries are included in the default SLC, such as pandas and scikit-learn. If you want to leverage additional libraries, you can create a custom SLC and add them - this process can be accomplished using the SLC notebook in :doc:`AI Lab<../ai_lab>` or following along with our documentation: `Adding New Packages to Existing Script Languages <https://docs.exasol.com/db/latest/database_concepts/udf_scripts/adding_new_packages_script_languages.htm>`_