# The `pwd` command

The `pwd` stands for print working directory. It prints the path of the working directory, starting from the root.
  
Example:

```
pwd   
```  

The output would be your current directory:

```
/home/your_user/some_directory
```

Syntax:

```
pwd [OPTION] 
```  

Tip:

You can also check this by printing out the `$PWD` variable:

```
echo $PWD
```

The output would be the same as of the `pwd` command.

### Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links

#### Logical:

Use the `-L` option after the `pwd` command.

Syntax:
```
pwd -L
```

#### Physical:

If your environment includes symlinks, use `pwd` with `-P`

Syntax:
```
pwd -P
```

By default, `pwd` behaves as if `-L` were specified.