# The `nohup` command

When a shell exits (maybe while logging out of an SSH session), the HUP ('hang up') signal is send to all of its child processes, causing them to terminate. If you require a long-running process to continue after exiting shell, you'll need the `nohup` command. Prefixing any command with `nohup` causes the command to become _immune_ to HUP signals. Additionally, STDIN is being ignored and all output gets redirected to local file `./nohup.out`.

### Examples:

1. Applying nohup to a long-running debian upgrade:

```
nohup apt-get -y upgrade
```

### Syntax:

```
nohup COMMAND [ARG]...
nohup OPTION
```
