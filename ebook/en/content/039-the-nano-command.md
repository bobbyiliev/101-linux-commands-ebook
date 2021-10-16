# The `nano` command

The `nano` command lets you create/edit text files.

### Installation:

Nano text editor is pre-installed on macOS and most Linux distros. It's an alternative to `vi` and `vim`. To check if it is installed on your system type:

```
nano --version
```
If you don't have `nano` installed you can do it by using the package manager:

Ubuntu or Debian:

```
sudo apt install nano
```

### Examples:

1. Open an existing file, type `nano` followed by the path to the file:

```
nano /path/to/filename
```

2. Create a new file, type `nano` followed by the filename:

```
nano filename
```

3. Open a file with the cursor on a specific line and character use the following syntax: 

```
nano +line_number,character_number filename
```

### Overview of some Shortcuts and their Functionalities:

|**Shortcut**  |**Description**   |
|:---|:---|
|`Ctrl + S`|Save current file|
|`Ctrl + O`|Offer to write file ("Save as")|
|`Ctrl + X`|Close buffer, exit from nano|
|`Ctrl + K`|Cut current line into cutbuffer|
|`Ctrl + U`|Paste contents of cutbuffer|
|`Alt + 6`|Copy current line into cutbuffer|
|`Alt + U`|Undo last action|
|`Alt + E`|	Redo last undone action|
