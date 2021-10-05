# The `vmstat` command

The `vmstat` command lets you monitor the performance of your system. It shows you information about your memory, disk, processes, CPU scheduling, paging, and block IO. This command is also referred to as **virtual memory statistic report**.

The very first report that is produced shows you the average details since the last reboot and after that, other reports are made which report over time.

### `vmstat`

![vmstat](https://imgur.com/9HZgBRN.png)

As you can see it is a pretty useful little command. The most important things that we see above are the `free`, which shows us the free space that is not being used, `si` shows us how much memory is swapped in every second in kB, and `so` shows how much memory is swapped out each second in kB as well.

### `vmstat -a`

If we run `vmstat -a`, it will show us the active and inactive memory of the system running.

![vmstat -a](https://imgur.com/LjL4tRh.png)

### `vmstat -d`

The `vmstat -d` command shows us all the disk statistics.

![vmstat -d](https://imgur.com/y3L0pNN.png)

As you can see this is a pretty useful little command that shows you different statistics about your virtual memory
