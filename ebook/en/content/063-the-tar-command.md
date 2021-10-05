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

|**Flag**   |**Description**   |
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
|`w`| Verify a archive file |
|`r`|update or add file or directory in already existed .tar file |
