# The `tty` command

The `tty` command prints the filename of the terminal connected to standard input. It shows which terminal device you're currently using and can determine if the input is coming from a terminal or being redirected from a file or pipe.

## Syntax

```
tty [options]
```

## Key Features

- **Terminal Identification**: Shows current terminal device
- **Redirection Detection**: Determines if input is from terminal or file
- **Session Information**: Helps identify terminal sessions
- **Scripting Support**: Exit codes indicate terminal vs non-terminal

## Basic Usage

### Show Current Terminal

```bash
# Display current terminal device
tty

# Example outputs:
# /dev/pts/0    (pseudo-terminal)
# /dev/tty1     (console terminal)
# /dev/ttys000  (macOS terminal)
```

### Check If Terminal

```bash
# Silent mode - just check if it's a terminal
tty -s

# Check exit code
tty -s && echo "Running in terminal" || echo "Not in terminal"

# Example usage in scripts
if tty -s; then
    echo "Interactive mode"
else
    echo "Non-interactive mode"
fi
```

## Common Options

### Basic Options

```bash
# -s: Silent mode (no output, just exit code)
tty -s

# --help: Show help information
tty --help

# --version: Show version information
tty --version
```

## Understanding Terminal Types

### 1. Physical Terminals

```bash
# Console terminals (virtual consoles)
# /dev/tty1, /dev/tty2, /dev/tty3, etc.

# Switch to virtual console and check
# Ctrl+Alt+F1 (then login)
tty
# Output: /dev/tty1
```

### 2. Pseudo Terminals

```bash
# Most common in desktop environments
# /dev/pts/0, /dev/pts/1, /dev/pts/2, etc.

# In terminal emulator
tty
# Output: /dev/pts/0

# Each new terminal window gets new pts number
```

### 3. Serial Terminals

```bash
# Serial console connections
# /dev/ttyS0, /dev/ttyS1, etc.

# USB serial devices
# /dev/ttyUSB0, /dev/ttyUSB1, etc.
```

## Practical Examples

### 1. Session Identification

```bash
# Identify current session
echo "Current session: $(tty)"

# Show user and terminal
echo "User: $(whoami) on $(tty)"

# Show all users and their terminals
who

# Show current user's terminals
who | grep $(whoami)
```

### 2. Multi-Terminal Scripts

```bash
#!/bin/bash
# Script that behaves differently based on terminal

current_tty=$(tty)
echo "Running on: $current_tty"

case "$current_tty" in
    /dev/tty[1-6])
        echo "Running on virtual console"
        # Console-specific behavior
        ;;
    /dev/pts/*)
        echo "Running in terminal emulator"
        # Terminal emulator behavior
        ;;
    *)
        echo "Unknown terminal type"
        ;;
esac
```

### 3. Interactive vs Non-Interactive Detection

```bash
#!/bin/bash
# Detect if script is running interactively

if tty -s; then
    echo "Interactive mode - can prompt user"
    read -p "Enter your name: " name
    echo "Hello, $name!"
else
    echo "Non-interactive mode - using defaults"
    name="User"
    echo "Hello, $name!"
fi
```

### 4. Terminal-Specific Configuration

```bash
#!/bin/bash
# Configure based on terminal capabilities

current_tty=$(tty)

if [[ "$current_tty" =~ ^/dev/pts/ ]]; then
    # Modern terminal emulator
    echo -e "\e[32mGreen text\e[0m"
    echo -e "\e[1mBold text\e[0m"
elif [[ "$current_tty" =~ ^/dev/tty[1-6]$ ]]; then
    # Virtual console - limited capabilities
    echo "Plain text output"
else
    echo "Unknown terminal - safe output"
fi
```

## Scripting Applications

### 1. Conditional User Interaction

```bash
#!/bin/bash
# Only prompt if running in terminal

ask_confirmation() {
    local message="$1"

    if tty -s; then
        read -p "$message (y/n): " response
        case "$response" in
            [Yy]|[Yy][Ee][Ss]) return 0 ;;
            *) return 1 ;;
        esac
    else
        # Non-interactive - assume yes
        echo "$message: Assumed yes (non-interactive)"
        return 0
    fi
}

# Usage
if ask_confirmation "Delete old files?"; then
    echo "Deleting files..."
else
    echo "Keeping files..."
fi
```

### 2. Progress Indicators

```bash
#!/bin/bash
# Show progress only in terminal

show_progress() {
    if tty -s; then
        echo -n "Processing: "
        for i in {1..10}; do
            echo -n "."
            sleep 0.5
        done
        echo " Done!"
    else
        echo "Processing... Done!"
    fi
}

show_progress
```

### 3. Logging Behavior

```bash
#!/bin/bash
# Different logging based on terminal

log_message() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    if tty -s; then
        # Terminal output - colored
        case "$level" in
            INFO)  echo -e "\e[32m[$timestamp] INFO: $message\e[0m" ;;
            WARN)  echo -e "\e[33m[$timestamp] WARN: $message\e[0m" ;;
            ERROR) echo -e "\e[31m[$timestamp] ERROR: $message\e[0m" ;;
        esac
    else
        # Non-terminal output - plain
        echo "[$timestamp] $level: $message"
    fi
}

# Usage
log_message "INFO" "Script started"
log_message "WARN" "Low disk space"
log_message "ERROR" "Connection failed"
```

## Terminal Session Management

### 1. Session Information

```bash
# Get detailed session info
get_session_info() {
    echo "=== Session Information ==="
    echo "Terminal: $(tty)"
    echo "User: $(whoami)"
    echo "Shell: $SHELL"
    echo "PID: $$"
    echo "PPID: $PPID"
    echo "Session ID: $(ps -o sid= -p $$)"
    echo "Process Group: $(ps -o pgid= -p $$)"
}

get_session_info
```

### 2. Multiple Terminal Detection

```bash
# Count user's active terminals
count_user_terminals() {
    local user=$(whoami)
    local count=$(who | grep "^$user " | wc -l)
    echo "User $user has $count active terminals"

    echo "Active sessions:"
    who | grep "^$user " | while read line; do
        echo "  $line"
    done
}

count_user_terminals
```

### 3. Terminal Communication

```bash
# Send message to specific terminal
send_to_terminal() {
    local target_tty="$1"
    local message="$2"

    if [ -w "$target_tty" ]; then
        echo "Message from $(tty): $message" > "$target_tty"
        echo "Message sent to $target_tty"
    else
        echo "Cannot write to $target_tty"
    fi
}

# Usage (if permissions allow)
# send_to_terminal "/dev/pts/1" "Hello from another terminal!"
```

## Integration with Other Commands

### 1. Combining with ps

```bash
# Find processes in current terminal
current_tty=$(tty | sed 's|/dev/||')
ps -t "$current_tty"

# Show process tree for current terminal
pstree -p $(ps -t "$current_tty" -o pid --no-headers | head -1)
```

### 2. Combining with who/w

```bash
# Show who is on the same terminal type
current_tty_type=$(tty | cut -d'/' -f3 | sed 's/[0-9]*$//')
who | grep "$current_tty_type"

# Detailed information about current session
w | grep "$(tty | sed 's|/dev/||')"
```

### 3. System Monitoring

```bash
# Monitor terminal activity
monitor_terminals() {
    echo "Active terminals:"
    ls -la /dev/pts/
    echo

    echo "Users and terminals:"
    who
    echo

    echo "Current session:"
    echo "  TTY: $(tty)"
    echo "  Uptime: $(uptime)"
}

monitor_terminals
```

## Security and Permissions

### 1. Terminal Permissions

```bash
# Check terminal permissions
check_tty_permissions() {
    local current_tty=$(tty)
    echo "Terminal: $current_tty"
    ls -la "$current_tty"

    # Check if others can write to terminal
    if [ -w "$current_tty" ]; then
        echo "Terminal is writable"
    else
        echo "Terminal is not writable"
    fi
}

check_tty_permissions
```

### 2. Secure Terminal Check

```bash
# Verify secure terminal environment
check_secure_terminal() {
    if ! tty -s; then
        echo "WARNING: Not running in a terminal"
        return 1
    fi

    local current_tty=$(tty)
    local tty_perms=$(ls -la "$current_tty" | cut -d' ' -f1)

    if [[ "$tty_perms" =~ .*w.*w.* ]]; then
        echo "WARNING: Terminal is world-writable"
        return 1
    fi

    echo "Terminal security check passed"
    return 0
}

check_secure_terminal
```

## Debugging and Troubleshooting

### 1. Terminal Issues

```bash
# Debug terminal problems
debug_terminal() {
    echo "=== Terminal Debug Information ==="
    echo "TTY: $(tty 2>/dev/null || echo "No TTY")"
    echo "TERM: $TERM"
    echo "Interactive: $(tty -s && echo "Yes" || echo "No")"
    echo "Standard input: $(file /proc/self/fd/0 | cut -d: -f2-)"
    echo "Standard output: $(file /proc/self/fd/1 | cut -d: -f2-)"
    echo "Standard error: $(file /proc/self/fd/2 | cut -d: -f2-)"
}

debug_terminal
```

### 2. Redirection Detection

```bash
# Detect various input/output scenarios
detect_io_redirection() {
    echo "Input/Output Analysis:"

    if tty -s; then
        echo "  Standard input: Terminal ($(tty))"
    else
        echo "  Standard input: Redirected/Pipe"
    fi

    if [ -t 1 ]; then
        echo "  Standard output: Terminal"
    else
        echo "  Standard output: Redirected/Pipe"
    fi

    if [ -t 2 ]; then
        echo "  Standard error: Terminal"
    else
        echo "  Standard error: Redirected/Pipe"
    fi
}

detect_io_redirection
```

### 3. Session Recovery

```bash
# Help recover lost terminal sessions
find_my_sessions() {
    local user=$(whoami)
    echo "Finding sessions for user: $user"

    echo "Current TTY: $(tty)"
    echo

    echo "All active sessions:"
    who | grep "^$user "
    echo

    echo "Screen sessions:"
    screen -ls 2>/dev/null || echo "No screen sessions"
    echo

    echo "Tmux sessions:"
    tmux list-sessions 2>/dev/null || echo "No tmux sessions"
}

find_my_sessions
```

## Advanced Usage

### 1. Terminal Multiplexing Integration

```bash
# Detect if running inside multiplexer
detect_multiplexer() {
    if [ -n "$TMUX" ]; then
        echo "Running inside tmux"
        echo "  Session: $(tmux display-message -p '#S')"
        echo "  Window: $(tmux display-message -p '#W')"
        echo "  Pane: $(tmux display-message -p '#P')"
    elif [ -n "$STY" ]; then
        echo "Running inside screen"
        echo "  Session: $STY"
    else
        echo "Not in a multiplexer"
    fi

    echo "TTY: $(tty)"
}

detect_multiplexer
```

### 2. Remote Session Detection

```bash
# Detect remote vs local sessions
detect_session_type() {
    local current_tty=$(tty)

    if [ -n "$SSH_CONNECTION" ]; then
        echo "Remote SSH session"
        echo "  From: $(echo $SSH_CONNECTION | cut -d' ' -f1,2)"
        echo "  To: $(echo $SSH_CONNECTION | cut -d' ' -f3,4)"
    elif [[ "$current_tty" =~ ^/dev/tty[1-6]$ ]]; then
        echo "Local console session"
    elif [[ "$current_tty" =~ ^/dev/pts/ ]]; then
        echo "Local terminal emulator"
    else
        echo "Unknown session type"
    fi

    echo "TTY: $current_tty"
}

detect_session_type
```

## Best Practices

### 1. Safe Scripting

```bash
# Always check for terminal before interactive operations
safe_interactive() {
    if ! tty -s; then
        echo "Error: This script requires a terminal" >&2
        exit 1
    fi

    # Proceed with interactive operations
    read -p "Continue? (y/n): " response
}
```

### 2. Cross-Platform Compatibility

```bash
# Handle different systems
get_terminal_info() {
    if command -v tty >/dev/null 2>&1; then
        local terminal=$(tty 2>/dev/null)
        if [ $? -eq 0 ]; then
            echo "$terminal"
        else
            echo "not a tty"
        fi
    else
        echo "tty command not available"
    fi
}
```

### 3. Error Handling

```bash
# Robust terminal checking
check_terminal_safe() {
    local tty_output
    tty_output=$(tty 2>/dev/null)
    local exit_code=$?

    if [ $exit_code -eq 0 ]; then
        echo "Terminal: $tty_output"
        return 0
    else
        echo "Not a terminal (exit code: $exit_code)"
        return 1
    fi
}
```

## Important Notes

- **Exit Codes**: tty returns 0 if stdin is a terminal, non-zero otherwise
- **Silent Mode**: Use `-s` for scripts that only need to check terminal status
- **Redirection**: Output changes when stdin is redirected from files or pipes
- **Security**: Be aware of terminal permissions and write access
- **Portability**: Available on most Unix-like systems
- **Session Management**: Useful for multiplexing and session tracking

The `tty` command is essential for scripts that need to detect terminal environments and behave appropriately in interactive vs non-interactive contexts.

For more details, check the manual: `man tty`
