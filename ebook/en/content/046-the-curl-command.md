# The `curl` command

In linux, `curl` is a tool to transfer data from or to a server, using one of the supported protocols(DICT, FILE ,FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP).

## Example :

```bash
$ curl example.com
```

The command will print the source code of the example.com homepage in the terminal window.

## The syntax of the `curl` command is :

```bash
$ curl [options...] <url>
```

## Options :

Options start with one or two dashes. Many of the options require an additional value next to them.

The short "single-dash" form of the options, `-d` for example, may be used with or without a space between it and its value, although a space is a recommended separator. The long "double-dash" form, `-d`, `--data` for example, requires a space between it and its value.

Short version options that don't need any additional values can be used immediately next to each other, like for example you can specify all the options `-O`, `-L` and `-v` at once as `-OLv`.

In general, all boolean options are enabled with `--option` and yet again disabled with `--no-option`. That is, you use the exact same option name but prefix it with `no-`. However, in this list we mostly only list and show the `--option` version of them. (This concept with `--no` options was added in 7.19.0. Previously most options were toggled on/off through repeated use of the same command line option.)

## Installation:

The curl command comes with most of the Linux distributions. But, if the system does not carry the curl by default. You need to install it manually. To install the curl, execute the following commands:

Update the system by executing the following commands:

```bash
$ sudo apt update
$ sudo apt upgrade
```
Now, install the curl utility by executing the below command:

```bash
$ sudo apt install curl
```

Verify the installation by executing the below command:

```bash
$ curl -version
```

The above command will display the installed version of the curl command.
