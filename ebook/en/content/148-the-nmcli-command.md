# The `nmcli` command

The `nmcli` command is used for managing network connections by controlling the NetworkManager, a daemon that handles networking, through command line. 
The command stands for Network Manager Command Line Interface. 

### Installation:

The `nmcli` command is already installed by default on most Linux distros. To check if it is installed on your system type: 

```
nmcli --version
```
If you don't have nmcli installed you can do it by using the package manager:

Ubuntu or Debian:

```
sudo apt install network manager
```
This will install NetworkManageron in your system. 
Now we have to start the network managing service.

```
sudo systemctl start NetworkManager
```

Red Hat-based System(such as Fedora, CentOS, REHL):

```
sudo dnf install NetworkManager
```
This will install NetworkManager in your system.
Now we have to start the network managing service.

```
sudo systemctl start NetworkManager
```

Arch Linux:

```
sudo pacman -S networkmanager
```
This will install NetworkManager in your system.
Now we have to start the network managing service.

```
sudo systemctl start NetworkManager
```

### Examples:

1. List all available Wifi networks

```
nmcli device wifi list
```

2. View Network Status

```
nmcli device status
```

3. Connect to a Wifi Network

```
nmcli device wifi connect "SSID_NAME" password "YOUR_PASSWORD"
```

4. Disconnect from a Wifi Network

```
nmcli connection down "CONNECTION_NAME"
```

5. Turn Wifi On/Off

```
nmcli radio wifi on
nmcli radio wifi off
```
, respectively.

6. Turn Bluetooth On/Off

```
nmcli radio bluetooth on
nmcli radio bluetooth off
```
, respectively.

7. To show all connections

```
nmcli connection show
```

8. To show detailed info about specific connections

```
nmcli connection show "CONNECTION_NAME"
```

### Syntax: 

The general syntax for the nmcli command is as follows:

```
nmcli [OPTIONS...] { help | general | networking | radio | connection | device | agent | monitor } [COMMAND] [ARGUMENTS...]
```

### Additional Flags and their Functionalities:

#### Options

| **Short Flag** | **Long Flag**          | **Description**                                                                                                |
| :------------- | :--------------------- | :------------------------------------------------------------------------------------------------------------- |
| `-a`           | `--ask`                | nmcli will stop and ask for any missing required argument(do not use for non interactive options)              |
| `-c`           | `--color`{yes/no}      | It controls color output. yes enables colors, while no disables colors                                         |
| `-h`           | `--help`               | Prints help information                                                                                        |
| `-p`           | `--pretty`             | This causes nmcli to produce more user friendly output, eg with headers, and values are aligned                |
| `-v`           | `--version`            | Shows the nmcli version                                                                                        |
| `-f`           | `--fields`{field1,...} | This option is used to specify what fields should be printed. Valid fields names differ for specific commands. |
| `-g`           | `--get-value`{field1,.}| This option is used to print values from specific field.  It is a shortcut for --mode tabular --terse --fields |

#### General Commands

| **Command**                    |**Description**                                                       |
| :----------------------------- | :------------------------------------------------------------------- |
| `nmcli general status`         | Show overall NetworkManager status                                   |
| `nmcli general hostname`       | Display current hostname                                             |

#### Networking Commands

| **Command**                    | **Description**                                                      |
| :----------------------------- | :------------------------------------------------------------------- |
| `nmcli networking on`          | Enable all networking                                                |
| `nmcli networking off`         | Disable all networking                                               |
| `nmcli networking connectivity`| Check network connectivity status                                    |

#### Radio Commands

| **Command**                    | **Description**                                                      |
| :----------------------------- | :------------------------------------------------------------------- |
| `nmcli radio wifi on`          | Enable Wi-Fi radio                                                   |
| `nmcli radio wifi off`         | Disable Wi-Fi radio                                                  |
| `nmcli radio all`              | Show status of all radio switches                                    |
| `nmcli radio wifi`             | Show Wi-Fi radio status                                              |

#### Connection Management Commands

| **Command**                                      | **Description**                                    |
| :----------------------------------------------- | :------------------------------------------------- |
| `nmcli connection show`                          | List all saved connection profiles                 |
| `nmcli connection show --active`                 | List only active connections                       |
| `nmcli connection show "NAME"`                   | Show detailed info about specific connection       |
| `nmcli connection up "NAME"`                     | Activate a connection                              |
| `nmcli connection down "NAME"`                   | Deactivate a connection                            |
| `nmcli connection modify "NAME" [OPTIONS]`       | Modify connection settings                         |
| `nmcli connection delete "NAME"`                 | Delete a connection profile                        |
| `nmcli connection reload`                        | Reload all connection files from disk              |

#### Device Management Commands

| **Command**                                      | **Description**                                    |
| :----------------------------------------------- | :------------------------------------------------- |
| `nmcli device status`                            | Show status of all devices                         |
| `nmcli device show "DEVICE"`                     | Show detailed info for specific device             |
| `nmcli device disconnect "DEVICE"`               | Disconnect from a device                           |
| `nmcli device wifi list`                         | List all available Wi-Fi networks                  |
| `nmcli device wifi connect "SSID" password "PWD"`| Connect to password-protected Wi-Fi                |
