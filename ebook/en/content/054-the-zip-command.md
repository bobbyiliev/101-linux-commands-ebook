# The `zip` command

The `zip` command is used to compress files and reduce their size. 
It outputs an archive containing one or more compressed files or directories.

### Examples:

In order to compress a single file with the `zip` command the syntax would be the following:

```
zip myZipFile.zip filename.txt
```

This also works with multiple files as well:

```
zip multipleFiles.zip file1.txt file2.txt
```

If you are compressing a whole directory, don't forget to add the `-r` flag:

```
zip -r zipFolder.zip myFolder/
```

### Syntax:

```
zip [OPTION] zipFileName filesList
```

### Possible options:

|**Flag**   |**Description**   |
|:---|:---|
|`-d`|Removes the file from the zip archive.  After creating a zip file, you can remove a file from the archive using the `-d` option|
|`-u`|Updates the file in the zip archive. This option can be used to update the specified list of files or add new files to the existing zip file. Update an existing entry in the zip archive only if it has been modified more recently than the version already in the zip archive.|
|`-m`|Deletes the original files after zipping.|
|`-r`|To zip a directory recursively, it will recursively zip the files in a directory. This option helps to zip all the files present in the specified directory.|
|`-x`|Exclude the files in creating the zip|
|`-v`|Verbose mode or print diagnostic version info. Normally, when applied to real operations, this option enables the display of a progress indicator during compression and requests verbose diagnostic info about zip file structure oddities|
