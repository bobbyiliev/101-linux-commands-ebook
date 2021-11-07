# The `fdisk` command

The `fdisk` command is used for controlling the disk partition table and making changes to it and this is a list of some of options provided by it : </b>
- Organize space for new drives.
- Modify old drives.
- Create space for new partitions.
- Move data to new partitions.
  

### Examples:

1. To view basic details about all available partitions on the system:

```
fdisk -l
```

2. To show the size of the partition:

```
fdisk -s /dev/sda
```

3. To view the help message and all options of the command:
```
fdisk -h
```

### Syntax:

```
fdisk [options] device
```

### Some of the command options:

On writing the following command 
```
fdisk /dev/sdb
```
the following window appears :
![Options](https://media.geeksforgeeks.org/wp-content/uploads/20190219152451/Screenshot-711.png)
and then you type m which will show you all options you need such as creating new partition and deleting a partition as in the following picture :
![Options](https://media.geeksforgeeks.org/wp-content/uploads/20190219153114/Screenshot-741.png)






