<h1 align="center">Developer Documentation</h1>

<p align="center">
Documentation and resources for data scientists and programmatic users to perform analytics with Exasol and to build applications on top.
</p>


# Getting Started
There are three ways to get started with Exasol:
- Download the [community edition](https://www.exasol.com/free-signup-community-edition/)
- Use the [docker version](https://github.com/exasol/docker-db)
- Signup for a free [SaaS trial](https://cloud.exasol.com/signup)

In the following we are going to use the SaaS version.

## Setting up the db
Our [main documentation](https://docs.exasol.com/saas/get_started/saas_first_steps.htm) shows you how to create a SaaS account and setup your first database and cluster.
## Installing pyexasol
Once your database is up and running you can connect via any client. From Python we use [PyExasol](https://github.com/exasol/pyexasol).
It can be easily installed via
```
pip install pyexasol[pandas]
```

## Connecting to the db
Connecting to an Exasol database is performed via:
```python
import pyexasol

C = pyexasol.connect(dsn='<host:port>', user='sys', password='exasol')
```
It is slightly different when connecting to a SaaS database as we need a [personal access token](https://docs.exasol.com/saas/administration/access_mngt/access_token.htm):
```python
import pyexasol

C = pyexasol.connect(dsn='<host:port>', user='sys', refresh_token='<token>')
```
Finally you can also wrap all credentials into a [local config file](https://exasol.github.io/pyexasol/master/user_guide/local_config.html):
```python
C = pyexasol.connect_local_config('my_exasol')
```
## Executing SQL
Running your first query is pretty straightforward:
```python
stmt = C.execute("SELECT * FROM EXA_ALL_USERS")

for row in stmt:
    print(row)
```
It also allows you to load resultsets into a pandas dataframe:
```python
C = pyexasol.connect(dsn='<host:port>', user='sys', password='exasol', compression=True)

df = C.export_to_pandas("SELECT * FROM EXA_ALL_USERS")
print(df.head())
```


# Data Ingestion
## CSV Files
## Parquet Files
## Import from external sources
## HTTP Transport
# Distributed Python (UDFs)
## Intro to UDFs
## Creating and running UDFs
## Debugging UDFs
# Advanced
##  move all the other stuff here
# Examples
# Environments
## Jupyter Notebooks
## VSCode
## Positron
# Integrations
## JupySQL
## Pandas
## Ibis
## SQLAlchemy
