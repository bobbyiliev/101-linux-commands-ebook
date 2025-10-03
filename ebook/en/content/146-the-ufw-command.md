# The `ufw` command

UFW (Uncomplicated Firewall) is a user-friendly command-line frontend for managing iptables firewall rules on Ubuntu and other Debian-based systems. It provides a simple way to configure firewall rules without dealing with complex iptables syntax.

## Syntax

```
ufw [options] command [parameters]
```

## Installation

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ufw

# Check if UFW is installed
which ufw
```

## Basic Commands

### Enable/Disable UFW

```bash
# Enable UFW
sudo ufw enable

# Disable UFW
sudo ufw disable

# Check UFW status
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered
```

## Basic Rules

### Allow/Deny Traffic

1. **Allow specific ports**

```bash
# Allow SSH (port 22)
sudo ufw allow 22
sudo ufw allow ssh

# Allow HTTP (port 80)
sudo ufw allow 80
sudo ufw allow http

# Allow HTTPS (port 443)
sudo ufw allow 443
sudo ufw allow https

# Allow custom port
sudo ufw allow 8080
```

2. **Deny specific ports**

```bash
# Deny port 80
sudo ufw deny 80

# Deny SSH from specific IP
sudo ufw deny from 192.168.1.100 to any port 22
```

3. **Allow/Deny by service name**

```bash
# Allow common services
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ftp
sudo ufw allow smtp
```

## Advanced Rules

### Port Ranges

```bash
# Allow port range
sudo ufw allow 1000:2000/tcp
sudo ufw allow 1000:2000/udp

# Allow specific protocol
sudo ufw allow 53/udp  # DNS
sudo ufw allow 53/tcp  # DNS over TCP
```

### IP Address Rules

1. **Allow/Deny specific IP addresses**

```bash
# Allow from specific IP
sudo ufw allow from 192.168.1.100

# Deny from specific IP
sudo ufw deny from 192.168.1.50

# Allow subnet
sudo ufw allow from 192.168.1.0/24
```

2. **Allow IP to specific port**

```bash
# Allow specific IP to SSH
sudo ufw allow from 192.168.1.100 to any port 22

# Allow subnet to web server
sudo ufw allow from 10.0.0.0/8 to any port 80
```

### Interface-specific Rules

```bash
# Allow on specific interface
sudo ufw allow in on eth0 to any port 80

# Allow out on specific interface
sudo ufw allow out on eth1 to any port 443
```

## Rule Management

### List Rules

```bash
# Show status and rules
sudo ufw status

# Show numbered rules
sudo ufw status numbered

# Show verbose status
sudo ufw status verbose
```

### Delete Rules

```bash
# Delete by rule number
sudo ufw delete 3

# Delete by specifying the rule
sudo ufw delete allow 80
sudo ufw delete allow from 192.168.1.100
```

### Insert Rules

```bash
# Insert rule at specific position
sudo ufw insert 1 allow from 192.168.1.0/24
```

## Default Policies

```bash
# Set default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw default deny forward

# Check current defaults
sudo ufw status verbose
```

## Application Profiles

### List Available Profiles

```bash
# List application profiles
sudo ufw app list

# Show profile info
sudo ufw app info OpenSSH
sudo ufw app info "Apache Full"
```

### Use Application Profiles

```bash
# Allow application
sudo ufw allow OpenSSH
sudo ufw allow "Apache Full"
sudo ufw allow "Nginx Full"

# Common application profiles
sudo ufw allow "OpenSSH"
sudo ufw allow "Apache"
sudo ufw allow "Apache Secure"
sudo ufw allow "Nginx HTTP"
sudo ufw allow "Nginx HTTPS"
sudo ufw allow "Nginx Full"
```

## Logging

```bash
# Enable logging
sudo ufw logging on

# Set log level
sudo ufw logging low
sudo ufw logging medium
sudo ufw logging high

# Disable logging
sudo ufw logging off

# View logs
sudo tail -f /var/log/ufw.log
```

## Reset and Reload

```bash
# Reset all rules to default
sudo ufw --force reset

# Reload UFW
sudo ufw reload
```

## Common Use Cases

### 1. Basic Web Server Setup

```bash
# Allow SSH, HTTP, and HTTPS
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

### 2. Database Server (MySQL)

```bash
# Allow MySQL only from application servers
sudo ufw allow from 192.168.1.10 to any port 3306
sudo ufw allow from 192.168.1.11 to any port 3306
```

### 3. Development Server

```bash
# Allow common development ports
sudo ufw allow 3000  # Node.js
sudo ufw allow 8000  # Django
sudo ufw allow 5000  # Flask
sudo ufw allow 4200  # Angular
```

### 4. Mail Server

```bash
# Allow mail server ports
sudo ufw allow smtp      # Port 25
sudo ufw allow 587/tcp   # SMTP submission
sudo ufw allow 993/tcp   # IMAPS
sudo ufw allow 995/tcp   # POP3S
```

### 5. DNS Server

```bash
# Allow DNS traffic
sudo ufw allow 53/tcp
sudo ufw allow 53/udp
```

## Security Best Practices

### 1. Principle of Least Privilege

```bash
# Start with deny all
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Only allow what's needed
sudo ufw allow ssh
sudo ufw allow from 192.168.1.0/24 to any port 80
```

### 2. Limit SSH Access

```bash
# Limit SSH attempts (6 attempts in 30 seconds)
sudo ufw limit ssh

# Allow SSH only from specific networks
sudo ufw allow from 192.168.1.0/24 to any port 22
sudo ufw deny ssh
```

### 3. Monitor and Log

```bash
# Enable logging
sudo ufw logging medium

# Monitor logs
sudo tail -f /var/log/ufw.log | grep DPT
```

## Troubleshooting

### 1. Check Current Rules

```bash
sudo ufw status numbered
sudo iptables -L -n
```

### 2. Test Connections

```bash
# Test if port is accessible
telnet your-server-ip 80
nc -zv your-server-ip 22
```

### 3. Debug UFW

```bash
# Dry run (show what would happen)
sudo ufw --dry-run allow 80

# Check UFW version
ufw --version
```

## Advanced Configuration

### 1. Custom Rules File

```bash
# Edit UFW rules directly
sudo vim /etc/ufw/user.rules
sudo vim /etc/ufw/user6.rules
```

### 2. Rate Limiting

```bash
# Limit connections per IP
sudo ufw limit ssh
sudo ufw limit 80/tcp
```

### 3. Port Forwarding

```bash
# Enable IP forwarding
echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/ufw/sysctl.conf

# Add NAT rules to /etc/ufw/before.rules
```

## Integration with Services

### 1. Docker Integration

```bash
# Allow Docker containers
sudo ufw allow from 172.17.0.0/16

# Block Docker bypass (in /etc/ufw/after.rules)
```

### 2. Fail2ban Integration

```bash
# UFW works with fail2ban
sudo apt install fail2ban
# Configure fail2ban to use UFW actions
```

## Important Notes

- UFW is a frontend for iptables, not a replacement
- Rules are processed in order (first match wins)
- Default policies apply when no specific rule matches
- UFW doesn't interfere with existing iptables rules by default
- Always test rules before enabling in production
- Keep SSH access rule before enabling UFW remotely

## Quick Reference

```bash
# Essential commands
sudo ufw enable                    # Enable firewall
sudo ufw status                    # Check status
sudo ufw allow 22                  # Allow SSH
sudo ufw allow from 192.168.1.0/24 # Allow subnet
sudo ufw delete 3                  # Delete rule #3
sudo ufw reset                     # Reset all rules
sudo ufw reload                    # Reload configuration
```

UFW provides an excellent balance between simplicity and functionality, making it ideal for system administrators who need effective firewall management without iptables complexity.

For more details, check the manual: `man ufw`
