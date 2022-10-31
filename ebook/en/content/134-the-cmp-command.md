# The `cmp` command

The `cmp` command is used to compare the two files byte by byte.

Example:
```
cmp file1.txt file2.txt
```

Syntax:
```
cmp [option] File1 File2
```

## Few Examples :

1. ### Comparison of two files:

Perform a simple comparison of the two files to check out if they differ from each other or not.

Example:
```
cmp File1 File2
```

2. ### Comparing Files after Skipping a Specified Number of Bytes:

Compare two files after skipping a certain number of bytes

Example:
```
cmp -i 2 list.txt list2.txt
```

Here “INT” represents the number of bytes to be skipped

3. ### Display the Differing Bytes of the Files in the Output:

Example: 
```
cmp -b list.txt list1.txt
```
4. ### Display Byte Numbers and Differing Byte Values of the Files in the Output:

Example: 
```
cmp -l list.txt list1.txt
```

5. ### Comparing the First “n” Number of Bytes of the Files:

Example:
```
cmp -n 10 list.txt list2.txt 
```
### Additional Flags and their Functionalities

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-b`|`--print-bytes`|print differing bytes|
|`-i`|`--ignore-initial=SKIP`|skip first SKIP bytes of both inputs|
|`-i`|`--ignore-initial=SKIP1:SKIP2`|skip first SKIP1 bytes of FILE1 and first SKIP2 bytes of FILE2|
|`-l`|`--verbose`|output byte numbers and differing byte values|
|`-n`|`--bytes=LIMIT`|compare at most LIMIT bytes|
|`-s`|`--quiet, --silent`|suppress all normal output|
|`v`|`--version`|output version information and exit|
||`--help`|Display this help and exit|

