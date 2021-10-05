# The `useradd` command

The `useradd` command is used to add or update user accounts to the system.

### Examples:

To add a new user with the `useradd` command the syntax would be the following:

```
useradd NewUser
```

To add a new user with the `useradd` command and give a home directory path for this new user the syntax would be the following:

```
useradd -d /home/NewUser NewUser
```

To add a new user with the `useradd` command and give it a specific id the syntax would be the following:

```
useradd -u 1234 NewUser
```

### Syntax:

```
useradd [OPTIONS] NameOfUser
```

### Possible options:

|**Flag**   |**Description**   |**Params**   |
|:---|:---|:---|
|`-d`|The new user will be created using /path/to/directory as the value for the user's login directory|/path/to/directory|
|`-u`|The numerical value of the user's ID|ID|
|`-g`|Create a user with specific group id|GroupID|
|`-M`|Create a user without home directory|-|
|`-e`|Create a user with expiry date|DATE (format: YYYY-MM-DD)|
|`-c`|Create a user with a comment|COMMENT|
|`-s`|Create a user with changed login shell|/path/to/shell|
|`-p`|Set an unencrypted password for the user|PASSWORD|

