# The `netstat` command

The term `netstat` stands for Network Statistics. In layman’s terms, netstat command displays the current network connections, networking protocol statistics, and a variety of other interfaces.  
  
Check if you have `netstat` on your PC:

```
netstat –v
```


If you don't have `netstat` installed on your PC, you can install it with the following command:

```
sudo apt install net-tools
```  

### You can use `netstat` command for some use cases given below:

- `Netstat` command with `-nr` flag shows the routing table detail on the terminal.

Example:

```
netstat  -nr
```

- `Netstat` command with  `-i` flag shows statistics for the currently configured network interfaces.
This command will display the first 10 lines of file `foo.txt` .
  
Example:

```
netstat  -i
```

- `Netstat` command with `-tunlp` will gives a list of networks, their current states, and their associated ports.

Example:

```
netstat -tunlp
```

- You can get the list of all TCP port connection by using `-at` with  `netstat`.

```
netstat  -at
```

- You can get the list of all UDP port connection by using `-au` with  `netstat`.
```
netstat  -au
```

- You can get the list of all active connection by using `-l` with  `netstat`.

```
netstat  -l
```
