# The `alias` command

The `alias` command lets you create shortcuts for long string to short ones.
It's usually used to replace long commands that you use frequently with short word.

### Examples:

1. To show the list of all defined aliases in the reusable form `alias NAME=VALUE` :

```
alias -p
```

2. To make `ls -A` shortcut:

```
alias la='ls -A'
```

### Syntax:

```
alias [-p] [name[=value]]
```

### Setting Persistent Options:

As most of linux custom settings for the terminal, any alias you defiend is only applied to the current opening terminal session.

For any alias to be active for all new sessions you need to add that command to your rc file to be executed in the startup of every new terminal.
this file can be as follows:
- **Bash**: ~/.bashrc
- **ZSH**: ~/.zshrc
- **Fish** – ~/.config/fish/config.fish

you can open that file with you favorite editor as follows:

```
vim ~/.bashrc
```
type your commands one per line, then save the file and exit.
the commands will be automatically applied in the next session.

If you want to apply it in the current session, run the following command:
```
source ~/.bashrc
```

### Opposite command:
To remove predefined alias you can use `unalias` command as follows:
```
unalias alias_name
```

to remove all aliases 
```
unalias -a
```
