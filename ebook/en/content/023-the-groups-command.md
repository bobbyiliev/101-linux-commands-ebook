# The `groups` command

In linux, there can be multiple users(those who use/operate the system), and groups are nothing but the collection of users. Groups make it easy to manage users with the same security and access privileges. A user can be part of different groups.

Important Points:

Groups command prints the names of the primary and any supplementary groups for each given username, or the current process if no names are given.
If more than one name is given, the name of each user is printed before the list of that user’s groups and the username is separated from the group list by a colon.

### Syntax:

```
groups [username]
```

#### Example 1

Provided with a user name

```
groups demon
```

In this example, username demon is passed with groups command and the output shows the groups in which the user demon is present, separated by a colon.

#### Example 2

No username is passed then this will display group membership for the current user:

```
groups
```

Here the current user is demon . So when we give “groups” command only we get groups in which demon is a user.

#### Example 3

Passing root with groups command:

```
$demon# groups
```

> Note: Primary and supplementary groups for a process are normally inherited from its parent and are usually unchanged since login. This means that if you change the group database after logging in, groups will not reflect your changes within your existing login session. The only options are –help and –version.
