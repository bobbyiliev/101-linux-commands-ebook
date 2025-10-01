# The `wall` command

The `wall` command (short for *write all*) is used to send a message to all logged-in users on a Linux system. It is commonly used by system administrators to broadcast important information, such as planned maintenance or urgent announcements.

## Syntax

```
wall [options] [message]
```

If no message is provided as an argument, `wall` will read the message from standard input (stdin).

## Options

Some popular option flags include:

```
-n	Do not display the header (username and terminal of the sender).
-t [seconds]	Set a timeout for writing the message to each terminal.
```

## Few Examples:

1. Broadcast a message to all users

```
wall "The system will shut down in 10 minutes. Please save your work."
```

2. Broadcast a message from a text file

```
wall < message.txt
```

3. Send a message without showing the sender header

```
wall -n "Maintenance completed successfully."
```

Here I showed you how to use the `wall` command in Linux. It is a simple but effective tool for system-wide communication, especially useful when you need to notify multiple logged-in users at once.

For more details: [Wall (Unix) on Wikipedia](https://en.wikipedia.org/wiki/Wall_%28Unix%29)