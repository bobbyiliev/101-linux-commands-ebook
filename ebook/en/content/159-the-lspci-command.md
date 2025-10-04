# The `lspci` command

The `lspci` command lists all PCI (Peripheral Component Interconnect) devices connected to the system. It provides detailed information about hardware components including graphics cards, network adapters, sound cards, storage controllers, and other PCI-based devices.

## Syntax

```
lspci [options]
```

## Key Features

- **Hardware Detection**: Lists all PCI devices
- **Detailed Information**: Vendor, device, class, and capabilities
- **Tree View**: Shows device hierarchy and relationships
- **Filtering Options**: Search by vendor, device, or class
- **Verbose Output**: Multiple levels of detail

## Basic Usage

### Simple Device Listing

```bash
# List all PCI devices
lspci

# Example output:
# 00:00.0 Host bridge: Intel Corporation Device 9b61
# 00:01.0 PCI bridge: Intel Corporation Device 1901
# 00:02.0 VGA compatible controller: Intel Corporation Device 9bc4
# 00:14.0 USB controller: Intel Corporation Device a36d
```

### Human-Readable Output

```bash
# Show device names instead of just IDs
lspci -nn

# More verbose output
lspci -v

# Very verbose output (includes everything)
lspci -vv

# Extremely verbose output
lspci -vvv
```

## Common Options

### Basic Options

```bash
# -v: Verbose (show detailed info)
lspci -v

# -vv: Very verbose
lspci -vv

# -n: Show numeric IDs instead of names
lspci -n

# -nn: Show both names and numeric IDs
lspci -nn

# -k: Show kernel drivers
lspci -k
```

### Display Options

```bash
# -t: Tree format
lspci -t

# -tv: Tree format with verbose info
lspci -tv

# -x: Show hex dump of config space
lspci -x

# -xxx: Show full hex dump
lspci -xxx
```

## Filtering and Selection

### 1. By Device Type

```bash
# Graphics cards
lspci | grep -i vga
lspci | grep -i display

# Network adapters
lspci | grep -i network
lspci | grep -i ethernet

# USB controllers
lspci | grep -i usb

# Sound cards
lspci | grep -i audio
lspci | grep -i sound

# Storage controllers
lspci | grep -i storage
lspci | grep -i sata
```

### 2. By Vendor

```bash
# Intel devices
lspci | grep -i intel

# AMD devices
lspci | grep -i amd

# NVIDIA devices
lspci | grep -i nvidia

# Broadcom devices
lspci | grep -i broadcom
```

### 3. Specific Device Selection

```bash
# Select specific device by bus ID
lspci -s 00:02.0

# Select multiple devices
lspci -s 00:02.0,00:14.0

# Select by vendor ID
lspci -d 8086:

# Select by vendor and device ID
lspci -d 8086:9bc4
```

## Detailed Information

### 1. Verbose Device Information

```bash
# Show capabilities and features
lspci -v

# Example output includes:
# - Memory addresses
# - IRQ assignments
# - Capabilities (MSI, Power Management, etc.)
# - Kernel modules/drivers

# Very detailed information
lspci -vv
# Includes:
# - Extended capabilities
# - Configuration registers
# - Link status and speeds
```

### 2. Driver Information

```bash
# Show which kernel drivers are in use
lspci -k

# Example output:
# 00:02.0 VGA compatible controller: Intel Corporation Device 9bc4
#         Subsystem: Dell Device 097d
#         Kernel driver in use: i915
#         Kernel modules: i915

# Combine with verbose for more detail
lspci -vk
```

### 3. Configuration Space

```bash
# Show configuration space (hex dump)
lspci -x

# Full configuration space
lspci -xxx

# Specific device configuration
lspci -s 00:02.0 -xxx
```

## Tree View and Topology

### 1. Device Hierarchy

```bash
# Show device tree structure
lspci -t

# Example output:
# -[0000:00]-+-00.0  Intel Corporation Device 9b61
#            +-01.0-[01]--
#            +-02.0  Intel Corporation Device 9bc4
#            +-14.0  Intel Corporation Device a36d

# Tree with device names
lspci -tv
```

### 2. Bus Information

```bash
# Show bridges and connections
lspci -tv | grep -E "(bridge|Bridge)"

# PCI Express information
lspci -vv | grep -A 5 -B 5 "Express"

# Link capabilities and status
lspci -vv | grep -E "(Link|Speed|Width)"
```

## Hardware Analysis

### 1. Graphics Card Information

```bash
# List graphics devices
get_gpu_info() {
    echo "=== Graphics Cards ==="
    lspci | grep -i -E "(vga|display|3d)"
    echo

    echo "=== Detailed GPU Information ==="
    lspci -v | grep -A 10 -B 2 -i -E "(vga|display)"
    echo

    echo "=== GPU Drivers ==="
    lspci -k | grep -A 3 -B 1 -i -E "(vga|display)"
}

get_gpu_info
```

### 2. Network Interface Analysis

```bash
# Network adapter details
get_network_info() {
    echo "=== Network Adapters ==="
    lspci | grep -i -E "(network|ethernet|wireless)"
    echo

    echo "=== Network Driver Information ==="
    lspci -k | grep -A 3 -B 1 -i -E "(network|ethernet)"
    echo

    echo "=== Wireless Capabilities ==="
    lspci -vv | grep -A 20 -B 5 -i wireless
}

get_network_info
```

### 3. Storage Controller Information

```bash
# Storage device details
get_storage_info() {
    echo "=== Storage Controllers ==="
    lspci | grep -i -E "(storage|sata|ide|scsi|nvme)"
    echo

    echo "=== Storage Driver Information ==="
    lspci -k | grep -A 3 -B 1 -i -E "(storage|sata|ahci)"
    echo

    echo "=== SATA Capabilities ==="
    lspci -vv | grep -A 10 -B 2 -i sata
}

get_storage_info
```

## System Analysis Scripts

### 1. Hardware Inventory

```bash
#!/bin/bash
# Complete hardware inventory using lspci

hardware_inventory() {
    echo "=== PCI Hardware Inventory ==="
    echo "Generated: $(date)"
    echo

    echo "--- System Overview ---"
    lspci | wc -l | xargs echo "Total PCI devices:"
    echo

    echo "--- Graphics ---"
    lspci | grep -i -E "(vga|display|3d)" || echo "No graphics devices found"
    echo

    echo "--- Network ---"
    lspci | grep -i -E "(network|ethernet|wireless)" || echo "No network devices found"
    echo

    echo "--- Storage ---"
    lspci | grep -i -E "(storage|sata|ide|nvme)" || echo "No storage controllers found"
    echo

    echo "--- Audio ---"
    lspci | grep -i -E "(audio|sound|multimedia)" || echo "No audio devices found"
    echo

    echo "--- USB Controllers ---"
    lspci | grep -i usb || echo "No USB controllers found"
    echo

    echo "--- Other Devices ---"
    lspci | grep -v -i -E "(vga|display|3d|network|ethernet|wireless|storage|sata|ide|nvme|audio|sound|multimedia|usb|bridge|host)" || echo "No other devices"
}

hardware_inventory > hardware_inventory.txt
```

### 2. Driver Status Check

```bash
#!/bin/bash
# Check driver status for all PCI devices

check_drivers() {
    echo "=== PCI Driver Status ==="

    lspci | while read line; do
        device_id=$(echo "$line" | cut -d' ' -f1)
        device_name=$(echo "$line" | cut -d' ' -f2-)

        driver_info=$(lspci -k -s "$device_id" | grep "Kernel driver in use")

        if [ -n "$driver_info" ]; then
            driver=$(echo "$driver_info" | cut -d':' -f2 | xargs)
            echo "✓ $device_id: $device_name -> $driver"
        else
            echo "✗ $device_id: $device_name -> NO DRIVER"
        fi
    done
}

check_drivers
```

### 3. Performance Analysis

```bash
#!/bin/bash
# Analyze PCI device performance capabilities

analyze_performance() {
    echo "=== PCI Performance Analysis ==="

    echo "--- PCIe Link Speeds ---"
    lspci -vv | grep -A 1 -B 1 "Link.*Speed" | grep -E "(:|Speed|Width)"
    echo

    echo "--- Memory Mappings ---"
    lspci -v | grep -E "(Memory at|I/O ports at)" | sort | uniq -c | sort -nr
    echo

    echo "--- Power Management ---"
    lspci -vv | grep -c "Power Management" | xargs echo "Devices with power management:"
    echo

    echo "--- MSI Capabilities ---"
    lspci -vv | grep -c "MSI:" | xargs echo "Devices with MSI support:"
    echo

    echo "--- 64-bit Devices ---"
    lspci -vv | grep -c "64-bit" | xargs echo "64-bit capable devices:"
}

analyze_performance
```

## Troubleshooting

### 1. Device Detection Issues

```bash
# Check if device is detected
check_device_detection() {
    local search_term="$1"

    echo "Searching for: $search_term"

    devices=$(lspci | grep -i "$search_term")
    if [ -n "$devices" ]; then
        echo "✓ Device(s) found:"
        echo "$devices"
        echo

        echo "Driver information:"
        echo "$devices" | while read line; do
            device_id=$(echo "$line" | cut -d' ' -f1)
            lspci -k -s "$device_id" | grep -E "(driver|module)"
        done
    else
        echo "✗ No devices found matching '$search_term'"
        echo "Try checking:"
        echo "  - Physical connections"
        echo "  - BIOS/UEFI settings"
        echo "  - Power supply"
    fi
}

# Usage examples
check_device_detection "graphics"
check_device_detection "network"
```

### 2. Driver Issues

```bash
# Find devices without drivers
find_missing_drivers() {
    echo "=== Devices Without Drivers ==="

    lspci | while read line; do
        device_id=$(echo "$line" | cut -d' ' -f1)
        device_name=$(echo "$line" | cut -d' ' -f2-)

        if ! lspci -k -s "$device_id" | grep -q "Kernel driver in use"; then
            echo "Missing driver: $device_id - $device_name"

            # Try to find available modules
            modules=$(lspci -k -s "$device_id" | grep "Kernel modules:" | cut -d':' -f2)
            if [ -n "$modules" ]; then
                echo "  Available modules:$modules"
            fi
        fi
    done
}

find_missing_drivers
```

### 3. Hardware Compatibility

```bash
# Check hardware compatibility
check_compatibility() {
    echo "=== Hardware Compatibility Check ==="

    echo "--- Unsupported Devices ---"
    lspci -nn | while read line; do
        if echo "$line" | grep -q "\[ffff:"; then
            echo "Possible unsupported device: $line"
        fi
    done
    echo

    echo "--- Legacy Devices ---"
    lspci | grep -i -E "(legacy|isa|parallel|serial|floppy)" || echo "No legacy devices found"
    echo

    echo "--- Vendor Support ---"
    echo "Intel devices: $(lspci | grep -i intel | wc -l)"
    echo "AMD devices: $(lspci | grep -i amd | wc -l)"
    echo "NVIDIA devices: $(lspci | grep -i nvidia | wc -l)"
    echo "Other vendors: $(lspci | grep -v -i -E "(intel|amd|nvidia)" | wc -l)"
}

check_compatibility
```

## Advanced Usage

### 1. Configuration Space Analysis

```bash
# Analyze specific device configuration
analyze_device_config() {
    local device_id="$1"

    echo "=== Configuration Analysis for $device_id ==="

    echo "--- Basic Information ---"
    lspci -s "$device_id" -v
    echo

    echo "--- Configuration Space ---"
    lspci -s "$device_id" -x
    echo

    echo "--- Capabilities ---"
    lspci -s "$device_id" -vv | grep -A 20 "Capabilities:"
}

# Usage: analyze_device_config "00:02.0"
```

### 2. Bandwidth Analysis

```bash
# Analyze PCIe bandwidth
analyze_bandwidth() {
    echo "=== PCIe Bandwidth Analysis ==="

    lspci -vv | grep -A 2 -B 2 "Express.*Root Port\|Express.*Endpoint" | \
    while read line; do
        if echo "$line" | grep -q "Express"; then
            echo "Device: $line"
        elif echo "$line" | grep -q "Link.*Speed"; then
            echo "  $line"
        fi
    done
}

analyze_bandwidth
```

### 3. Power Management

```bash
# Check power management capabilities
check_power_management() {
    echo "=== Power Management Status ==="

    lspci -vv | grep -B 5 -A 10 "Power Management" | \
    grep -E "(^[0-9a-f]{2}:[0-9a-f]{2}\.[0-9]|Power Management|PME)"
}

check_power_management
```

## Integration with Other Tools

### 1. Combining with lsmod

```bash
# Match PCI devices with loaded modules
match_devices_modules() {
    echo "=== PCI Devices and Kernel Modules ==="

    lspci -k | grep -E "(^[0-9a-f]{2}:|Kernel driver|Kernel modules)" | \
    while read line; do
        if [[ "$line" =~ ^[0-9a-f]{2}: ]]; then
            echo "$line"
        elif [[ "$line" =~ "Kernel driver in use:" ]]; then
            driver=$(echo "$line" | cut -d':' -f2 | xargs)
            echo "  Active driver: $driver"
            lsmod | grep "^$driver" && echo "    ✓ Module loaded" || echo "    ✗ Module not found"
        fi
    done
}
```

### 2. Combining with udev

```bash
# Check udev rules for PCI devices
check_udev_rules() {
    local device_id="$1"

    echo "Checking udev rules for device: $device_id"

    # Get vendor and device IDs
    vendor_device=$(lspci -n -s "$device_id" | awk '{print $3}')
    vendor_id=$(echo "$vendor_device" | cut -d':' -f1)
    device_id_hex=$(echo "$vendor_device" | cut -d':' -f2)

    echo "Vendor ID: $vendor_id, Device ID: $device_id_hex"

    # Search udev rules
    find /etc/udev/rules.d /lib/udev/rules.d -name "*.rules" -exec grep -l "$vendor_id\|$device_id_hex" {} \; 2>/dev/null
}
```

## Security Considerations

### 1. Hardware Security

```bash
# Check for security-relevant hardware
check_security_hardware() {
    echo "=== Security Hardware Check ==="

    echo "--- TPM Devices ---"
    lspci | grep -i tpm || echo "No TPM devices found"
    echo

    echo "--- Virtualization Support ---"
    lspci -vv | grep -i -E "(vt-x|amd-v|virtualization)" || echo "Check CPU flags for virtualization"
    echo

    echo "--- IOMMU Support ---"
    lspci -vv | grep -i iommu || echo "No explicit IOMMU references found"
    echo

    echo "--- Hardware Security Modules ---"
    lspci | grep -i -E "(security|crypto|hsm)" || echo "No HSM devices found"
}

check_security_hardware
```

## Best Practices

### 1. Regular Hardware Monitoring

```bash
# Create hardware monitoring script
#!/bin/bash
# Monitor hardware changes

BASELINE_FILE="/var/lib/hardware_baseline.txt"
CURRENT_FILE="/tmp/current_hardware.txt"

# Generate current state
lspci -nn > "$CURRENT_FILE"

# Compare with baseline
if [ -f "$BASELINE_FILE" ]; then
    if ! diff -q "$BASELINE_FILE" "$CURRENT_FILE" >/dev/null; then
        echo "Hardware configuration changed!"
        echo "Changes:"
        diff "$BASELINE_FILE" "$CURRENT_FILE"
    fi
else
    echo "Creating hardware baseline"
fi

# Update baseline
cp "$CURRENT_FILE" "$BASELINE_FILE"
```

### 2. Documentation

```bash
# Generate hardware documentation
document_hardware() {
    local output_file="hardware_documentation_$(date +%Y%m%d).txt"

    {
        echo "Hardware Documentation"
        echo "Generated: $(date)"
        echo "Hostname: $(hostname)"
        echo "========================="
        echo

        echo "PCI Device Summary:"
        lspci | wc -l | xargs echo "Total devices:"
        echo

        echo "Detailed Device List:"
        lspci -nn
        echo

        echo "Driver Status:"
        lspci -k
        echo

        echo "Device Tree:"
        lspci -tv

    } > "$output_file"

    echo "Documentation saved to: $output_file"
}
```

## Important Notes

- **Root Access**: Some detailed information requires root privileges
- **Hardware Detection**: Only shows devices connected to PCI bus
- **Driver Status**: Shows currently loaded drivers, not all available drivers
- **Updates**: Device information is read from kernel, may require hardware rescan
- **Vendor IDs**: Numeric IDs are standardized, names come from PCI ID database
- **Tree View**: Shows physical bus topology and device relationships

The `lspci` command is essential for hardware troubleshooting, driver management, and system analysis.

For more details, check the manual: `man lspci`
