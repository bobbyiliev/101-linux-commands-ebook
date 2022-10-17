# The `less` command

The less command is a Linux terminal pager which shows a file's content one screen at a time.
Useful when dealing with a large text file because it doesn't load the entire file but accesses it page by page, resulting in fast loading speeds.
## Syntax
```
less [options] file_path
```

## Options
Some popular option flags include:
```
-E	less automatically exits upon reaching the end of file.
-f	Forces less to open non-regular files (a directory or a device-special file).
-F	Exit less if the entire file can be displayed on the first screen.
-g	Highlights the string last found using search. By default, less highlights all strings matching the last search command.
-G	Removes all highlights from strings found using search.
```
For a complete list of options, refer to the less help file by running:
```
    less --help
```
## Few Examples:
1. Open a Text File
```
less /etc/updatedb.conf
```

2. Show Line Numbers
```
less -N /etc/init/mysql.conf
```

3. Open File with Pattern Search
```
less -pERROR /etc/init/mysql.conf
```
4. Remove Multiple Blank Lines
```
less welcome.txt
```

Here I showed you how to use the less command in Linux. Although there are other terminal pagers, such as most and more, but less could be a better choice as it is a powerful tool present in almost every system.

For more details: https://phoenixnap.com/kb/less-command-in-linux#:~:text=The%20less%20command%20is%20a,resulting%20in%20fast%20loading%20speeds.