# `lscpu` command

`lscpu` in Linux/Unix is used to display CPU Architecture info. `lscpu` gathers CPU architecture information from `sysfs` and `/proc/cpuinfo` files.

For example : 
 ```
  manish@godsmack:~$ lscpu
    Architecture:        x86_64
    CPU op-mode(s):      32-bit, 64-bit
    Byte Order:          Little Endian
    CPU(s):              4
    On-line CPU(s) list: 0-3
    Thread(s) per core:  2
    Core(s) per socket:  2
    Socket(s):           1
    NUMA node(s):        1
    Vendor ID:           GenuineIntel
    CPU family:          6
    Model:               142
    Model name:          Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz
    Stepping:            9
    CPU MHz:             700.024
    CPU max MHz:         3100.0000
    CPU min MHz:         400.0000
    BogoMIPS:            5399.81
    Virtualization:      VT-x   
    L1d cache:           32K
    L1i cache:           32K
    L2 cache:            256K
    L3 cache:            3072K
    NUMA node0 CPU(s):   0-3
 ```
  
  
## Options

`-a, --all`
    Include lines for online and offline CPUs in the output (default for -e). This option may only specified together with option -e or -p. 
    For example: `lsof -a`

`-b, --online`
    Limit the output to online CPUs (default for -p). This option may only be specified together with option -e or -p. 
    For example: `lscpu -b`

`-c, --offline`
    Limit the output to offline CPUs. This option may only be specified together with option -e or -p. 

`-e, --extended [=list]`
    Display the CPU information in human readable format.
    For example: `lsof -e`
    
For more info: use `man lscpu` or `lscpu --help`
