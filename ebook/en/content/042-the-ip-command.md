# The `ip` command

The `ip` command is present in the net-tools which is used for performing several network administration tasks. IP stands for Internet Protocol. This command is used to show or manipulate routing, devices, and tunnels. It can perform tasks like configuring and modifying the default and static routing, setting up tunnel over IP, listing IP addresses and property information, modifying the status of the interface, assigning, deleting and setting up IP addresses and routes.

### Examples:

1. To assign an IP Address to a specific interface (eth1) :

```
 ip addr add 192.168.50.5 dev eth1
```

2. To show detailed information about network interfaces like IP Address, MAC Address information etc. :

```
ip addr show
```

### Syntax:

```
ip [ OPTIONS ] OBJECT { COMMAND | help }
```


### Additional Flags and their Functionalities:

|**Flag**   |**Description**   |
|:---|:---|
|`-a`| Display and modify IP Addresses |
|`-l`|Display and modify network interfaces |
|`-r`|Display and alter the routing table|
|`-n`|Display and manipulate neighbor objects (ARP table) |
|`-ru`|Rule in routing policy database.|
|`-s`|Output more information. If the option appears twice or more, the amount of information increases |
|`-f`|Specifies the protocol family to use|
|`-r`|Use the system's name resolver to print DNS names instead of host addresses|
|`-c`|To configure color output |

