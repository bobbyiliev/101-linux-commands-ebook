# The `free` command

The `free` command in Linux/Unix is used to show memory (RAM/SWAP) information.

# Usage

## Show memory usage

**Action:**
--- Output the memory usage - available and used, as well as swap

**Details:**
--- The values are shown in kibibytes by default.

**Command:**
```
free
```

## Show memory usage in human-readable form

**Action:**
--- Output the memory usage - available and used, as well as swap

**Details:**
--- Outputted values ARE human-readable (are in GB / MB)

**Command:**
```
free -h
```
## Show memory usage with a total line

**Action:**
--- Output the memory usage and also add a summary line with the total.

**Details:**
--- The `-t` flag is useful for seeing the combined total of memory and swap.

**Command:**
```
free -t
```