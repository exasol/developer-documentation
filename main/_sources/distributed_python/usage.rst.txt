Creating and running UDFs
-------------------------

In the CREATE SCRIPT command, you must define the type of input and output values.
There are two types of UDF inputs (set and scalar) and two types of UDF outputs (returns and emits). 
These can be combined as needed to suite your use case.

- Input values

    - **SCALAR** Specifies that the script processes single input rows. The code is therefore called once per input row.

    - **SET** Specifies that the processing refers to a set of input rows. Within the code, you can iterate through those rows.

- Output values

    - **RETURNS** Specifies that the script returns a single value.

    - **EMITS** Specifies that the script can create (emit) multiple result rows (tuples).

Each UDF script must contain the main function run(). This function is called with a parameter providing access to the input data of Exasol. If your script processes multiple input tuples (using SET), you can iterate through the single tuples using this parameter.
You can specify an ORDER BY clause either when creating a script or when calling it. This clause sorts the processing of the groups of SET input data. If it is necessary for the algorithm, you should specify this clause when creating the script to avoid wrong results due to misuse.

Input parameters in scripts are always case sensitive, similar to the script code. This is different to SQL identifiers, which are only case sensitive if they are delimited.

You can use this `UDF Generator <https://htmlpreview.github.io/?https://github.com/EXASOL/script-languages/blob/master/udf-script-signature-generator/udf-script-signature-generator.html>`_ to help you get started building your own UDFs.

Examples
^^^^^^^^^

You can view examples of UDFs `here <https://docs.exasol.com/db/latest/database_concepts/udf_scripts/udf_examples.htm>`_.