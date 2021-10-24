
# The `nice/renice` command

The `nice/renice` commands is used to modify the priority of the program to be executed. 
The priority range is between -20 and 19 where 19 is the lowest priority.
### Examples:

1. Running cc command in the background with a lower priority than default (slower):

```
nice -n 15 cc -c *.c &
```

2. Increase the priority to all processes belonging to group "test":

```
renice --20 -g test
```

### Syntax:

```
nice [  -Increment|  -n Increment ] Command [ Argument ... ]
```


### Flags : 

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-Increment`|<center>-</center>|Increment is the value of priority you want to assign.|
|`-n Increment`|<center>-</center>|Same as `-Increment`



