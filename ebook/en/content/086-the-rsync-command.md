# The `rsync` Command

  `rsync` is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from another host over any remote shell, or to/from a remote rsync daemon. It offers a large number of options that control every aspect of its behavior and permit very flexible specification of the set of files to be copied. It is famous for its delta-transfer algorithm, which reduces the amount of data sent over the network by sending only the differences between the source files and the existing files in the destination. Rsync is widely used for backups and mirroring and as an improved copy command for everyday use.

  Rsync finds files that need to be transferred using a `lqquick checkrq algorithm (by default)` that looks for files that have changed in size or in last-modified time. Any changes in the other preserved attributes (as requested by options) are made on the destination file directly when the quick check indicates that the file's data does not need to be updated.

**Some of the additional features of `rsync` are:**

- support for copying links, devices, owners, groups, and permissions
- exclude and exclude-from options similar to GNU tar
- a CVS exclude mode for ignoring the same files that CVS would ignore
- can use any transparent remote shell, including ssh or rsh
- does not require super-user privileges
- pipelining of file transfers to minimize latency costs
- support for anonymous or authenticated rsync daemons (ideal for mirroring)


## Examples:

1. Copy/Sync a File on a Local Computer
```
rsync -zvh backup.tar.gz /tmp/backups/
```

2. Copy/Sync a Directory on Local Computer
```
rsync -avzh /root/rpmpkgs /tmp/backups/

```

3. Copy/Sync Files and Directory to or From a Server
```
rsync -avzh /root/rpmpkgs root@192.168.0.141:/root/
```

4. Show Progress While Transferring Data with rsync
```
rsync -avzhe ssh --progress /root/rpmpkgs root@192.168.0.141:/root/rpmpkgs
```

5. Set the Max Size of Files to be Transferred
```
rsync -avzhe ssh --max-size='200k' /var/lib/rpm/ root@192.168.0.151:/root/tmprpm
```


## Syntax:

```
1. Local:  rsync [OPTION...] SRC... [DEST]
2. Access via remote shell:
  Pull: rsync [OPTION...] [USER@]HOST:SRC... [DEST]
  Push: rsync [OPTION...] SRC... [USER@]HOST:DEST
3. Access via rsync daemon:
  Pull: rsync [OPTION...] [USER@]HOST::SRC... [DEST]
        rsync [OPTION...] rsync://[USER@]HOST[:PORT]/SRC... [DEST]
  Push: rsync [OPTION...] SRC... [USER@]HOST::DEST
        rsync [OPTION...] SRC... rsync://[USER@]HOST[:PORT]/DEST
```



## Additional Flags and their Functionalities:

|Short Flag |	Long Flag	| Description |
|---|---|---|
|-v| --verbose|	increase verbosity|
|-q| --quiet|	suppress non-error messages|
|-|--no-motd	|suppress daemon-mode MOTD (see caveat)|
|-c| --checksum|	skip based on checksum, not mod-time & size|
|-a|--archive	|archive mode; equals -rlptgoD (no -H,-A,-X)|
|-|--no-OPTION|	turn off an implied OPTION (e.g., --no-D)|
|-r| --recursive|	recurse into directories|
|-R| --relative	|use relative path names|
|-|--no-implied-dirs|	don't send implied dirs with --relative|
|-b| --backup	|make backups (see --suffix & --backup-dir)|
|-|--backup-dir=DIR	|make backups into hierarchy based in DIR|
|-|--suffix=SUFFIX	|backup suffix (default ~ w/o --backup-dir)|
|-u| --update	|skip files that are newer on the receiver|
|-|--inplace	|update destination files in-place|
|-|--append	|append data onto shorter files|
|-|--append-verify|	--append w/old data in file checksum|
|-d| --dirs	|transfer directories without recursing|
|-l| --links	|copy symlinks as symlinks|
|-L| --copy-links|	transform symlink into referent file/dir|
|-|--copy-unsafe-links|	only "unsafe" symlinks are transformed|
|-|--safe-links	|ignore symlinks that point outside the tree|
|-k| --copy-dirlinks|	transform symlink to dir into referent dir|
|-K| --keep-dirlinks|	treat symlinked dir on receiver as dir|
|-H| --hard-links|	preserve hard links|
|-p| --perms	|preserve permissions|
|-E| --executability|	preserve executability|
|-|--chmod=CHMOD|	affect file and/or directory permissions|
|-A| --acls	|preserve ACLs (implies -p)|
|-X| --xattrs	|preserve extended attributes|
|-o| --owner	|preserve owner (super-user only)|
|-g| --group	|preserve group|
|-|--devices	|preserve device files (super-user only)|
|-|--specials|	preserve special files|
|-D	|-|same as --devices --specials|
|-t| --times	|preserve modification times|
|-O| --omit-dir-times|	omit directories from --times|
|-|--super	|receiver attempts super-user activities|
|-|--fake-super|	store/recover privileged attrs using xattrs|
|-S| --sparse	|handle sparse files efficiently|
|-n| --dry-run	|perform a trial run with no changes made|
|-W| --whole-file	|copy files whole (w/o delta-xfer algorithm)|
|-x| --one-file-system|	don't cross filesystem boundaries|
|-B| --block-size=SIZE|	force a fixed checksum block-size|
|-e| --rsh=COMMAND	|specify the remote shell to use|
|-|--rsync-path=PROGRAM	|specify the rsync to run on remote machine|
|-|--existing	skip |creating new files on receiver|
|-|--ignore-existing	|skip updating files that exist on receiver|
|-|--remove-source-files|	sender removes synchronized files (non-dir)|
|-|--del	|an alias for --delete-during|
|-|--delete	|delete extraneous files from dest dirs|
|-|--delete-before|	receiver deletes before transfer, not during|
|-|--delete-during|	receiver deletes during the transfer|
|-|--delete-delay	|find deletions during, delete after|
|-|--delete-after	|receiver deletes after transfer, not during|
|-|--delete-excluded|	also delete excluded files from dest dirs|
|-|--ignore-errors|	delete even if there are I/O errors|
|-|--force	|force deletion of dirs even if not empty|
|-|--max-delete=NUM|	don't delete more than NUM files|
|-|--max-size=SIZE|	don't transfer any file larger than SIZE|
|-|--min-size=SIZE|	don't transfer any file smaller than SIZE|
|-|--partial|	keep partially transferred files|
|-|--partial-dir=DIR	|put a partially transferred file into DIR|
|-|--delay-updates	|put all updated files into place at end|
|-m | --prune-empty-dirs|	prune empty directory chains from file-list|
|-|--numeric-ids|	don't map uid/gid values by user/group name|
|-|--timeout=SECONDS|	set I/O timeout in seconds|
|-|--contimeout=SECONDS|	set daemon connection timeout in seconds|
|-I | --ignore-times	|don't skip files that match size and time|
|-|--size-only|	skip files that match in size|
|-|--modify-window=NUM	|compare mod-times with reduced accuracy|
|-T| --temp-dir=DIR|	create temporary files in directory DIR|
|-y| --fuzzy	|find similar file for basis if no dest file|
|-|--compare-dest=DIR|	also compare received files relative to DIR|
|-|--copy-dest=DIR|	... and include copies of unchanged files|
|- |--link-dest=DIR|	hardlink to files in DIR when unchanged|
|-z | --compress|	compress file data during the transfer|
|-|--compress-level=NUM	|explicitly set compression level|
| - |--skip-compress=LIST|	skip compressing files with suffix in LIST|
|-C | --cvs-exclude	|auto-ignore files in the same way CVS does|
|-f | --filter=RULE	|add a file-filtering RULE|
| -F | - |same as --filter='dir-merge /.rsync-filter' ; repeated: --filter='- .rsync-filter'|
|-|--exclude=PATTERN	|exclude files matching PATTERN|
|-|--exclude-from=FILE|	read exclude patterns from FILE|
|-|--include=PATTERN	|don't exclude files matching PATTERN|
|-|--include-from=FILE|	read include patterns from FILE|
|-|--files-from=FILE|	read list of source-file names from FILE|
|-0| --from0	|all *from/filter files are delimited by 0s|
|-s| --protect-args|	no space-splitting; wildcard chars only|
|-|--address=ADDRESS|	bind address for outgoing socket to daemon|
| - |--port=PORT	|specify double-colon alternate port number|
|-| --sockopts=OPTIONS|	specify custom TCP options|
|-|--blocking-io	|use blocking I/O for the remote shell|
|-|--stats|	give some file-transfer stats|
|-8|--8-bit-output	|leave high-bit chars unescaped in output|
|-h| --human-readable	|output numbers in a human-readable format|
|- |--progress	|show progress during transfer|
|-P|- |	same as --partial --progress|
|-i | --itemize-changes|	output a change-summary for all updates|
| -|--out-format=FORMAT|	output updates using the specified FORMAT|
|- |--log-file=FILE	|log what we're doing to the specified FILE|
|-|--log-file-format=FMT|	log updates using the specified FMT|
|-|--password-file=FILE|	read daemon-access password from FILE|
|-|--list-only|	list the files instead of copying them|
|- |--bwlimit=KBPS|	limit I/O bandwidth; KBytes per second|
|-|--write-batch=FILE|	write a batched update to FILE|
|-|--only-write-batch=FILE|	like --write-batch but w/o updating dest|
|-|--read-batch=FILE|	read a batched update from FILE|
|-|--protocol=NUM	|force an older protocol version to be used|
|-|--iconv=CONVERT_SPEC	|request charset conversion of file names|
|- | --checksum-seed=NUM|	set block/file checksum seed (advanced)|
|- |--daemon	|run as an rsync daemon|
|-4 | --ipv4	|prefer IPv4|
|-6 | --ipv6	|prefer IPv6|
| - |--version	|print version number|
|-h |--help	|show help|


