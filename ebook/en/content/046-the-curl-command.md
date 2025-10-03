# The `curl` command

In Linux, curl is a powerful command-line tool used to transfer data from or to a server using a wide variety of protocols, including HTTP, HTTPS, and FTP. It is often used for testing APIs, downloading files, and automating web-related tasks.

## The syntax of the `curl` command :

```bash
$ curl [options...] <url>
```
The command will print the source code of the example.com homepage in the terminal window.

## Common Options :

curl has over 200 options! Here are some of the most common and useful ones.

| Option               | Long Version        | Description                                                            |
|----------------------|---------------------|------------------------------------------------------------------------|
| `-O`                 | `--remote-name`     | Downloads the file and saves it with the same name as the remote file.  |
| `-o <file>`          | `--output <file>`   | Saves the downloaded output to a specific filename.                    |
| `-L`                 | `--location`        | Follows redirects if the server reports that the requested page has moved. |
| `-X <METHOD>`        | `--request <METHOD>`| Specifies the HTTP request method to use (e.g., POST, PUT, DELETE).     |
| `-H <header>`        | `--header <header>` | Allows you to add a custom HTTP header to your request.                 |


## Examples :

### 1. View the source code of a webpage

This is the simplest use of curl. It will fetch the content from the URL and print its HTML source code directly to your terminal.
```bash
$ curl example.com
```
### 2. Download a file

The -O flag is used to download a file. curl will save it in your current directory using the same name as the remote file.

```bash
$ curl -O https://github.com/bobbyiliev/101-linux-commands/archive/refs/tags/v1.0.zip
```
### 3. Download a file and rename it

Using the -o flag, you can specify a new name for the downloaded file.
```bash
$ curl -o linux-commands.zip https://github.com/bobbyiliev/101-linux-commands/archive/refs/tags/v1.0.zip
```

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
