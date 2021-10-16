# The `sort` command

the `sort` command is used to sort a file, arranging the records in a particular order. By default, the sort command sorts a file assuming the contents are ASCII. Using options in the sort command can also be used to sort numerically. 

### Examples:

Suppose you create a data file with name file.txt: 
```
Command : 
$ cat > file.txt
abhishek
chitransh
satish
rajan
naveen
divyam
harsh
```

Sorting a file: Now use the sort command 

Syntax : 

```
sort filename.txt
```

```
Command:
$ sort file.txt

Output :
abhishek
chitransh
divyam
harsh
naveen 
rajan
satish
```

Note: This command does not actually change the input file, i.e. file.txt. 


### The sort function on a file with mixed case content 

i.e. uppercase and lower case: When we have a mix file with both uppercase and lowercase letters then first the upper case letters would be sorted following with the lower case letters.


Example: 

Create a file mix.txt 


```
Command :
$ cat > mix.txt
abc
apple
BALL
Abc
bat
```
Now use the sort command 

```
Command :
$ sort mix.txt
Output :
Abc                                                                                                                                                    
BALL                                                                                                                                                   
abc                                                                                                                                                    
apple                                                                                                                                                  
bat
```


