# The `ssh` command

The `ssh` command in Linux stands for "Secure Shell". It is a protocol used to securely connect to a remote server/system. ssh is more secure in the sense that it transfers the data in encrypted form between the host and the client. ssh runs at TCP/IP port 22.

### Examples:

1. Use a Different Port Number for SSH Connection: 	

```
ssh test.server.com -p 3322
```

2. -i ssh to remote server using a private key?

```
ssh -i private.key user_name@host
```

3. -l ssh specifying a different username

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
|`-B bind_interface`|Bind to the address of bind_interface before attempting to connect to the destination host.  This is only useful on systems with more than one address.|
|`-b bind_address`|Use bind_address on the local machine as the source address of the connection.  Only useful on systems with more than one address.
|`-C`|Compresses all data (including stdin, stdout, stderr, and data for forwarded X11 and TCP connections) for a faster transfer of data.|
|`-c cipher_spec`|Selects the cipher specification for encrypting the session.|
|`-D [bind_address:]port`|Dynamic application-level port forwarding. This allocates a socket to listen to port on the local side. When a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine.|
|`-E log_file`|Append debug logs instead of standard error.|
|`-e escape_char`|Sets the escape character for sessions with a pty (default: ‘~’).  The escape character is only recognized at the beginning of a line.  The escape character followed by a dot (‘.’) closes the connection; followed by control-Z suspends the connection; and followed by itself sends the escape character once.  Setting the character to “none” disables any escapes and makes the session fully transparent.|
|`-F configfile`|Specifies a per-user configuration file. The default for the per-user configuration file is ~/.ssh/config.|
|`-f`|Requests ssh to go to background just before command execution.|
|`-G`|Causes ssh to print its configuration after evaluating Host and Match blocks and exit.|
|`-g`|Allows remote hosts to connect to local forwarded ports.|
|`-I pkcs11`|Specify the PKCS#11 shared library ssh should use to communicate with a PKCS#11 token providing keys.|
|`-i identity_file`|A file from which the identity key (private key) for public key authentication is read.|
|`-J [user@]host[:port]`|Connect to the target host by first making a ssh connection to the pjump host[(/iam/jump-host) and then establishing a TCP forwarding to the ultimate destination from there.|
|`-K`|Enables GSSAPI-based authentication and forwarding (delegation) of GSSAPI credentials to the server.|
|`-k`|Disables forwarding (delegation) of GSSAPI credentials to the server.|
|`-L [bind_address:]port:host:hostport`, `-L [bind_address:]port:remote_socket`, `-L local_socket:host:hostport`, `-L local_socket:remote_socket`|Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side.  This works by allocating a socket to listen to either a TCP port on the local side, optionally bound to the specified bind_address, or to a Unix socket.  Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection is made to either host port hostport, or the Unix socket remote_socket, from the remote machine.|
|`-l login_name`|Specifies the user to log in as on the remote machine.|
|`-M`|Places the ssh client into “master” mode for connection sharing.  Multiple -M options places ssh into “master” mode but with confirmation required using ssh-askpass before each operation that changes the multiplexing state (e.g. opening a new session).|
|`-m mac_spec`|A comma-separated list of MAC (message authentication code) algorithms, specified in order of preference.|
|`-N`|Do not execute a remote command.  This is useful for just forwarding ports.|
|`-n`|Prevents reading from stdin.|
|`-O ctl_cmd`|Control an active connection multiplexing master process.  When the -O option is specified, the ctl_cmd argument is interpreted and passed to the master process.  Valid commands are: “check” (check that the master process is running), “forward” (request forwardings without command execution), “cancel” (cancel forwardings), “exit” (request the master to exit), and “stop” (request the master to stop accepting further multiplexing requests).|
|`-o`|Can be used to give options in the format used in the configuration file.  This is useful for specifying options for which there is no separate command-line flag.|
|`-p`, `--port PORT`|Port to connect to on the remote host.|
|`-Q query_option`|Queries ssh for the algorithms supported for the specified version 2.  The available features are: cipher (supported symmetric ciphers), cipher-auth (supported symmetric ciphers that support authenticated encryption), help (supported query terms for use with the -Q flag), mac (supported message integrity codes), kex (key exchange algorithms), kex-gss (GSSAPI key exchange algorithms), key (keytypes), key-cert (certificate key types), key-plain (non-certificate key types), key-sig (all keytypes and signature algorithms), protocol-version (supported SSH protocol versions), and sig (supported signature algorithms).  Alternatively, any keyword from ssh_config(5) or sshd_config(5) thattakes an algorithm list may be used as an alias for the corresponding query_option.|
|`-q`| Qiet mode. Causes most warning and diagnostic messages to be suppressed.|
|`-R [bind_address:]port:host:hostport, -R [bind_address:]port:local_socket, -R remote_socket:host:hostport, -R remote_socket:local_socket, -R [bind_address:]port`|Specifies that connections to the given TCP port or Unix socket on the remote (server) host are to be forwarded to the local side.|
|`-S ctl_path`|Specifies the location of a control socket for connection sharing, or the string “none” to disable connection sharing.|
|`-s`|May be used to request invocation of a subsystem on the remote system.  Subsystems facilitate the use of SSH as a secure transport for other applications (e.g. sftp(1)).  The subsystem is specified as the remote command.|
|`-T`| Disable pseudo-terminal allocation.|
|`-t`|Force pseudo-terminal allocation.  This can be used to execute arbitrary screen-based programs on a remote machine, which can be very useful, e.g. when implementing menu services.  Multiple -t options force tty allocation, even if ssh has no local tty.
|`-V`|Display the version number.|
|`-v`|Verbose mode. It echoes everything it is doing while establishing a connection. It is very useful in the debugging of connection failures.|
|`-W host:port`|Requests that standard input and output on the client be forwarded to host on port over the secure channel.  Implies -N, -T, ExitOnForwardFailure and ClearAllForwardings, though these can be overridden in the configuration file or using -o command line options.|
|`-w local_tun[remote_tun]`|Requests tunnel device forwarding with the specified tun devices between the client (local_tun) and the server (remote_tun).	The devices may be specified by numerical ID or the keyword “any”, which uses the next available tunnel device.  If remote_tun is not specified, it defaults to “any”.	If the Tunnel directive is unset, it will be set to the default tunnel mode, which is “point-to-point”.  If a different Tunnel forwarding mode it desired, then it should be specified before -w.|
|`-X`|Enables X11 forwarding (GUI Forwarding).|
|`-x`|Disables X11 forwarding (GUI Forwarding).|
|`-Y`|Enables trusted X11 Forwarding.|
|`-y`|Send log information using the syslog system module.  By default this information is sent to stderr.|
