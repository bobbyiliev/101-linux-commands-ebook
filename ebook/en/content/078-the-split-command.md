# The `split` command

The `split` command in Linux is used to split a file into smaller files.

### Examples

1. Split a file into a smaller file using file name

```
split filename.txt
```

2. Split a file named filename into segments of 200 lines beginning with prefix file

```
split -l 200 filename file
```

This will create files of the name fileaa, fileab, fileac, filead, etc. of 200 lines.

3. Split a file named filename into segments of 40 bytes with prefix file

```
split -b 40 filename file
```

This will create files of the name fileaa, fileab, fileac, filead, etc. of 40 bytes.

4. Split a file using --verbose to see the files being created.

```
split filename.txt --verbose
```

### Syntax:

```
split [options] filename [prefix]
```

### Additional Flags and their Functionalities

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-a`|`--suffix-length=N`|Generate suffixes of length N (default 2)| 
||`--additional-suffix=SUFFIX`|Append an additional SUFFIX to file names|
|`-b`|`--bytes=SIZE`|Put SIZE bytes per output file|
|`-C`|`--line-bytes=SIZE`|Put at most SIZE bytes of records per output file|
|`-d`| |Use numeric suffixes starting at 0, not alphabetic|
||`--numeric-suffixes[=FROM]`|Same as -d, but allow setting the start value|
|`-x`||Use hex suffixes starting at 0, not alphabetic|
||`--hex-suffixes[=FROM]`|Same as -x, but allow setting the start value|
|`-e`|`--elide-empty-files`|Do not generate empty output files with '-n'|
||`--filter=COMMAND`|Write to shell COMMAND;<br>file name is $FILE|
|`-l`|`--lines=NUMBER`|Put NUMBER lines/records per output file|
|`-n`|`--number=CHUNKS`|Generate CHUNKS output files;<br>see explanation below|
|`-t`|`--separator=SEP`|Use SEP instead of newline as the record separator;<br>'\0' (zero) specifies the NUL character|
|`-u`|`--unbuffered`|Immediately copy input to output with '-n r/...'|
||`--verbose`|Print a diagnostic just before each<br>output file is opened|
||`--help`|Display this help and exit|
||`--version`|Output version information and exit|

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

CHUNKS may be:
|**CHUNKS**   |**Description**   |
|:---|:---|
|`N`|Split into N files based on size of input|
|`K/N`|Output Kth of N to stdout|
|`l/N`|Split into N files without splitting lines/records|
|`l/K/N`|Output Kth of N to stdout without splitting lines/records|
|`r/N`|Like 'l' but use round robin distribution|
|`r/K/N`|Likewise but only output Kth of N to stdout|


