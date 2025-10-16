# The `mkdir` command

The `mkdir` command is used to create directories (folders) in Linux/Unix systems. It's one of the most fundamental file system commands and provides various options for creating single directories, multiple directories, and nested directory structures.

## Syntax

```bash
mkdir [OPTIONS] DIRECTORY [DIRECTORY ...]
```

## Key Features

- **Single Directory Creation**: Create individual directories
- **Multiple Directory Creation**: Create several directories at once
- **Nested Directory Creation**: Create parent directories automatically
- **Permission Setting**: Set directory permissions during creation
- **Verbose Output**: Display creation progress
- **SELinux Support**: Set security contexts

## Basic Usage

### Creating Single Directory

```bash
# Create a directory in current location
mkdir mydir

# Create directory with absolute path
mkdir /home/user/documents

# Create directory in home directory
mkdir ~/projects
```

### Creating Multiple Directories

```bash
# Create multiple directories at once
mkdir dir1 dir2 dir3

# Create directories with different paths
mkdir ~/documents ~/downloads ~/pictures

# Create numbered directories
mkdir project{1,2,3,4,5}

# Create directories with ranges
mkdir folder{01..10}
```

## Advanced Usage

### Creating Nested Directories

```bash
# Create nested directory structure (creates parent directories)
mkdir -p projects/web/frontend/src

# Create complex directory structure
mkdir -p company/{departments/{hr,finance,it},projects/{web,mobile,desktop}}

# Create directory structure with absolute path
mkdir -p /opt/myapp/{bin,config,logs,data}
```

### Setting Permissions During Creation

```bash
# Create directory with specific permissions (755)
mkdir -m 755 public_dir

# Create directory with full permissions for owner only (700)
mkdir -m 700 private_dir

# Create directory with read/write for owner, read for group and others (644)
mkdir -m 644 shared_dir

# Create directory with full access for everyone (777)
mkdir -m 777 temp_dir

# Using symbolic notation
mkdir -m u=rwx,g=rx,o=rx public_folder
```

### Verbose Mode

```bash
# Show what directories are being created
mkdir -v newdir

# Verbose with multiple directories
mkdir -v dir1 dir2 dir3

# Verbose with nested structure
mkdir -pv projects/{frontend/{src,dist},backend/{api,database}}
```

## Practical Examples

### Project Structure Creation

```bash
# Create a typical web project structure
mkdir -p mywebsite/{css,js,images,includes,admin}

# Create a software project structure
mkdir -p myproject/{src/{main,test},docs,build,config}

# Create a backup directory structure
mkdir -p backups/{daily,weekly,monthly}/{system,database,files}
```

### System Administration

```bash
# Create log directories for an application
sudo mkdir -p /var/log/myapp/{error,access,debug}

# Create configuration directories
sudo mkdir -p /etc/myapp/{conf.d,ssl,keys}

# Create data directories with proper permissions
sudo mkdir -p /var/lib/myapp/data
sudo mkdir -m 750 /var/lib/myapp/secure
```

### User Environment Setup

```bash
# Set up user development environment
mkdir -p ~/development/{projects,tools,scripts}
mkdir -p ~/development/projects/{personal,work,opensource}

# Create organization directories
mkdir -p ~/documents/{work,personal,finance,education}
mkdir -p ~/documents/work/{reports,presentations,spreadsheets}
```

## Working with Special Characters

### Directories with Spaces

```bash
# Create directory with spaces (use quotes)
mkdir "My Documents"
mkdir 'Project Files'

# Create multiple directories with spaces
mkdir "Dir One" "Dir Two" "Dir Three"

# Using escape characters
mkdir My\ Documents
```

### Special Characters

```bash
# Create directories with special characters
mkdir "data-2024"
mkdir "backup_$(date +%Y%m%d)"
mkdir "temp.$(whoami)"

# Avoid problematic characters
mkdir project_2024  # Better than "project 2024"
mkdir user_data     # Better than "user's data"
```

## Error Handling and Validation

### Common Error Scenarios

```bash
# Check if directory exists before creating
if [ ! -d "mydir" ]; then
    mkdir mydir
    echo "Directory created"
else
    echo "Directory already exists"
fi

# Create directory only if parent exists
mkdir subdir  # Fails if current directory doesn't exist
mkdir -p parentdir/subdir  # Creates both if needed
```

### Safe Directory Creation

```bash
# Function to safely create directories
create_safe_dir() {
    if mkdir -p "$1" 2>/dev/null; then
        echo "Created directory: $1"
    else
        echo "Failed to create directory: $1"
        return 1
    fi
}

# Usage
create_safe_dir "/path/to/new/directory"
```

## Combining with Other Commands

### Directory Creation and Navigation

```bash
# Create directory and immediately change to it
mkdir myproject && cd myproject

# Create and navigate in one command (function)
mkcd() {
    mkdir -p "$1" && cd "$1"
}
mkcd ~/projects/newproject
```

### Creating Directories with Files

```bash
# Create directory structure and add files
mkdir -p project/{src,docs,tests}
touch project/src/main.py
touch project/docs/README.md
touch project/tests/test_main.py

# Create directory and set up basic files
mkdir website
cd website
mkdir {css,js,images}
touch index.html css/style.css js/script.js
```

### Batch Operations

```bash
# Create directories from a list
cat > dirlist.txt << EOF
projects/web
projects/mobile
projects/desktop
documents/reports
documents/presentations
EOF

# Create all directories from file
while read dir; do
    mkdir -p "$dir"
done < dirlist.txt
```

## Permission and Ownership

### Setting Ownership After Creation

```bash
# Create directory and set ownership
mkdir myapp
sudo chown user:group myapp

# Create with specific permissions and ownership
sudo mkdir -m 755 /opt/myapp
sudo chown user:group /opt/myapp
```

### Creating Directories for Different Users

```bash
# Create user-specific directories
sudo mkdir -p /home/newuser/{Documents,Downloads,Pictures}
sudo chown -R newuser:newuser /home/newuser
sudo chmod 755 /home/newuser
```

## SELinux Context

### Setting SELinux Context

```bash
# Create directory with specific SELinux context
mkdir -Z user_home_t user_data

# Create directory and set context afterward
mkdir secure_data
sudo semanage fcontext -a -t httpd_exec_t "/path/to/secure_data(/.*)?"
sudo restorecon -R /path/to/secure_data
```

## Troubleshooting

### Common Issues and Solutions

```bash
# Permission denied
sudo mkdir /restricted/path  # Use sudo for system directories

# Parent directory doesn't exist
mkdir -p path/to/deep/directory  # Use -p flag

# Directory already exists
mkdir -p existing_dir  # -p prevents error if directory exists

# Invalid characters in name
mkdir "valid_name"  # Use quotes or escape special characters
```

### Debugging Directory Creation

```bash
# Check available space before creating
df -h .

# Verify parent directory permissions
ls -ld parent_directory

# Check if directory was created successfully
if [ -d "newdir" ]; then
    echo "Directory created successfully"
    ls -ld newdir
fi
```

## Options Reference

|**Option**|**Long Form**|**Description**|
|:---|:---|:---|
|`-m MODE`|`--mode=MODE`|Set file mode (permissions) for created directories|
|`-p`|`--parents`|Create parent directories as needed, no error if existing|
|`-v`|`--verbose`|Print a message for each created directory|
|`-Z CTX`|`--context=CTX`|Set SELinux security context|
|`--help`|-|Display help message and exit|
|`--version`|-|Output version information and exit|

## Best Practices

### Directory Naming Conventions

```bash
# Use descriptive names
mkdir user_documents    # Good
mkdir stuff            # Poor

# Use consistent naming patterns
mkdir project_2024_01
mkdir project_2024_02

# Avoid spaces and special characters
mkdir my-project       # Good
mkdir "my project"     # Works but can cause issues
```

### Organization Strategies

```bash
# Date-based organization
mkdir -p archives/$(date +%Y)/{01..12}

# Project-based organization
mkdir -p projects/{active,completed,archived}

# User-based organization
mkdir -p users/{admins,developers,testers}
```

### Automation and Scripting

```bash
#!/bin/bash
# Script to create standard project structure

PROJECT_NAME="$1"
if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: $0 <project_name>"
    exit 1
fi

echo "Creating project structure for: $PROJECT_NAME"
mkdir -p "$PROJECT_NAME"/{
    src/{main,test},
    docs/{api,user},
    config/{dev,prod,test},
    scripts/{build,deploy},
    data/{input,output,temp}
}

echo "Project structure created successfully!"
tree "$PROJECT_NAME"
```

## Integration with Other Tools

### With Version Control

```bash
# Create project with Git initialization
mkdir myproject
cd myproject
git init
mkdir {src,docs,tests}
touch .gitignore README.md
```

### With Docker

```bash
# Create Docker project structure
mkdir -p docker-project/{app,data,logs,config}
touch docker-project/Dockerfile
touch docker-project/docker-compose.yml
```

## Important Notes

- Use `-p` flag to avoid errors when directories already exist
- Be careful with permissions when creating system directories
- Always use quotes around directory names with spaces
- Consider using `tree` command to visualize created directory structures
- The `mkdir` command creates directories with default permissions modified by umask
- Use absolute paths when creating directories outside current location

The `mkdir` command is essential for organizing files and creating directory structures in Linux systems.

For more details, check the manual: `man mkdir`
