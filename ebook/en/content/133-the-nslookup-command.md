# The `nslookup` command

The `nslookup` command is a network administration command-line tool for querying the Domain Name System (DNS) to obtain domain name or IP address mapping or any other specific DNS record.

## Syntax

```
nslookup [options] [host]
```

## Options
Some popular option flags include:

```
-domain=[domain-name]	Change the default DNS name.
-debug	Show debugging information.
-port=[port-number]	Specify the port for queries. The default port number is 53.
-timeout=[seconds]	Specify the time allowed for the server to respond.
-type=a	View information about the DNS A address records.
-type=any	View all available records.
-type=hinfo	View hardware-related information about the host.
-type=mx	View Mail Exchange server information.
-type=ns	View Name Server records.
-type=ptr	View Pointer records. Used in reverse DNS lookups.
-type=soa	View Start of Authority records.
```

## Few Examples:
1. Query DNS Server
```
nslookup www.google.com
```

2. Specify a port to query
```
nslookup -port=53 www.google.com
```

3. Get the MX Record
```
nslookup -type=mx google.com
```

Here I showed you how to use the nslookup command in Linux. Although there are other DNS lookup tools, such as dig, nslookup could be a better choice as it is a powerful tool present in almost every system.

For more details: [Nslookup on Wikipedia](https://en.wikipedia.org/wiki/Nslookup)