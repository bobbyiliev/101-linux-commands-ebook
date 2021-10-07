# The `wget` command

The `wget` command is used for downloading files from the Internet. It supports downloading files using HTTP, HTTPS and FTP protocols. It allows you to download several files at once, download in the background, resume downloads, limit the bandwidth, mirror a website, and much more.

## Syntax

The `wget` syntax requires you to define the downloading options and the URL the to be downloaded file is coming from.

```bash
$ wget [options] [URL]
```

### Examples

In this example we will download the Ubuntu 20.04 desktop iso file from different sources. Go over to your terminal or open a new one and type in the below `wget`. This will stat the download. The download may take a few minutes to complete.

1. Starting a regular download

```bash
wget https://releases.ubuntu.com/20.04/ubuntu-20.04.3-desktop-amd64.iso
```

2. You can resume a download using the `-c` option

```bash
wget -c https://mirrors.piconets.webwerks.in/ubuntu-mirror/ubuntu-releases/20.04.3/ubuntu-20.04.3-desktop-amd64.iso
```

3. To download in the background, use the `-b` option

```bash
wget -b https://mirrors.piconets.webwerks.in/ubuntu-mirror/ubuntu-releases/20.04.3/ubuntu-20.04.3-desktop-amd64.iso
```

## More options

On top of downloading, `wget` provides many more features, such as downloading multiple files, dowloading in the background, limiting download bandwith and resuming stopped downloads. View all `wget` options in its man page.

```bash
man wget
```

### Additional Flags and their Functionalities

| **Short Flag** | **Description**                                                               |
| -------------- | ----------------------------------------------------------------------------- |
| `-v`           | prints version of the wget available on your system                           |
| `-h`           | print help message displaying all the possible options                        |
| `-b`           | This option is used to send a process to the background as soon as it starts. |
| `-t`           | This option is used to set number of retries to a specified number of times   |
| `-c`           | This option is used to resume a partially downloaded file                     |
