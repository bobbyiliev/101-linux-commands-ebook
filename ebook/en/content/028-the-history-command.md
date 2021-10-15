# The `history` command

If you type `history` you will get a list of the last 500 commands used. This gives you the possibility to copy and paste commands that you executed in the past.

This is powerful in combination with grep. So you can search for a command in your command history.

### Examples:

1. If you want to search in your history for artisan commands you ran in the past.

```
history | grep artisan
```

2. If you only want to show the last 10 commands you can.

```
history 10
```