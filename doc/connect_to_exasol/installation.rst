.. _installation-pyexasol:

Installation
================

PyExasol is distributed through `PyPI <https://pypi.org/project/pyexasol/>`_ . It can be installed via pip, poetry, or any other type of dependency management tool:

.. code-block:: bash

   pip install pyexasol


Optional Dependencies
------------------------

PyExasol can also be installed with sets of optional dependencies to enable certain functionality.

.. code-block:: bash

   pip install pyexasol[optional-package-name]

- ``orjson`` is required for ``json_lib=orjson`` to improve JSON parsing performance.
- ``pandas`` is required for importing_and_exporting_data functions working with :class:`pandas.DataFrame`.
- ``polars`` is required for importing_and_exporting_data functions working with :class:`polars.DataFrame`.
- ``pyarrow`` is required for importing_and_exporting_data functions working with :class:`pyarrow.parquet`.
- ``pproxy`` is used in the examples to test an HTTP proxy.
- ``rapidjson`` is required for ``json_lib=rapidjson`` to improve JSON parsing performance.
- ``ujson`` is required for ``json_lib=ujson`` to improve JSON parsing performance.
