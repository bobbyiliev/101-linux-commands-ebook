# The `yum` command

The `yum`command is the primary package management tool for installing, updating, removing, and managing software packages in Red Hat Enterprise Linux. It is an acronym for _`Yellow Dog Updater, Modified`_.

`yum` performs dependency resolution when installing, updating, and removing software packages. It can manage packages from installed repositories in the system or from .rpm packages.

### Syntax:

```[linux]
yum -option command
```

### Examples:

1. To see an overview of what happened in past transactions:

```[linux]
yum history
```

2. To undo a previous transaction:

```[linux]
yum history undo <id>
```

3. To install firefox package with 'yes' as a response to all confirmations

```[linux]
yum -y install firefox
```

4. To update the mysql package it to the latest stable version

```[linux]
yum update mysql
```

### Commonly used commands along with yum:

| **Command**    | **Description**                                   |
| :------------- | :------------------------------------------------ |
| `install`      | Installs the specified packages                   |
| `remove`       | Removes the specified packages                    |
| `search`       | Searches package metadata for keywords            |
| `info`         | Lists the description                             |
| `update`       | Updates each package to the latest version        |
| `repolist`     | Lists repositories                                |
| `history`      | Displays what has happened in past transactions   |
| `groupinstall` | To install a particular package group             |
| `clean`        | To clean all cached files from enabled repository |

### Additional Flags and their Functionalities:

| **Short Flag**    | **Long Flag**   | **Description**                                                                                                                                                      |
| :---------------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-C`              | `--cacheonly`   | Runs entirely from system cache, doesn’t update the cache and use it even in case it is expired.                                                                     |
| <center>-<center> | `--security`    | Includes packages that provide a fix for a security issue. Applicable for the upgrade command.                                                                       |
| `-y`              | `--assumeyes`   | Automatically answer yes for all questions.                                                                                                                          |
| <center>-<center> | `--skip-broken` | Resolves depsolve problems by removing packages that are causing problems from the transaction. It is an alias for the strict configuration option with value False. |
| `-v`              | `--verbose`     | Verbose operation, show debug messages.                                                                                                                              |
