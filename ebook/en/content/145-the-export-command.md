# The `export` command

The `export` command is used to set environment variables that will be available to child processes. It makes variables available to all processes started from the current shell session.

## Syntax

```
export [options] [variable[=value]]
export [options] [name[=value] ...]
```

## How Environment Variables Work

- **Local variables**: Only available in the current shell
- **Environment variables**: Available to current shell and all child processes
- `export` converts local variables to environment variables

## Options

Some popular option flags include:

```
-f    Export functions instead of variables
-n    Remove variable from environment (unexport)
-p    Display all exported variables
```

## Examples

1. Export a simple variable

```bash
export MY_VAR="Hello World"
```

2. Export multiple variables at once

```bash
export VAR1="value1" VAR2="value2" VAR3="value3"
```

3. Export an existing local variable

```bash
LOCAL_VAR="test"
export LOCAL_VAR
```

4. Show all exported variables

```bash
export -p
```

5. Export PATH modifications

```bash
export PATH="$PATH:/usr/local/bin"
```

6. Export with command substitution

```bash
export CURRENT_DATE=$(date)
export HOSTNAME=$(hostname)
```

7. Unexport a variable (remove from environment)

```bash
export -n MY_VAR
```

8. Export function

```bash
my_function() {
    echo "Hello from function"
}
export -f my_function
```

## Common Environment Variables

1. **PATH** - Executable search paths

```bash
export PATH="/usr/local/bin:$PATH"
```

2. **HOME** - User's home directory

```bash
export HOME="/home/username"
```

3. **EDITOR** - Default text editor

```bash
export EDITOR="vim"
export VISUAL="code"
```

4. **LANG** - System language and locale

```bash
export LANG="en_US.UTF-8"
```

5. **PS1** - Primary prompt string

```bash
export PS1="\u@\h:\w\$ "
```

6. **JAVA_HOME** - Java installation directory

```bash
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk"
```

7. **NODE_ENV** - Node.js environment

```bash
export NODE_ENV="production"
```

## Development Environment Examples

1. **Python development**

```bash
export PYTHONPATH="$PYTHONPATH:/path/to/modules"
export VIRTUAL_ENV="/path/to/venv"
```

2. **Node.js development**

```bash
export NODE_PATH="/usr/local/lib/node_modules"
export NPM_CONFIG_PREFIX="$HOME/.npm-global"
```

3. **Go development**

```bash
export GOPATH="$HOME/go"
export GOROOT="/usr/local/go"
export PATH="$PATH:$GOROOT/bin:$GOPATH/bin"
```

4. **Database configuration**

```bash
export DB_HOST="localhost"
export DB_PORT="5432"
export DB_NAME="myapp"
export DB_USER="dbuser"
```

## Shell Configuration Files

Make exports permanent by adding them to configuration files:

1. **Bash** - `~/.bashrc` or `~/.bash_profile`

```bash
echo 'export MY_VAR="permanent_value"' >> ~/.bashrc
```

2. **Zsh** - `~/.zshrc`

```bash
echo 'export MY_VAR="permanent_value"' >> ~/.zshrc
```

3. **System-wide** - `/etc/environment` or `/etc/profile`

```bash
# /etc/environment
MY_GLOBAL_VAR="system_wide_value"
```

## Checking Variables

1. Check if variable is exported

```bash
env | grep MY_VAR
printenv MY_VAR
echo $MY_VAR
```

2. Check variable scope

```bash
# Local variable
MY_LOCAL="test"
bash -c 'echo $MY_LOCAL'  # Empty output

# Exported variable
export MY_EXPORTED="test"
bash -c 'echo $MY_EXPORTED'  # Shows "test"
```

## Advanced Usage

1. **Conditional exports**

```bash
if [ -d "/opt/myapp" ]; then
    export MYAPP_HOME="/opt/myapp"
fi
```

2. **Export with default values**

```bash
export EDITOR="${EDITOR:-vim}"
export PORT="${PORT:-3000}"
```

3. **Export arrays (Bash 4+)**

```bash
declare -a my_array=("item1" "item2" "item3")
export my_array
```

4. **Export with validation**

```bash
validate_and_export() {
    if [ -n "$1" ] && [ -n "$2" ]; then
        export "$1"="$2"
        echo "Exported $1=$2"
    else
        echo "Error: Invalid arguments"
    fi
}

validate_and_export "API_KEY" "your-secret-key"
```

## Use Cases

- **Development environments**: Setting up language-specific paths
- **Application configuration**: Database URLs, API keys, feature flags
- **System administration**: Custom PATH modifications, proxy settings
- **CI/CD pipelines**: Build configuration, deployment targets
- **Security**: Sensitive data that shouldn't be in scripts

## Important Notes

- Exported variables are inherited by child processes
- Changes to exported variables in child processes don't affect parent
- Use quotes for values with spaces or special characters
- Environment variables are typically uppercase by convention
- Be careful with sensitive data in environment variables
- Some variables (like PATH) should be appended to, not replaced

## Security Considerations

1. **Avoid sensitive data in exports**

```bash
# Bad
export PASSWORD="secret123"

# Better - read from secure file or prompt
read -s -p "Enter password: " PASSWORD
export PASSWORD
```

2. **Use temporary exports for sensitive operations**

```bash
# Export temporarily
export TEMP_TOKEN="secret"
my_command_that_needs_token
unset TEMP_TOKEN  # Clean up
```

The `export` command is fundamental for shell scripting and system administration, enabling proper environment configuration for applications and processes.

For more details, check the manual: `help export` or `man bash`
