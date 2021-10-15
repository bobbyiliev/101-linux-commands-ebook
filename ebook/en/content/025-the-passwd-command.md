
# The `passwd` command

In Linux, `passwd` command changes the password of user accounts. A normal user may only change the password for their own account, but a superuser may change the password for any account.
`passwd` also changes the account or associated password validity period.


## Example

```bash
$ passwd

```


## The syntax of the `passwd` command is :

```bash
$ passwd [options] [LOGIN]

```
## options

```bash
-a, --all
        This option can be used only with -S and causes show status for all users.

-d, --delete
        Delete a user's password.

-e, --expire
        Immediately expire an account's password.

-h, --help
        Display help message and exit.

-i, --inactive
        This option is used to disable an account after the password has been expired for a number of days.

-k, --keep-tokens
        Indicate password change should be performed only for expired authentication tokens (passwords).

-l, --lock
        Lock the password of the named account.

-q, --quiet
        Quiet mode.

-r, --repository
        change password in repository.

-S, --status
        Display account status information.                                                                        

```
