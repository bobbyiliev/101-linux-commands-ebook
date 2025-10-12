# The `su` command

The `su` (substitute user) command allows you to run commands as another user account. It's commonly used to switch to the root account for administrative tasks or to run commands as a different user without logging out and logging back in.

## Syntax

```bash
su [OPTIONS] [-] [USER [ARGUMENT...]]
```

## Key Features

- **User Switching**: Switch to any user account on the system
- **Environment Control**: Choose whether to inherit or reset environment variables
- **Shell Selection**: Specify which shell to use
- **Group Management**: Switch primary and supplementary groups
- **Command Execution**: Run specific commands as another user

## Basic Usage

### Switching to Root

```bash
# Switch to root user (requires root password)
su

# Switch to root with login shell (recommended)
su -

# Alternative syntax for login shell
su -l
su --login
```

### Switching to Specific User

```bash
# Switch to specific user
su username

# Switch to user with login shell
su - username
su -l username

# Switch to user and run specific command
su - username -c "whoami"
```

## Environment Handling

### Login Shell vs Non-Login Shell

```bash
# Non-login shell (keeps current environment)
su username
# Current directory and environment variables are preserved

# Login shell (starts fresh environment)
su - username
# Changes to user's home directory and loads their profile
```

### Environment Variable Control

```bash
# Preserve current environment
su -m username
su --preserve-environment username

# Preserve specific environment variables
su -w HOME,TERM username
su --whitelist-environment=HOME,TERM username

# Reset environment but preserve specific variables
su - username --preserve-environment=PATH
```

## Advanced Usage

### Group Management

```bash
# Switch user and primary group
su -g developers username

# Switch with supplementary groups
su -G developers,admins username

# Check current groups
su - username -c "groups"
```

### Shell Selection

```bash
# Use specific shell
su -s /bin/bash username
su --shell=/bin/zsh username

# Use shell if allowed by /etc/shells
su -s /usr/bin/fish username

# Check available shells
cat /etc/shells
```

### Command Execution

```bash
# Run single command as another user
su - username -c "ls -la /home/username"

# Run multiple commands
su - username -c "cd /tmp && ls -la && pwd"

# Run script as another user
su - username -c "/path/to/script.sh"

# Run command with arguments
su - username -c "grep 'pattern' /var/log/syslog"
```

## Practical Examples

### System Administration

```bash
# Switch to root for administrative tasks
su -
# Now you can run administrative commands

# Run single administrative command
su -c "systemctl restart apache2"

# Edit system configuration file
su -c "nano /etc/hosts"

# Check system logs
su -c "tail -f /var/log/syslog"
```

### Development Workflows

```bash
# Switch to application user for deployment
su - appuser -c "cd /opt/myapp && ./deploy.sh"

# Run application as specific user
su - www-data -c "/usr/bin/php /var/www/html/script.php"

# Test permissions as different user
su - testuser -c "ls -la /shared/directory"
```

### User Management Tasks

```bash
# Create file as specific user
su - username -c "touch /home/username/newfile.txt"

# Check user's environment
su - username -c "env | sort"

# Run user's shell configuration
su - username -c "source ~/.bashrc && echo \$PATH"
```

## Security Considerations

### Password Requirements

```bash
# su requires the target user's password
su username  # Requires username's password

# Root can switch to any user without password
sudo su - username  # Uses sudo authentication

# Check who can use su
grep su /etc/group
```

### Audit and Logging

```bash
# Check su usage in logs
sudo grep su /var/log/auth.log

# Monitor current su sessions
w
who

# Check login history
last
```

### Safe Usage Patterns

```bash
# Always use login shell for administrative tasks
su -  # Better than just 'su'

# Use sudo instead of su when possible
sudo command  # Better than 'su -c command'

# Limit time as root
su -c "command1 && command2 && exit"
```

## Comparison with Sudo

### When to Use `su`

```bash
# Multiple administrative commands
su -
# Run several commands as root
exit

# Interactive root session
su -
# Work as root for extended period
```

### When to Use `sudo`

```bash
# Single command execution
sudo systemctl restart service

# Better security and logging
sudo -u username command

# Temporary privilege escalation
sudo apt update && sudo apt upgrade
```

## Configuration and Customization

### PAM Configuration

```bash
# Check PAM configuration for su
cat /etc/pam.d/su

# Restrict su to wheel group (some distributions)
# Edit /etc/pam.d/su and uncomment:
# auth required pam_wheel.so use_uid
```

### Shell Configuration

```bash
# Check if shell is allowed
grep username /etc/passwd
cat /etc/shells

# Set shell for user
sudo chsh -s /bin/bash username
```

### Environment Customization

```bash
# Customize login environment
# Edit ~/.profile, ~/.bashrc, or ~/.bash_profile

# Set specific environment for su sessions
# Create ~/.surc or modify shell configuration
```

## Troubleshooting

### Common Issues

```bash
# Authentication failure
su: Authentication failure
# Check password, user existence, account status

# Permission denied
su: Permission denied
# Check PAM configuration, wheel group membership

# Shell not allowed
su: Warning: shell not allowed
# Add shell to /etc/shells or use -s option
```

### Debugging

```bash
# Check user account status
sudo passwd -S username

# Verify user existence
id username
grep username /etc/passwd

# Check group membership
groups username

# Test with verbose output
su -v username
```

## Script Integration

### Using su in Scripts

```bash
#!/bin/bash
# Script to run commands as different user

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Switch to app user and run commands
su - appuser -c "
    cd /opt/myapp
    ./backup.sh
    ./cleanup.sh
"
```

### Automated Tasks

```bash
# Cron job running as specific user
# Add to root's crontab:
# 0 2 * * * su - backupuser -c '/usr/local/bin/backup.sh'

# System service running as user
su - serviceuser -c '/opt/service/start.sh' &
```

## Options Reference

|**Option**|**Long Form**|**Description**|
|:---|:---|:---|
|`-`|`--login`|Start login shell, load user's environment|
|`-c CMD`|`--command=CMD`|Execute command and exit|
|`-f`|`--fast`|Pass -f to shell (for csh/tcsh)|
|`-g GRP`|`--group=GRP`|Specify primary group|
|`-G GRP`|`--supp-group=GRP`|Specify supplementary group|
|`-l`|`--login`|Same as `-` option|
|`-m`|`--preserve-environment`|Don't reset environment variables|
|`-p`|`--preserve-environment`|Same as `-m` option|
|`-s SHL`|`--shell=SHL`|Use specified shell|
|`-w VAR`|`--whitelist-environment=VAR`|Don't reset specified variables|
|`--help`|-|Display help message|
|`--version`|-|Display version information|

## Best Practices

### Security Best Practices

- Use `sudo` instead of `su` when possible for better logging
- Always use login shell (`su -`) for administrative tasks
- Limit time spent as root user
- Use specific commands rather than interactive sessions when possible
- Regularly audit su usage through system logs

### Operational Best Practices

- Use descriptive comments when switching users in scripts
- Verify user existence before attempting to switch
- Handle authentication failures gracefully in scripts
- Document user switching requirements in system documentation

## Important Notes

- `su` requires the target user's password (unless run as root)
- Using `su -` is recommended for administrative tasks as it provides a clean environment
- `su` sessions are logged in `/var/log/auth.log` or similar system logs
- The `wheel` group restriction may be enabled on some systems
- Always exit su sessions when finished to return to original user

The `su` command is essential for user switching and privilege management in Linux systems, but should be used carefully with proper security considerations.

For more details, check the manual: `man su`
