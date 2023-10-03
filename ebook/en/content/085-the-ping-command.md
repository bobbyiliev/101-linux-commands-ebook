# The `ping` command

The `ping` (Packet Internet Groper) command is a network utility used to check network connectivity between a host and a server or another host. It sends ICMP (Internet Control Message Protocol) echo requests to a specified IP address or URL and measures the time it takes to receive a response. This time delay is referred to as "latency." Ping is a fundamental tool for network troubleshooting and monitoring.

## Understanding Latency

Latency, in the context of networking, is the time delay between sending a packet and receiving a response. 

When you use the `ping` command, it measures the latency by sending a series of packets to the target host and calculating the time it takes for each packet to complete the round trip. The latency is typically measured in milliseconds (ms). Understanding latency is essential because:

- **Network Performance**: Lower latency means faster data transmission and more responsive network connections, which is critical for real-time applications.

- **Troubleshooting**: High latency can indicate network congestion, packet loss, or connectivity issues that need attention.

- **Quality of Service (QoS)**: Service providers and network administrators use latency metrics to ensure that network services meet quality standards.

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

3. Controlling the number of packets to send: 
Earlier we did not define the number of packets to send to the server/host by using -c option we can do so. 

 ```
ping -c 5 google.com
```

4. Controlling the size of the packet: 
Earlier a default sized packets were sent to a host but we can send light and heavy packet by using 
-s option. 

```
ping -s 40 -c 5 google.com
```

5. Changing the time interval between ping packets: 
By default ping wait for 1 sec to send next packet we can change this time by using -i option.  

```
ping -i 2 google.com
```


