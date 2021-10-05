# The `crontab` command

`crontab` - maintain crontab files for individual users (Vixie Cron)


crontab  is  the program used to install, deinstall or list the tables used to drive the cron(8) daemon in Vixie Cron.  Each user can have their own crontab, and though these are files in /var/spool/cron/crontabs, they are not intended to be edited directly.
### Syntax:

```
crontab [ -u user ] file
crontab [ -u user ] [ -i ] { -e | -l | -r }
```

### Examples:

1. The -l option causes the current crontab to be displayed on standard output.

```
crontab -l
```

2.  The -r option causes the current crontab to be removed.

```
crontab -r
```

3. The -e option is used to edit the current crontab using the editor specified by the VISUAL or EDITOR environment variables.  After you exit from the editor,  the modified crontab will be installed automatically.  If neither of the environment variables is defined, then the default editor /usr/bin/editor is used.

```
crontab -e
```

### Help Command
Run below command to view the complete guide to `crontab` command.
```
man crontab
```