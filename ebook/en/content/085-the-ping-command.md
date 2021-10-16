# The `ping` command

The `ping` (Packet Internet Groper) command is used to check the network connectivity between host and server/host. This command takes as input the IP address or the URL and sends a data packet to the specified address with the message “PING” and get a response from the server/host this time is recorded which is called latency. Ping uses ICMP(Internet Control Message Protocol) to send an ICMP echo message to the specified host if that host is available then it sends ICMP reply message. Ping is generally measured in millisecond every modern operating system has this ping pre-installed.

The basic ping syntax includes ping followed by a hostname, a name of a website, or the exact IP address.

```
ping [option] [hostname] or [IP address]
```

### Examples:

1. To get ping version installed on your system. 

```
sudo ping -v
```

2. To check whether a remote host is up, in this case, google.com, type in your terminal:

```
ping google.com
```

3. Controlling the number of pings: 
Earlier we did not define the number of packets to send to the server/host by using -c option we can do so. 

 ```
ping -c 5 google.com
```

4. Controlling the number of pings: 
Earlier a default sized packets were sent to a host but we can send light and heavy packet by using 
-s option. 

```
ping -s 40 -c 5 google.com
```

5. Changing the time interval: 
By default ping wait for 1 sec to send next packet we can change this time by using -i option.  

```
ping -i 2 google.com
```


