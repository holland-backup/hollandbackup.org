About
#####

Holland is an Open Source backup framework originally developed at Rackspace
and written in Python. Its goal is to help facilitate backing up databases with
greater configurability, consistency, and ease. Holland is capable of backing
up other types of data, too. Because of its plugin structure, Holland can be
used to backup anything you want by whatever means you want.

Notable Features
----------------

* Pluggable Framework
* Supports Multiple Backup Sets
* Database and Table Filtering (Using GLOBs)
* Auto-Detection of Transactional DBs
* Safe use of –single-transaction with mysqldump
* In-Line and Pluggable Compression
* Backups Suitable for Point-In-Time Recovery / Replication
* MySQL + LVM Snapshot and Logical Backups
* PostgreSQL backups using pgdump
