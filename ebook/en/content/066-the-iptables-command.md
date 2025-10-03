# The `iptables` command

The `iptables` command is a powerful firewall administration tool for Linux systems. It allows you to configure the Linux kernel firewall (netfilter) by setting up, maintaining, and inspecting the tables of IP packet filter rules.

## Syntax

```
iptables [options] [chain] [rule-specification] [target]
```

## Basic Concepts

### Tables
- **filter**: Default table for packet filtering (INPUT, OUTPUT, FORWARD)
- **nat**: Network Address Translation (PREROUTING, POSTROUTING, OUTPUT)
- **mangle**: Packet alteration (PREROUTING, POSTROUTING, INPUT, OUTPUT, FORWARD)
- **raw**: Connection tracking exemption (PREROUTING, OUTPUT)

### Chains
- **INPUT**: Incoming packets to local system
- **OUTPUT**: Outgoing packets from local system
- **FORWARD**: Packets routed through the system
- **PREROUTING**: Packets before routing decision
- **POSTROUTING**: Packets after routing decision

### Targets
- **ACCEPT**: Allow the packet
- **DROP**: Silently discard the packet
- **REJECT**: Discard and send error message
- **LOG**: Log the packet and continue processing
- **DNAT**: Destination NAT
- **SNAT**: Source NAT
- **MASQUERADE**: Dynamic source NAT

## Basic Commands

### Listing Rules

```bash
# List all rules
sudo iptables -L

# List rules with line numbers
sudo iptables -L --line-numbers

# List rules in specific table
sudo iptables -t nat -L
sudo iptables -t mangle -L

# Show packet and byte counters
sudo iptables -L -v

# Show rules in iptables-save format
sudo iptables -S
```

### Basic Rule Operations

```bash
# Add rule to end of chain
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Insert rule at specific position
sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT

# Delete specific rule
sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT

# Delete rule by line number
sudo iptables -D INPUT 3

# Replace rule at specific position
sudo iptables -R INPUT 1 -p tcp --dport 443 -j ACCEPT
```

## Common Rule Examples

### 1. Allow/Block Specific Ports

```bash
# Allow SSH (port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP (port 80)
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Allow HTTPS (port 443)
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Block specific port
sudo iptables -A INPUT -p tcp --dport 8080 -j DROP
```

### 2. Allow/Block by IP Address

```bash
# Allow specific IP
sudo iptables -A INPUT -s 192.168.1.100 -j ACCEPT

# Block specific IP
sudo iptables -A INPUT -s 192.168.1.50 -j DROP

# Allow subnet
sudo iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT

# Block IP range
sudo iptables -A INPUT -m iprange --src-range 192.168.1.100-192.168.1.200 -j DROP
```

### 3. Allow/Block by Interface

```bash
# Allow traffic on loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow on specific interface
sudo iptables -A INPUT -i eth0 -p tcp --dport 80 -j ACCEPT

# Block on specific interface
sudo iptables -A INPUT -i eth1 -j DROP
```

## Advanced Rules

### 1. Stateful Connections

```bash
# Allow established and related connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow new connections on specific ports
sudo iptables -A INPUT -m state --state NEW -p tcp --dport 22 -j ACCEPT
```

### 2. Rate Limiting

```bash
# Limit SSH connections (6 per minute)
sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 6/min -j ACCEPT

# Limit ping requests
sudo iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/sec -j ACCEPT
```

### 3. Time-based Rules

```bash
# Allow access during business hours
sudo iptables -A INPUT -p tcp --dport 80 -m time --timestart 09:00 --timestop 17:00 -j ACCEPT

# Allow access on weekdays
sudo iptables -A INPUT -p tcp --dport 22 -m time --weekdays Mon,Tue,Wed,Thu,Fri -j ACCEPT
```

### 4. Multiport Rules

```bash
# Allow multiple ports
sudo iptables -A INPUT -p tcp -m multiport --dports 22,80,443 -j ACCEPT

# Block multiple ports
sudo iptables -A INPUT -p tcp -m multiport --dports 135,445,1433 -j DROP
```

## NAT Configuration

### 1. Source NAT (SNAT)

```bash
# Static SNAT
sudo iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j SNAT --to-source 203.0.113.1

# Dynamic SNAT (Masquerading)
sudo iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE
```

### 2. Destination NAT (DNAT)

```bash
# Port forwarding
sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 192.168.1.100:80

# Forward to different IP
sudo iptables -t nat -A PREROUTING -d 203.0.113.1 -j DNAT --to-destination 192.168.1.100
```

## Policy Configuration

### Default Policies

```bash
# Set default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# View current policies
sudo iptables -L | grep "policy"
```

### Chain Management

```bash
# Create custom chain
sudo iptables -N CUSTOM_CHAIN

# Delete custom chain (must be empty)
sudo iptables -X CUSTOM_CHAIN

# Flush specific chain
sudo iptables -F INPUT

# Flush all chains
sudo iptables -F
```

## Logging

```bash
# Log dropped packets
sudo iptables -A INPUT -j LOG --log-prefix "DROPPED: " --log-level 4

# Log before dropping
sudo iptables -A INPUT -p tcp --dport 23 -j LOG --log-prefix "TELNET_ATTEMPT: "
sudo iptables -A INPUT -p tcp --dport 23 -j DROP

# View logs
sudo tail -f /var/log/syslog | grep "DROPPED:"
```

## Common Firewall Configurations

### 1. Basic Desktop Firewall

```bash
#!/bin/bash
# Clear existing rules
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X

# Default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Allow loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow ping
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
```

### 2. Web Server Firewall

```bash
#!/bin/bash
# Basic web server configuration
sudo iptables -F

# Default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Allow loopback and established connections
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH (limit attempts)
sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 6/min -j ACCEPT

# Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow ping
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
```

### 3. Router/Gateway Configuration

```bash
#!/bin/bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# NAT for internal network
sudo iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

# Allow forwarding for established connections
sudo iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow forwarding from internal network
sudo iptables -A FORWARD -s 192.168.1.0/24 -j ACCEPT
```

## Persistence

### 1. Save/Restore Rules

```bash
# Save current rules
sudo iptables-save > /etc/iptables/rules.v4

# Restore rules
sudo iptables-restore < /etc/iptables/rules.v4

# Install persistence package (Ubuntu/Debian)
sudo apt install iptables-persistent
```

### 2. Automatic Loading

```bash
# Create systemd service
sudo vim /etc/systemd/system/iptables-restore.service

[Unit]
Description=Restore iptables firewall rules
Before=network-pre.target

[Service]
Type=oneshot
ExecStart=/sbin/iptables-restore /etc/iptables/rules.v4

[Install]
WantedBy=multi-user.target

# Enable service
sudo systemctl enable iptables-restore.service
```

## Troubleshooting

### 1. Testing Rules

```bash
# Test connectivity
telnet target-ip port
nc -zv target-ip port

# Check if rule matches
sudo iptables -L -v -n | grep "rule-description"

# Monitor rule usage
watch "sudo iptables -L -v -n"
```

### 2. Debugging

```bash
# Enable all logging temporarily
sudo iptables -A INPUT -j LOG --log-prefix "INPUT: "
sudo iptables -A OUTPUT -j LOG --log-prefix "OUTPUT: "
sudo iptables -A FORWARD -j LOG --log-prefix "FORWARD: "

# Monitor logs
sudo tail -f /var/log/syslog | grep "INPUT:\|OUTPUT:\|FORWARD:"
```

### 3. Emergency Access

```bash
# Temporary rule to allow all (emergency)
sudo iptables -I INPUT 1 -j ACCEPT

# Flush all rules (removes all protection)
sudo iptables -F
sudo iptables -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
```

## Security Best Practices

### 1. Default Deny Policy

```bash
# Always start with deny-all policy
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
# Keep OUTPUT as ACCEPT for normal operation
```

### 2. Order Matters

```bash
# More specific rules should come first
sudo iptables -I INPUT 1 -s 192.168.1.100 -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

### 3. Rate Limiting Critical Services

```bash
# Protect SSH from brute force
sudo iptables -A INPUT -p tcp --dport 22 -m recent --set --name SSH
sudo iptables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 3 --name SSH -j DROP
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

## Performance Considerations

```bash
# Use connection tracking for better performance
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Place frequently matched rules first
sudo iptables -I INPUT 1 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Use specific matches to reduce processing
sudo iptables -A INPUT -p tcp --dport 80 -s 192.168.1.0/24 -j ACCEPT
```

## Important Notes

- Always test rules before making them permanent
- Keep a way to access the system if rules block you out
- Use specific protocols and ports rather than blanket rules
- Monitor logs to understand traffic patterns
- Document your firewall rules for future reference
- Regular backup of working configurations
- Consider using UFW for simpler firewall management

The `iptables` command provides comprehensive firewall capabilities but requires careful planning and testing to avoid security issues or system lockouts.

For more details, check the manual: `man iptables`
