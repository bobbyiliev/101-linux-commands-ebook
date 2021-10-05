
  
# The `wget` command

The `who` command is used for downloading files from the Internet. It allows you to download several files at once, download in the background, resume downloads, limit the bandwidth, mirror a website, and much more.

### Examples

1. You can resume a download using the `-c` option

```
wget -c https://mirrors.piconets.webwerks.in/ubuntu-mirror/ubuntu-releases/20.04.3/ubuntu-20.04.3-desktop-amd64.iso
```

2. To download in the background, use the `-b` option

```
wget -b https://mirrors.piconets.webwerks.in/ubuntu-mirror/ubuntu-releases/20.04.3/ubuntu-20.04.3-desktop-amd64.iso
```

### Syntax:

```
wget [options] [url]
```

### Additional Flags and their Functionalities

|**Short Flag**    |**Description**   |
|--|--|
| `-v` |prints version of the wget available on your system  |
| `-h` |print help message displaying all the possible options  |
|`-b`|This option is used to send a process to the background as soon as it starts. |
|`-t`|This option is used to set number of retries to a specified number of times |
|`-c`|This option is used to resume a partially downloaded file |
