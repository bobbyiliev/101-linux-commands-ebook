# The `iptables` Command

The `iptables` command is used to set up and maintain tables for the Netfilter firewall for IPv4, included in the Linux kernel. The firewall matches packets with rules defined in these tables and then takes the specified action on a possible match.

### Syntax:
```
iptables --table TABLE -A/-C/-D... CHAIN rule --jump Target
```

### Example and Explanation:
*This command will append to the chain provided in parameters:*
```
iptables [-t table] --append [chain] [parameters]
```

*This command drops all the traffic coming on any port:*
```
iptables -t filter --append INPUT -j DROP
```
### Flags and their Functionalities:
|Flag|Description|
|:---|:---|
|`-C`|Check if a rule is present in the chain or not. It returns 0 if the rule exists and returns 1 if it does not.|
|`-A`|Append to the chain provided in parameters.|
|`-D`|Delete rule from the specified chain.|
