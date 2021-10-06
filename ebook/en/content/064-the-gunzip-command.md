# The `gunzip` command

The `gunzip` command is an antonym command of [`gzip` command](015-the-gzip-command.md). In other words, it decompress files deflated by `gzip` command.

`gunzip` takes a list of files on its command line and replaces each file whose name ends with _.gz_, _-gz_, _.z_, _-z_, or *\_z* (ignoring case) and which begins with the correct magic number with an uncompressed file without the original extension. `gunzip` also recognizes the special extensions *.tgz* and *.taz* as shorthands for *.tar.gz* and  *.tar.Z*  respectively.

### Examples:

1. Uncompress a file

```
gunzip filename.gz
```

2. Recursively uncompress content inside a directory, that match extension (suffix) compressed formats accepted by `gunzip`:

```
gunzip -r directory_name/
```

3. Uncompress all files in the current/working directory whose suffix match *.tgz*:

```
gunzip -S .tgz *
```

4. List compressed and uncompressed sizes, compression ratio and uncompressed name of input compressed file/s:

```
gunzip -l file_1 file_2
```

### Syntax:

```
gunzip [ -acfhklLnNrtvV ] [-S suffix] [ name ...  ]
```

### Video tutorial about using gzip, gunzip and tar commands:

[This video](https://www.youtube.com/watch?v=OBtG8zfVwuI) shows how to compress and decompress in a Unix shell. It uses `gunzip` as decompression command.

### Additional Flags and their Functionalities:

|**Short Flag**|**Long Flag**|**Description**|
|:---|:---|:---|
|-c|--stdout|write on standard output, keep original files unchanged|
|-h|--help|give help information|
|-k|--keep|keep (don't delete) input files|
|-l|--list|list compressed file contents|
|-q|--quiet|suppress all warnings|
|-r|--recursive|operate recursively on directories|
|-S|--suffix=SUF|use suffix SUF on compressed files|
||--synchronous|synchronous output (safer if system crashes, but slower)|
|-t|--test|test compressed file integrity|
|-v|--verbose|verbose mode|
|-V|--version|display version number|
