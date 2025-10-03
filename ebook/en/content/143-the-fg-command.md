# The `fg` command

The `fg` command is used to bring background or stopped jobs to the foreground, making them the active process in your terminal. It's an essential part of job control in Unix-like shells.

## Syntax

```
fg [job_spec]
```

If no job specification is provided, `fg` operates on the current job (most recent job).

## Job Specifications

You can refer to jobs using different formats:
- `%1` - Job number 1
- `%+` or `%%` - Current job (most recent)
- `%-` - Previous job
- `%string` - Job whose command line starts with string
- `%?string` - Job whose command line contains string

## Examples

1. Bring the current job to foreground

```bash
fg
```

2. Bring specific job to foreground

```bash
fg %1
```

3. Bring job by partial command name

```bash
fg %vim
```

4. Bring job containing specific text

```bash
fg %?backup
```

## Complete Job Control Workflow

Here's a typical workflow demonstrating `fg` usage:

1. Start a background job

```bash
ping google.com > /tmp/ping.txt &
```

2. Start another job and stop it

```bash
vim myfile.txt
# Press Ctrl+Z to stop
```

3. Check current jobs

```bash
jobs
```
Output:
```
[1]-  Running    ping google.com > /tmp/ping.txt &
[2]+  Stopped    vim myfile.txt
```

4. Bring vim to foreground

```bash
fg %2
```

5. Work in vim, then stop again (Ctrl+Z) and bring ping to foreground

```bash
fg %1
```

## Practical Examples

1. Working with editors

```bash
# Start editing
nano config.txt
# Stop with Ctrl+Z
# Do other work
ls -la
# Return to editor
fg
```

2. Managing multiple development tasks

```bash
# Start compilation in background
make all > build.log 2>&1 &

# Start editing source code
vim main.c
# Stop editor (Ctrl+Z)

# Check build progress
fg %make
# Stop build monitoring (Ctrl+Z)

# Return to editing
fg %vim
```

3. Interactive debugging session

```bash
# Start debugger
gdb ./myprogram
# Stop debugger (Ctrl+Z)

# Check core dumps or logs
ls -la core.*

# Return to debugger
fg %gdb
```

4. Working with multiple terminals/sessions

```bash
# Start SSH session
ssh user@remote-server
# Stop SSH (Ctrl+Z)

# Do local work
ps aux | grep myprocess

# Return to SSH session
fg %ssh
```

## Advanced Usage

1. Switching between multiple stopped jobs

```bash
# Start several editors
vim file1.txt
# Ctrl+Z
vim file2.txt
# Ctrl+Z
nano file3.txt
# Ctrl+Z

# Check all jobs
jobs

# Switch between them
fg %1    # vim file1.txt
# Ctrl+Z
fg %2    # vim file2.txt
# Ctrl+Z
fg %3    # nano file3.txt
```

2. Using with job control in scripts

```bash
#!/bin/bash
# Start background monitoring
tail -f /var/log/syslog &
MONITOR_PID=$!

# Do main work
./main_script.sh

# Bring monitor to foreground for review
fg %tail

# Or kill it
kill $MONITOR_PID
```

## Related Commands

- `bg` - Put job in background
- `jobs` - List active jobs
- `kill` - Terminate job
- `Ctrl+Z` - Stop (suspend) current job
- `Ctrl+C` - Terminate current job

## Use Cases

- **Code editing**: Switch between multiple open editors
- **Development**: Alternate between compilation and editing
- **System monitoring**: Switch between monitoring tools
- **Remote sessions**: Resume SSH or other remote connections
- **Interactive programs**: Return to paused interactive applications
- **Debugging**: Resume debugger sessions

## Important Notes

- When a job is brought to foreground, it becomes the active process
- You can only have one foreground job at a time
- Foreground jobs can receive keyboard input
- Use Ctrl+Z to stop (suspend) a foreground job
- Use Ctrl+C to terminate a foreground job
- Background jobs continue running even when not in foreground

## Error Handling

Common issues with `fg`:
- Job doesn't exist: `fg: %3: no such job`
- No jobs available: `fg: no current job`
- Job already in foreground

## Tips for Effective Usage

1. **Use job numbers**: More reliable than partial names
2. **Check jobs first**: Always run `jobs` to see current status
3. **Consistent workflow**: Develop a routine for job switching
4. **Redirect output**: Background jobs should redirect output to avoid interference

```bash
# Good practice
tail -f /var/log/messages > monitor.out 2>&1 &
vim script.sh
# Ctrl+Z
fg %tail  # Review logs
# Ctrl+Z
fg %vim   # Continue editing
```

## Integration with Other Tools

`fg` works well with:
- **Terminal multiplexers**: `screen`, `tmux`
- **Development environments**: IDEs, editors
- **System monitoring**: `top`, `htop`, `tail`
- **Network tools**: `ssh`, `ping`, `netstat`

The `fg` command is crucial for efficient terminal multitasking and provides seamless switching between different tasks.

For more details, check the manual: `help fg`
