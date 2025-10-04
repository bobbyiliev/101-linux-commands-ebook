# The `Wait` commands

The wait command is a shell builtin that pauses script execution until a specific background process, or all running child processes, have finished.

Its primary purpose is to synchronize tasks, ensuring that a script doesn't continue to the next step until prerequisite background jobs are complete. A background process is a command that is run with an ampersand (&) at the end, which tells the shell to run it without waiting for it to finish.

## Syntax

```bash
$ wait [PID]
```
[PID] - An optional Process ID to wait for. If no PID is given, wait will wait for all active child processes to complete.

## Examples

### 1. Waiting for a Specific Process
This example shows how to launch a single background process and wait for it specifically.

### Script:
```bash
#!/bin/bash
echo "This process will run in the background..." &
process_id=$!

echo "Script is now waiting for process ID: $process_id"
wait $process_id
echo "Process $process_id has finished."
echo "The script exited with status: $?"
```
### Explanation:

* &: The ampersand runs the echo command in the background, allowing the script to immediately continue to the next line.

* $!: This is a special shell variable that holds the Process ID (PID) of the most recently executed background command. We save it to the process_id variable.

* wait $process_id: This is the key command. The script pauses here until the process with that specific ID is complete.

* $?: This variable holds the exit status of the last command that finished. An exit status of 0 means success.


### Output:

```bash
$ bash wait_example.sh
Script is now waiting for process ID: 12345
This process will run in the background...
Process 12345 has finished.
The script exited with status: 0
```

### 2. Waiting for All Background Processes
This is the most common use case. Here, we launch several background tasks and then use a single wait command to pause until all of them are done.

### Script:
```bash
#!/bin/bash

echo "Starting multiple background jobs..."
sleep 3 &
sleep 1 &
sleep 2 &

echo "Waiting for all sleep commands to finish."
wait
echo "All jobs are done. Continuing with the rest of the script."
```

### Output:

```bash
$ bash wait_all_example.sh
Starting multiple background jobs...
Waiting for all sleep commands to finish.
(after about 3 seconds)
All jobs are done. Continuing with the rest of the script.
```