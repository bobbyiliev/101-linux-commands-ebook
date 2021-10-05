# The `env` command

The `env` command in Linux/Unix is used to either print a list of the current environment variables or to run a program in a custom environment without changing the current one. 

## Syntax

```bash
env [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]
```

## Usage

1. Print out the set of current environment variables
    ```bash 
    env 
    ```
2. Run a command with an empty environment
   ```bash 
    env -i command_name
    ```
3. Remove variable from the environment
    ```bash 
    env -u variable_name
    ```
4. End each output with NULL
    ```bash 
    env -0 
    ```

## Full List of Options

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-i`|`--ignore-environment`|Start with an empty environment|
|`-0`|`--null`|End each output line with NUL, not newline|
|`-u`|`--unset=NAME `|Remove variable from the environment|
|`-C`|`--chdir=DIR`|Change working directory to DIR|
|`-S`|`--split-string=S`|Process and split S into separate arguments. It's used to pass multiple arguments on shebang lines|
|`-v`|`--debug`|Print verbose information for each processing step|
|-|`--help`|Print a help message|
|-|`--version`|Print the version information|