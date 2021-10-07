# The `ssh` command

The `ssh` command in Linux stands for "Secure Shell" Its is a protocal used to securely connect to a remote server/system. ssh is securer in the sense that it transfers the data in encrypted form between the host and the client. ssh runs at TCP/IP port 22.

### Examples:

1. Use a Different Port Number for SSH Connection: 	

```
ssh test.server.com -p 3322
```

2. -i ssh to remote server using a private key?

```
ssh -i private.key user_name@host
```

3. -l ssh speecifying a different user name

```
ssh -l alternative-username sample.ssh.com
```

### Syntax:

```
ssh user_name@host(IP/Domain_Name)
```
```
ssh -i private.key user_name@host
```
```
ssh sample.ssh.com  ls /tmp/doc
```


### Additional Flags and their Functionalities:

|**Flag**   |**Description**   |
|:---|:---|
|`-1`|Forces ssh to use protocol SSH-1 only.|
|`-2`|Forces ssh to use protocol SSH-2 only.|
|`-4`|Allows IPv4 addresses only.|
|`-A`|Authentication agent connection forwarding is enabled..|
|`-a`|Authentication agent connection forwarding is disabled.|
|`-C`|Compresses all data (including stdin, stdout, stderr, and data for forwarded X11 and TCP connections) for a faster transfer of data.|
|`-f`|Requests ssh to go to background just before command execution.|
|`-g`|Allows remote hosts to connect to local forwarded ports.|
|`-n`|Prevents reading from stdin.|
|`-p`, `--port PORT`|Port to connect to on the remote host.|
|`-i`|identity_file file from which the identity key (private key) for public key authentication is read.|
|`-l`|login_name Specifies the user to log in as on the remote machine.|
|`-q`|Suppresses all errors and warnings|
|`-V`|Display the version number.|
|`-v`|Verbose mode. It echoes everything it is doing while establishing a connection. It is very useful in the debugging of connection failures.|
|`-X`|Enables X11 forwarding (GUI Forwarding).|
|`-c cipher_spec`|Selects the cipher specification for encrypting the session. Specific cipher algorithm will be selected only if both the client and the server support it.|
