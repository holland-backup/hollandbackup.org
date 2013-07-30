Holland Backup 1.0.10 Available
################################################

:slug: holland-1-0-10-available
:date: 2013-07-31 01:00
:tags: Communication,Release
:author: Holland Core Team

We are pleased to announce the release of Holland 1.0.10. This version
squashes a number of bugs and also offers up a few new features, which
include:

 **Purge On Demand** 

 Purge on demand is a new option that, if set, causes Holland to
 purge old backups in order to make space for a new backup as opposed
 to failing due to lack of space.

 **Additional Options For Compression Plugins**

 Custom options can now be specified for to the underlying compression
 command. This  was added to support explicit flags, such as 
 ``gzip --rsyncable`` or ``pigz --processes N``.

 **Routines and Events Now Default for mysqldump** 

 mysqldump will now use the --routines and --events options by default
 if the version of MySQL supports these features.

 **mysqldump: Now With More Failure**

 The mysqldump plugin will now fail by design if it detects that no
 databases are to be backed up. This often indicates a configuration
 issue (such as insufficient backup user privileges).

The new version is available as both a tarball and via the OpenSUSE 
repositories:

 * http://hollandbackup.org/releases/stable/1.0/holland-1.0.10.tar.gz
 * http://download.opensuse.org/repositories/home:/holland-backup/

