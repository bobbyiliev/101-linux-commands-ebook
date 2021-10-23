# The `echo` command

The `echo` command lets you display the line of text/string that is passed as an argument

### Examples:

1. To Show the line of text or string passed as an argument:

```
echo Hello There
```
2. To show all files/folders similar to the `ls` command:
```
echo *
```
3. To save text to a file named foo.bar:
```
echo "Hello There" > foo.bar
```
4. To append text to a file named foo.bar:
```
echo "Hello There" >> foo.bar
```
### Syntax:

```
echo [option] [string]
```

#### It is usually used in shell scripts and batch files to output status text to the screen or a file.The `-e` used with it enables the interpretation of backslash escapes


### Additional Options and their Functionalities:


|**Option**   |**Description**   |
|:---|:---|
|`\b`|removes all the spaces in between the text|
|`\c`|suppress trailing new line with backspace interpretor ‘-e‘ to continue without emitting new line.|
|`\n`|creates new line from where it is used|
|`\t`|creates horizontal tab spaces|
|`\r`|carriage returns with backspace interpretor ‘-e‘ to have specified carriage return in output|
|`\v`|creates vertical tab spaces|
|`\a`|alert returns with a backspace interpretor ‘-e‘ to have sound alert|
|`-n`|omits echoing trailing newline .|
