# The `gzip` command

The `gzip` command in Linux/Unix is used to compress/decompress data.

# Usage

## Compress a file

**Action:**
--- Compressing a file

**Details:**
--- Reduce the size of the file by applying compression

**Command:**
```
gzip file_name
```

## Decompress a file

**Action:**
--- Decompressing a file

**Details:**
--- Restore the file's original form in terms of data and size

**Command:**
```
gzip -d archive_01.gz
```

## Compress multiple files:

**Action:**
--- Compress multiple files

**Details:**
--- Compress multiple files into multiple archives

**Command:**
```
gzip file_name_01 file_name_02 file_name_03
```

## Decompress multiple files:

**Action:**
--- Decompress multiple files

**Details:**
--- Decompress multiple files from multiple archives

**Command:**
```
gzip -d archive_01.gz archive_02.gz archive_03.gz
```

## Compress a directory:

**Action:**
--- Compress all the files in a directory

**Details:**
--- Compress multiple files under a directory in one single archive

**Command:**
```
gzip -r directory_name
```

## Decompress a directory:

**Action:**
--- Decompress all the files in a directory

**Details:**
--- Decompress multiple files under a directory from one single archive

**Command:**
```
gzip -dr directory_name
```

## Verbose (detailed) output while compressing:

**Action:**
--- Compress a file in a more verbose manner

**Details:**
--- Output more information about the action of the command

**Command:**
```
gzip -v file_name
```
