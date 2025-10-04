# The `wall` command

The `wall` command (short for *write all*) is used to send a message to all logged-in users on a Linux system. It is commonly used by system administrators to broadcast important information, such as planned maintenance or urgent announcements.

## Syntax

```bash
$wall [options] [message]
```

If a [message] is not provided on the command line, wall will read from standard input until it receives an end-of-file character (Ctrl+D).

## Options

| Option | Description |
|--------|-------------|
| -n     | Suppress the banner (which shows who sent the message) and only show the message text. |
| -t [seconds] | Set a timeout, in seconds. `wall` will try to write to a user's terminal for this duration before giving up. |

## Examples:

### 1. Broadcast a message to all users

This command sends a message directly to all logged-in users.

```bash
$ wall "The system will shut down in 10 minutes. Please save your work."
```
### Output (on other users' terminals):

```bash
Broadcast message from your_username@hostname (pts/0) (Sat Oct  4 19:50:00 2025):

The system will shut down in 10 minutes. Please save your work.
```

### 2. Broadcast a message from a text file

You can redirect the contents of a file to be used as the message.

### Contents of message.txt:

```bash
System maintenance will begin shortly.
Connections may be temporarily unstable.
```

### Command:
```bash
$ wall < message.txt
```

### 3. Send a multi-line message from standard input
If you run wall without a message, you can type a multi-line message directly in the terminal. Press Ctrl+D when you are finished to send it.

```bash
$ wall
The server is now back online.
All services are running normally.
<Ctrl+D>
```

### Output (on other users' terminals):
```bash
Broadcast message from your_username@hostname (pts/0) (Sat Oct  4 19:52:00 2025):

The server is now back online.
All services are running normally.
```
