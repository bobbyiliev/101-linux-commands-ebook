# The `screen` command

`screen` - With screen you can start a screen session and then open any number of windows (virtual terminals) inside that session. 
Processes running in Screen will continue to run when their window is not visible even if you get disconnected.  This is very
handy for running long during session such as bash scripts that run very long.

To start a screen session you type `screen`, this will open a new screen session with a virtual terminal open.

Below are some most common commands for managing Linux Screen Windows:

|**Command**   |**Description**   |
|:---|:---|
|`Ctrl+a`+ `c`|Create a new window (with shell).|
|`Ctrl+a`+ `"`|List all windows.
|`Ctrl+a`+ `0`|Switch to window 0 (by number).
|`Ctrl+a`+ `A`|Rename the current window.
|`Ctrl+a`+ `S`|Split current region horizontally into two regions.
|`Ctrl+a`+ `'`|Split current region vertically into two regions.
|`Ctrl+a`+ `tab`|Switch the input focus to the next region.
|`Ctrl+a`+ `Ctrl+a`|Toggle between the current and previous windows
|`Ctrl+a`+ `Q`|Close all regions but the current one.
|`Ctrl+a`+ `X`|Close the current region.


## Restore a Linux Screen

To restore to a screen session you type `screen -r`, if you have more than one open screen session you have to add the 
session id to the command to connect to the right session.

## Listing all open screen sessions

To find the session ID you can list the current running screen sessions with:

`screen -ls`

There are screens on:
```
18787.pts-0.your-server   (Detached)
15454.pts-0.your-server   (Detached)
2 Sockets in /run/screens/S-yourserver.
``` 

If you want to restore screen 18787.pts-0, then type the following command:

`screen -r 18787`
