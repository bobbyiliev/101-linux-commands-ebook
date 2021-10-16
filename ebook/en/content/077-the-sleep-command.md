# The `sleep` command

The `sleep` command is used to create a dummy job. A dummy job helps in delaying the execution. It takes time in seconds by default but a small suffix(s, m, h, d) can be added at the end to convert it into any other format. This command pauses the execution for an amount of time which is defined by NUMBER.

Note: If you will define more than one NUMBER with sleep command then this command will delay for the sum of the values.


### Examples :

1. To sleep for 10s

```
sleep 10s
```  

2. A more generalized command:

```
sleep NUMBER[SUFFIX]...
```

## Options
 It accepts the following options:
  
1.   --help
	   > display this help and exit
2.  --version
	 >  output version information and exit


---
