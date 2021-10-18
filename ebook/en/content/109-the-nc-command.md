# The `nc` command

The `nc` (or netcat) command is used to perform any operation involving TCP (Transmission Control Protocol, connection oriented), UDP (User Datagram Protocol, connection-less, no guarantee of data delivery) or UNIX-domain sockets. It can be thought of as swiss-army knife for communication protocol utilities.

### Syntax:

```
nc [options] [ip] [port]
```

### Examples:

#### 1. Open a TCP connection to port 80 of host, using port 1337 as source port with timeout of 5s:

```bash
$ nc -p 1337 -w 5 host.ip 80
```

#### 2. Open a UDP connection to port 80 on host:

```bash
$ nc -u host.ip 80
```

#### 3. Create and listen on UNIX-domain stream socket:

```bash
$ nc -lU /var/tmp/dsocket
```

#### 4. Create a basic server/client model:

This creates a connection, with no specific server/client sides with respect to nc, once the connection is established.

```bash
$ nc -l 1234 # in one console

$ nc 127.0.0.1 1234 # in another console
```

#### 5. Build a basic data transfer model:

After the file has been transferred, sequentially, the connection closes automatically

```bash
$ nc -l 1234 > filename.out # to start listening in one console and collect data

$ nc host.ip 1234 < filename.in
```

#### 6. Talk to servers:

Basic example of retrieving the homepage of the host, along with headers.

```bash
$ printf "GET / HTTP/1.0\r\n\r\n" | nc host.ip 80
```

#### 7. Port scanning:

Checking which ports are open and running services on target machines. `-z` flag commands to inform about those rather than initiate a connection.

```bash
$ nc -zv host.ip 20-2000 # range of ports to check for
```

### Flags and their Functionalities:

| **Short Flag** | **Description**                                                   |
| -------------- | ----------------------------------------------------------------- |
| `-4`           | Forces nc to use IPv4 addresses                                   |
| `-6`           | Forces nc to use IPv6 addresses                                   |
| `-b`           | Allow broadcast                                                   |
| `-D`           | Enable debugging on the socket                                    |
| `-i`           | Specify time interval delay between lines sent and received       |
| `-k`           | Stay listening for another connection after current is over       |
| `-l`           | Listen for incoming connection instead of initiate one to remote  |
| `-T`           | Specify length of TCP                                             |
| `-p`           | Specify source port to be used                                    |
| `-r`           | Specify source and/or destination ports randomly                  |
| `-s`           | Specify IP of interface which is used to send the packets         |
| `-U`           | Use UNIX-domain sockets                                           |
| `-u`           | Use UDP instead of TCP as protocol                                |
| `-w`           | Declare a timeout threshold for idle or unestablished connections |
| `-x`           | Should use specified protocol when talking to proxy server        |
| `-z`           | Specify to scan for listening daemons, without sending any data   |
