===========
Overview
===========

Exasol is compatible with a wide range of technologies.

PyExasol is the officially supported Python connector for Exasol. It helps to handle massive volumes of data commonly associated with DBMS within python.

PyExasol provides an API to read & write multiple data streams in parallel using separate processes, which is necessary to fully utilize hardware and achieve linear scalability. With PyExasol you are no longer limited to a single CPU core.


PyExasol Main concepts
-----------------------

* Based on `WebSocket <https://github.com/exasol/websocket-api>`_ protocol.
* Optimized for minimum overhead.
* Easy integration with pandas, parquet, and polars via HTTP transport.
* Compression to reduce network bottleneck.

System Requirements
---------------------

* **Exasol >= 7.1**
* **Python >= 3.9**

PyExasol Versions
---------------------------

For the latest version and info about PyExasol versions, refer to the `version history <https://github.com/exasol/pyexasol/releases>`_



