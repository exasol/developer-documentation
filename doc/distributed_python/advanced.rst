Advanced
--------

From a performance perspective, which programming language you should use in an UDF script depends on the purpose and context of the script, as specific elements may have different capacities in each language. For example, string processing can be faster in one language while XML parsing can be faster in another. This means that one language cannot be said to have better performance in all circumstances. However, if overall performance is the most important criteria, we recommend using Lua. Lua is integrated in Exasol in the most native way, and therefore, it has the smallest process overhead.

During the processing of a SELECT statement, multiple virtual machines are started for each script and node. These virtual machines process the data independently. For scalar functions, the input rows are distributed across those virtual machines to achieve maximum parallelism. For SET input tuples, the virtual machines are used per group if you specify a GROUP BY clause. Otherwise, there will be only one group, which means only one node and virtual machine can process the data.

The following pages contain information about more advanced UDF functionality:

* `UDF Instance Limiting <https://docs.exasol.com/db/latest/database_concepts/udf_scripts/udf_instance_limit.htm>`_ 

* `Hiding Access tokens and secrets <https://docs.exasol.com/db/latest/database_concepts/udf_scripts/hide_access_keys_passwords.htm>`_ 

* `Managing Script Language Containers <https://docs.exasol.com/db/latest/database_concepts/udf_scripts/adding_new_packages_script_languages.htm>`_