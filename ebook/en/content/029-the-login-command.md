# The `login` Command

The `login` command initiates a user session.

## Syntax

```bash
$ login [-p] [-h host] [-H] [-f username|username]
```

## Flags and their functionalities

|**Short Flag**    |**Description**   |
|--|--|
| `-f` |Used to skip a login authentication. This option is usually used by the getty(8) autologin feature.  |
| `-h` | Used by other servers (such as telnetd(8) to pass the name of the remote host to login so that it can be placed in utmp and wtmp. Only the superuser is allowed use this option.  |
|`-p`|Used by getty(8) to tell login to preserve the environment. |
|`-H`|Used by other servers (for example, telnetd(8)) to tell login that printing the hostname should be suppressed in the login: prompt.  |
|`--help`|Display help text and exit.|
|-V|Display version information and exit.|

## Examples

To log in to the system as user abhishek, enter the following at the login prompt:
```bash
$ login: abhishek
```
If a password is defined, the password prompt appears. Enter your password at this prompt.
