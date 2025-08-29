BucketFS
===================

BucketFS is a synchronous file system that is available on all database nodes in an Exasol cluster. Each node in the cluster can connect to the BucketFS service and will see the same content as the other nodes.

A BucketFS service contains a number of buckets that can store a number of files. Each bucket can have different access privileges. Folders are not supported directly. Folders only exist as long as their is at least 1 file in that folder, but if you specify an upload path including folders, these will be created.

Each configured data disk in Exasol has a preinstalled BucketFS service with a default bucket. You can create additional BucketFS services as needed. `ConfD <https://docs.exasol.com/db/latest/confd/overview_bucketfs_jobs.htm>`_ jobs controls the management of BucketFS and the underlying buckets.



For machine learning - BucketFS is used to store trained models and serve those to UDFs when generating inferences
