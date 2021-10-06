# The `tar` command

The `tar` command  stands for tape archive, is used to create Archive and extract the Archive files. This command  provides archiving functionality in Linux. We can use tar command to create compressed or uncompressed Archive files and also maintain and modify them. 

### Examples:

1. To create a tar file in abel directory:

```
tar -cvf file-14-09-12.tar /home/abel/
```

2. Untars file in the current directory:

```
 tar -xvf file-14-09-12.tar
```

### Syntax:

```
tar [options] [archive-file] [file or directory to be archived
```


### Additional Flags and their Functionalities:

|**Use Flag**   |**Description**   |
|:---|:---|
|`-c`|Creates Archive |
|`-x`|Extract the archive |
|`-f`|Creates archive with given filename|
|`-t`|Displays or lists files in archived file |
|`-u`|Archives and adds to an existing archive file|
|`-v`|Displays Verbose Information |
|`-A`|Concatenates the archive files |
|`-z`|zip, tells tar command that creates tar file using gzip |
|`-j`|Filter archive tar file using tbzip |
|`w`|Verify a archive file |
|`r`|update or add file or directory in already existed .tar file |
|`-?`|Displays a short summary of the project |
|`-d`|Find the difference between an archive and file system |
|`--usage`|shows available tar options |
|`--version`|Displays the installed tar version |
|`--show-defaults`|Shows default enabled options |

|**Option Flag**   |**Description**   |
|:---|:---|
|`--check-device`| Check device numbers during incremental archive|
|`-g`|Used to allow compatibility with GNU-format incremental ackups|
|`--hole-detection`|Used to detect holes in the sparse files|
|`-G`| Used to allow compatibility with old GNU-format incremental backups|
|`--ignore-failed-read`|Don't exit the program on file read errors|
|`--level`|Set the dump level for created archives|
|`-n`|Assume the archive is seekable|
|`--no-check-device`|Do not check device numbers when creating archives|
|`--no-seek`|Assume the archive is not seekable|
|`--occurrence=N|`Process only the Nth occurrence of each file|
|`--restrict|`Disable use of potentially harmful options|
|`--sparse-version=MAJOR,MINOR`|Set version of the sparce format to use|
|`-S`|Handle sparse files efficiently.|

|**Overwright control Flag** |**Description**|
|:---|:---|
|`-k`|Don't replace existing files|
|`--keep-newer-files`|Don't replace existing files that are newer than the archives version|
|`--keep-directory-symlink`|Don't replace existing symlinks|
|`--no-overwrite-dir`|Preserve metadata of existing directories|
|`--one-top-level=DIR`|Extract all files into a DIR|
|`--overwrite`| Overwrite existing files|
|`--overwrite-dir`| Overwrite metadata of directories|
|`--recursive-unlink`| Recursivly remove all files in the directory before extracting|
|`--remove-files`| Remove files after adding them to a directory|
|`--skip-old-files`| Don't replace existing files when extracting|
|`-u`| Remove each file before extracting over it|
|`-w`| Verify the archive after writing it|
