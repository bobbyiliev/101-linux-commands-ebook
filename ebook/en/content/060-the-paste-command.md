# The `paste` command

The `paste` command write lines of two or more files sequentially, separated by TABs to the standard output

### Syntax:

```[linux]
paste [OPTIONS]... [FILE]...
```

### Examples:

1. To paste two files

```[linux]
paste file1 file2
```

2. To paste two files using new line as delimiter

```[linux]
paste -d '\n' file1 file2
```

### Additional Flags and their Functionalities:

| **Short Flag**     | **Long Flag**               | **Description**                                                                                                                   |
| :----------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `-d`               | `--delimiter`                     | use charater of TAB |
| `-s`               | `--serial`              | paste one file at a time instead of in parallel |
| `-z`               | `--zero-terminated`          | set line delimiter to NUL, not newline |
|                | `--help`                    | print command help |
|                | `--version`          | print version information |
