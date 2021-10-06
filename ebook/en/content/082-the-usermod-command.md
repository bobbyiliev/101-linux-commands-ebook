# The `usermod` command

The `usermod` command lets you to change the properties of a user in Linux through the command line. After creating a user we have to sometimes change their attributes like password or login directory etc. so in order to do that we use the `usermod` command.

### Syntax:

```
usermod [options] USER
```

#### Note : Only superuser (root) is allowed to execute `usermod` command 

### Options and their Functionalities:

|**Option**   |**Description**   |
|:---|:---|
|`-a`|to add anyone of the group to a secondary group|
|`-c`|to add comment field for the useraccount|
|`-d`|to modify the directory for any existing user account|
|`-g`|change the primary group for a User|
|`-G`|to add supplementary groups|
|`-l`|to change existing user login name|
|`-L`|to lock system user account|
|`-m`|to move the contents of the home directory from existing home dir to new dir|
|`-p`|to create an un-encrypted password|
|`-s`|to create a specified shell for new accounts|
|`-u`|to assigned UID for the user account|
|`-U`|to unlock any locked user|

### Examples:

1. To add a comment/description for a user:
```
sudo usermod -c "This is test user" test_user
```

2. To change the home directory of a user:
```
sudo usermod -d /home/sam test_user
```

3. To change the expiry date of a user: 
```
sudo usermod -e 2021-10-05 test_user
```

4. To change the group of a user: 
```
sudo usermod -g sam test_user
```

5. To change user login name:
``` 
sudo usermod -l test_account test_user
```

6. To lock a user:
```
sudo usermod -L test_user
```

7. To unlock a user:
```
sudo usermod -U test_user
```

8. To set an unencrypted password for the user:
```
sudo usermod -p test_password test_user
```

9. To create a shell for the user:
```
sudo usermod -s /bin/sh test_user
```

10. To change the user id of a user:
``` 
sudo usermod -u 1234 test_user
```
