# The `crontab` command

`crontab` is used to maintain crontab files for individual users (Vixie Cron)


crontab is the program used to install, uninstall or list the tables used to drive the cron(8) daemon in Vixie Cron.  Each user can have their own crontab, and though these are files in `/var/spool/cron/crontabs`, they are not intended to be edited directly.

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

4. You can specify the user you want to edit the crontab for.  Every user has its own crontab.  Assume you have a `www-data` user, which is in fact the user Apache is default running as. If you want to edit the crontab for this user you can run the following command

```
crontab -u www-data -e 
``` 

### Help Command
Run below command to view the complete guide to `crontab` command.
```
man crontab
```