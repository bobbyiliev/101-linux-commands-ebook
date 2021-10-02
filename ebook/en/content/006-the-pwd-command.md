 # The `PWD` command

The `pwd` stands for Print Working Directory. It prints the path of the working directory, starting from the root.
  
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

You can also check this by priting out the `$PWD` variable:

```
echo $PWD
```

The output would be the same as of the `pwd` command.

### Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links

By default, `pwd' behaves as if `-L' were specified.
 
