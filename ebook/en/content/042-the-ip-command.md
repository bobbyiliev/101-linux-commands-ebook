# The `ip` command

The `ip` command is a powerful utility from the iproute2 package used for network administration tasks. It serves as the modern replacement for older networking tools like `ifconfig`, `route`, and `arp`. The `ip` command can show or manipulate routing, network devices, interfaces, and tunnels.

## Syntax

```
ip [ OPTIONS ] OBJECT { COMMAND | help }
```

## Key Features

- **Interface Management**: Configure and monitor network interfaces
- **IP Address Management**: Add, remove, and display IP addresses
- **Routing Control**: Manage routing tables and routes
- **Neighbor Management**: Handle ARP/neighbor cache entries
- **Network Namespaces**: Work with network namespaces
- **Tunneling**: Create and manage network tunnels

## Basic Usage

### Display Network Interfaces

```bash
# Show all network interfaces
ip link show

# Show specific interface
ip link show eth0

# Show interface statistics
ip -s link show eth0
```

### IP Address Management

```bash
# Show all IP addresses
ip addr show

# Show addresses for specific interface
ip addr show eth0

# Add IP address to interface
sudo ip addr add 192.168.1.100/24 dev eth0

# Remove IP address from interface
sudo ip addr del 192.168.1.100/24 dev eth0

# Flush all addresses from interface
sudo ip addr flush dev eth0
```

## Interface Management

### Bringing Interfaces Up/Down

```bash
# Bring interface up
sudo ip link set eth0 up

# Bring interface down
sudo ip link set eth0 down

# Set interface MTU
sudo ip link set eth0 mtu 1400

# Change MAC address
sudo ip link set eth0 address 00:11:22:33:44:55
```

### Creating Virtual Interfaces

```bash
# Create VLAN interface
sudo ip link add link eth0 name eth0.100 type vlan id 100

# Create bridge interface
sudo ip link add name br0 type bridge

# Create virtual ethernet pair
sudo ip link add veth0 type veth peer name veth1

# Delete virtual interface
sudo ip link delete veth0
```

## Routing Management

### Viewing Routes

```bash
# Show routing table
ip route show

# Show routes for specific destination
ip route get 8.8.8.8

# Show routes via specific interface
ip route show dev eth0

# Show IPv6 routes
ip -6 route show
```

### Managing Routes

```bash
# Add default route
sudo ip route add default via 192.168.1.1

# Add specific route
sudo ip route add 10.0.0.0/8 via 192.168.1.1

# Add route via specific interface
sudo ip route add 172.16.0.0/16 dev eth1

# Delete route
sudo ip route del 10.0.0.0/8

# Replace existing route
sudo ip route replace default via 192.168.1.254
```

### Multiple Routing Tables

```bash
# Show all routing tables
ip route show table all

# Add route to specific table
sudo ip route add 192.168.2.0/24 via 10.0.0.1 table 100

# Show specific routing table
ip route show table 100

# Add routing rule
sudo ip rule add from 192.168.1.0/24 table 100
```

## Neighbor (ARP) Management

### ARP Cache Operations

```bash
# Show ARP cache
ip neigh show

# Show neighbors for specific interface
ip neigh show dev eth0

# Add static ARP entry
sudo ip neigh add 192.168.1.50 lladdr 00:11:22:33:44:55 dev eth0

# Delete ARP entry
sudo ip neigh del 192.168.1.50 dev eth0

# Flush ARP cache
sudo ip neigh flush all
```

## Advanced Features

### Network Namespaces

```bash
# List network namespaces
ip netns list

# Create network namespace
sudo ip netns add myns

# Execute command in namespace
sudo ip netns exec myns ip addr show

# Delete network namespace
sudo ip netns del myns

# Move interface to namespace
sudo ip link set eth1 netns myns
```

### Tunneling

```bash
# Create GRE tunnel
sudo ip tunnel add gre1 mode gre remote 10.0.0.2 local 10.0.0.1 ttl 255

# Create IPIP tunnel
sudo ip tunnel add ipip1 mode ipip remote 192.168.1.2 local 192.168.1.1

# Show tunnels
ip tunnel show

# Delete tunnel
sudo ip tunnel del gre1
```

### Traffic Control

```bash
# Show queueing disciplines
ip qdisc show

# Add traffic shaping
sudo ip qdisc add dev eth0 root handle 1: htb default 30

# Show traffic control statistics
ip -s qdisc show dev eth0
```

## Monitoring and Statistics

### Interface Statistics

```bash
# Show detailed interface statistics
ip -s link show

# Show extended statistics
ip -s -s link show eth0

# Monitor interface changes
ip monitor link

# Monitor address changes
ip monitor addr
```

### Real-time Monitoring

```bash
# Monitor all network events
ip monitor

# Monitor only route changes
ip monitor route

# Monitor with timestamps
ip -t monitor
```

## Common Options

### General Options

```bash
# Use specific protocol family
ip -4 addr show    # IPv4 only
ip -6 addr show    # IPv6 only

# Show more details
ip -d link show

# Output in JSON format
ip -j addr show

# Colorize output
ip -c addr show

# Don't resolve names
ip -n route show
```

### Batch Operations

```bash
# Execute commands from file
sudo ip -batch commands.txt

# Example batch file content:
# link set eth0 up
# addr add 192.168.1.100/24 dev eth0
# route add default via 192.168.1.1
```

## Practical Examples

### Setting Up Static IP

```bash
# Complete static IP configuration
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.1.1

# Add DNS (edit /etc/resolv.conf)
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

### Creating Bridge with VLANs

```bash
# Create bridge
sudo ip link add name br0 type bridge

# Create VLAN interfaces
sudo ip link add link eth0 name eth0.10 type vlan id 10
sudo ip link add link eth0 name eth0.20 type vlan id 20

# Add interfaces to bridge
sudo ip link set eth0.10 master br0
sudo ip link set eth0.20 master br0

# Bring everything up
sudo ip link set br0 up
sudo ip link set eth0.10 up
sudo ip link set eth0.20 up
```

### Network Troubleshooting

```bash
# Check connectivity path
ip route get 8.8.8.8

# Verify interface status
ip link show | grep -E "(UP|DOWN)"

# Check for duplicate IPs
ip addr show | grep inet

# Monitor network changes
ip monitor all
```

## Options Reference

|**Option**|**Description**|
|:---|:---|
|`-4, -6`|Use IPv4 or IPv6 protocol family|
|`-b, -batch`|Read commands from file|
|`-c, -color`|Use colored output|
|`-d, -details`|Show detailed information|
|`-f, -family`|Specify protocol family|
|`-h, -human`|Human readable output|
|`-j, -json`|JSON output format|
|`-n, -numeric`|Don't resolve names|
|`-o, -oneline`|Single line output|
|`-r, -resolve`|Resolve hostnames|
|`-s, -stats`|Show statistics|
|`-t, -timestamp`|Show timestamps|

## Objects Reference

|**Object**|**Description**|
|:---|:---|
|`link`|Network device (interface)|
|`addr`|IPv4 or IPv6 address|
|`route`|Routing table entry|
|`rule`|Rule in routing policy database|
|`neigh`|Neighbor (ARP) table entry|
|`ntable`|Neighbor table configuration|
|`tunnel`|Tunnel over IP|
|`maddr`|Multicast address|
|`mroute`|Multicast routing cache entry|
|`monitor`|Watch for netlink messages|

## Important Notes

- The `ip` command requires root privileges for most configuration changes
- Changes made with `ip` are immediate but not persistent across reboots
- For persistent configuration, use network configuration files or NetworkManager
- Always backup network configuration before making changes
- Use `ip` over deprecated tools like `ifconfig` and `route`

## Integration with NetworkManager

```bash
# Check if NetworkManager is managing interface
nmcli device status

# Temporarily disable NetworkManager for interface
sudo nmcli device set eth0 managed no

# Re-enable NetworkManager management
sudo nmcli device set eth0 managed yes
```

The `ip` command is essential for modern Linux network administration and provides comprehensive control over network configuration.

For more details, check the manual: `man ip`

