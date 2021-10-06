# The `bzip2` command

The `bzip2` command lets you to compress and decompress the files i.e. it helps in binding the files into a single file which takes less storage space as the original file use to take.

### Syntax:

```
bzip2 [OPTIONS] filenames ...
```

#### Note : Each file is replaced by a compressed version of itself, with the name original name of the file followed by extension bz2.

### Options and their Functionalities:

|**Option**   |**Alias**   |**Description**   |
|:---|:---|:---|
|`-d`|`--decompress`|to decompress compressed file|
|`-f`|`--force`|to force overwrite an existing output file|
|`-h`|`--help`|to display the help message and exit|
|`-k`|`--keep`|to enable file compression, doesn't deletes the original input file|
|`-L`|`--license`|to display the license terms and conditions|
|`-q`|`--quiet`|to suppress non-essential warning messages|
|`-t`|`--test`|to check integrity of the specified .bz2 file, but don't want to decompress them|
|`-v`|`--erbose`|to display details for each compression operation|
|`-V`|`--version`|to display the software version|
|`-z`|`--compress`|to enable file compression, but deletes the original input file|


> #### By default, when bzip2 compresses a file, it deletes the original (or input) file. However, if you don't want that to happen, use the -k command line option.

### Examples:

1. To force compression:
```
bzip2 -z input.txt
```
**Note: This option deletes the original file also**

2. To force compression and also retain original input file:
```
bzip2 -k input.txt
```

3. To force decompression: 
```
bzip2 -d input.txt.bz2
```

4. To test integrity of compressed file: 
```
bzip2 -t input.txt.bz2
```

5. To show the compression ratio for each file processed:
``` 
bzip2 -v input.txt
```
