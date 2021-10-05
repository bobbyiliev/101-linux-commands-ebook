# The `userdel` command

The `userdel` command is used to delete a user account and related files

### Examples:

To delete a user with the `userdel` command the syntax would be the following:

```
userdel userName
```

To force the removal of a user account even if the user is still logged in, using the `userdel` command the syntax would be the following:

```
userdel -f userName
```

To delete a user along with the files in the user’s home directory using the `userdel` command the syntax would be the following:

```
userdel -r userName
```

### Syntax:

```
userdel [OPTIONS] userName
```

### Possible options:

|**Flag**   |**Description**   |
|:---|:---|
|`-f`|Force the removal of the specified user account even if the user is logged in|
|`-r`|Remove the files in the user’s home directory along with the home directory itself and the user’s mail spool|
|`-Z`|Remove any SELinux(Security-Enhanced Linux) user mapping for the user’s login.|


