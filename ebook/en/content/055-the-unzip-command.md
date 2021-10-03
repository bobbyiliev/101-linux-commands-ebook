# The `unzip` command

The `unzip` command extracts all files from the specified ZIP archive to the current directory.

### Examples:

In order to extract the files the syntax would be the following:

```
unzip myZipFile.zip
```

To unzip a ZIP file to a different directory than the current one, don't forget to add the `-d` flag:

```
unzip myZipFile.zip -d /path/to/directory
```

To unzip a ZIP file and exclude specific file or files or directories from being extracted, don't forget to add the `-x` flag:

```
unzip myZipFile.zip -x file1.txt file2.txt
```

### Syntax:

```
unzip zipFileName [OPTION] [PARAMS]
```

### Possible options:

|**Flag**   |**Description**   |**Params**   |
|:---|:---|:---|
|`-d`|Unzip an archive to a different directory.|/path/to/directory|
|`-x`|Extract the archive but do not extract the specified files.|filename(s)|
|`-j`|Unzip without creating new folders, if the zipped archive contains a folder structure.|-|
|`-l`|Lists the contents of an archive file without extracting it.|-|
|`-n`|Do not overwrite existing files; supply an alternative filename instead.|-|
|`-o`|Overwrite files.|-|
|`-P`|Supplies a password to unzip a protected archive file.|password|
|`-q`|Unzips without writing status messages to the standard output.|-|
|`-t`|Tests whether an archive file is valid.|-|
|`-v`|Displays detailed (verbose) information about the archive without extracting it.|-|
