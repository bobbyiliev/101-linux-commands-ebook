
# The `finger` command

The `finger` displays information about the system users.

### Examples:

1. View detail about a particular user.

```
finger abc
```
*Output*
```
Login: abc                          Name: (null)
Directory: /home/abc                Shell: /bin/bash
On since Mon Nov  1 18:45 (IST) on :0 (messages off)
On since Mon Nov  1 18:46 (IST) on pts/0 from :0.0
New mail received Fri May  7 10:33 2013 (IST)
Unread since Sat Jun  7 12:59 2003 (IST)
No Plan.
```

2. View login details and Idle status about an user

```
finger -s root
```
*Output*
```
Login     Name       		Tty      Idle  Login Time   Office     Office Phone
root         root           *1    19d Wed 17:45
root         root           *2     3d Fri 16:53
root         root           *3        Mon 20:20
root         root           *ta    2  Tue 15:43
root         root           *tb    2  Tue 15:44
```
### Syntax:

```
finger [-l] [-m] [-p] [-s] [username]
```


### Additional Flags and their Functionalities:

|**Flag**   |**Description**   |
|:---|:---|
|`-l`|Force long output format.|
|`-m`|Match arguments only on user name (not first or last name).|
|`-p`|Suppress printing of the .plan file in a long format printout.|
|`-s`|Force short output format.|

### Additional Information
**Default Format**

The default format includes the following items:

Login name  
Full username  
Terminal name  
Write status (an * (asterisk) before the terminal name indicates that write permission is denied)  
For each user on the host, the default information list also includes, if known, the following items:

Idle time (Idle time is minutes if it is a single integer, hours and minutes if a : (colon) is present, or days and hours if a “d” is present.)  
Login time  
Site-specific information

**Longer Format**

A longer format is used by the finger command whenever a list of user’s names is given. (Account names as well as first and last names of users are accepted.) This format is multiline, and includes all the information described above along with the following:

User’s $HOME directory  
User’s login shell  
Contents of the .plan file in the user’s $HOME directory  
Contents of the .project file in the user’s $HOME directory
