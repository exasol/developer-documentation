UDF (User Defined Functions)
========================================


User Defined Functions are one of the most powerful features of Exasol. It offers endless opportunities for embedding customer and third-party computational modules and frameworks into the database. For instance, it is possible to compute a complex AI model based on PyTorch inside the database.
Given the parallel architecture of the database, the model will be simultaneously computed on each node with a different partition of the data.

documentation/muhammad-01
The UDFs are backed by :doc:`BucketFS <./bfs>` - an Exasol proprietary replicated file system. This is where the model is usually stored. The file system is called replicated because the copies of all its files are stored at every node of the database cluster.


Want to learn more about UDFs and it's usage and examples? Check out :ref:`overview-label`.

The UDFs are backed by :doc:`BucketFS <./bfs>` - an Exasol proprietary replicated file system. This is where the model is usually stored. The file system is called replicated because the copies of all its files are stored at every node of the database cluster.

