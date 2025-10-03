# The `journalctl` command

The `journalctl` command is used to view and query the systemd journal, which collects and stores system logs in a structured, indexed format. It's the primary tool for viewing system logs in modern Linux distributions.

## Syntax

```
journalctl [options] [matches]
```

## Options

Some popular option flags include:

```
-f          Follow journal (like tail -f)
-u [unit]   Show logs for specific unit/service
-p [level]  Filter by priority level (0-7)
-S [time]   Show entries since specified time
-U [time]   Show entries until specified time
-b          Show logs from current boot
-k          Show kernel messages only
-r          Reverse output (newest first)
-n [lines]  Show last N lines
--no-pager  Don't pipe output to pager
-x          Add explanatory help texts
-o [format] Output format (json, short, verbose, etc.)
--disk-usage Show current disk usage
--vacuum-size=[size] Remove logs to reduce size
--vacuum-time=[time] Remove logs older than time
```

## Priority Levels

```
0  Emergency (emerg)
1  Alert (alert)
2  Critical (crit)
3  Error (err)
4  Warning (warning)
5  Notice (notice)
6  Informational (info)
7  Debug (debug)
```

## Examples

1. View all journal entries

```bash
journalctl
```

2. Follow live journal entries

```bash
journalctl -f
```

3. Show logs for a specific service

```bash
journalctl -u nginx
```

4. Show logs since last boot

```bash
journalctl -b
```

5. Show logs from previous boot

```bash
journalctl -b -1
```

6. Show kernel messages

```bash
journalctl -k
```

7. Show logs from specific time

```bash
journalctl --since "2024-01-01 00:00:00"
```

8. Show logs from last hour

```bash
journalctl --since "1 hour ago"
```

9. Show logs between time periods

```bash
journalctl --since "2024-01-01" --until "2024-01-02"
```

10. Show only error and critical messages

```bash
journalctl -p err
```

11. Show last 50 lines

```bash
journalctl -n 50
```

12. Follow logs for specific service

```bash
journalctl -u ssh -f
```

13. Show logs in JSON format

```bash
journalctl -o json
```

14. Show disk usage

```bash
journalctl --disk-usage
```

15. Remove old logs to free space

```bash
journalctl --vacuum-size=100M
```

16. Remove logs older than 2 weeks

```bash
journalctl --vacuum-time=2weeks
```

17. Show logs with explanations

```bash
journalctl -x
```

18. Show logs for specific process ID

```bash
journalctl _PID=1234
```

19. Show logs for specific user

```bash
journalctl _UID=1000
```

20. Show reverse chronological order

```bash
journalctl -r
```

## Time Specifications

You can use various time formats:
- `"2024-01-01 12:00:00"`
- `"yesterday"`
- `"today"`
- `"1 hour ago"`
- `"30 minutes ago"`
- `"2 days ago"`

## Output Formats

```
short      Default format
verbose    All available fields
json       JSON format
json-pretty Pretty-printed JSON
export     Binary export format
cat        Very short format
```

## Use Cases

- Troubleshooting system issues
- Monitoring service behavior
- Security auditing
- Performance analysis
- Debugging system problems
- Tracking user activities

## Important Notes

- Journal files are stored in `/var/log/journal/` or `/run/log/journal/`
- Requires appropriate permissions to view system logs
- Can consume significant disk space over time
- Use vacuum options to manage log size
- Persistent logging requires proper configuration

The `journalctl` command is essential for system administration and troubleshooting in systemd-based Linux distributions.

For more details, check the manual: `man journalctl`
