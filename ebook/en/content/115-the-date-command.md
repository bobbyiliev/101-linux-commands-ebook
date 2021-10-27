# The `date` command

The `date` command is used to print the system current date and time. 

`date` command is also used to set the date and time of the system, but you need to be the super-user *(root)* to do it.

### Examples:

1. To show the current date and time:

```
date
```

2. You can use -u option to show the date and time in UTC *(Coordinated Universal Time)* time zone

```
date -u
```

1. To display any given date string in formatted date:

```
date --date="2/02/2010"
date --date="2 years ago"
```

### Syntax:

```
date [OPTION]... [+FORMAT]
date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-d`|`--date=STRING`|convert the provided string into formatted date|
|`-f`|`--file=DATEFILE`|like `--date` but for files|
|`-I[FMT]`|`--iso-8601[=FMT]`|Display date and time in ISO 8601 format|
|`-r`|`--reference=FILE`|Display the last modification time of FILE|
|`-s`|`--set=STRING`|sets the time to the one described by STRING|
|`-u`|`--universal`|show the date and time in UTC *(Coordinated Universal Time)* time zone|
|`-R`|`--rfc-email`|Display date and time in ISO 8601 format Example: (Fri, 22 Oct 2021 05:18:42 +0200)|
|<center>-<center>|`rfc-3339=FMT`|Display date and time in RFC 3339 format|
|<center>-<center>|`--debug`|Usually used with `--date` to annotate the parsed date and warn about questionable  usage  to stderr|

### Control The output:

You can use Format specifiers to control the output date and time.

### Examples:
|**Command**   |**Output**   |
|:---|:---|
|`$ date "+%D"`|`10/22/21`|
|`$ date "+%D %T"`|`10/22/21 05:33:51`|
|`$ date "+%A %B %d %T %y"`|`Friday October 22 05:34:47 21`|

### Syntax:

```
date "+%[format-options ...]"
```

### List of Format specifiers to control the output:

|**Specifiers**   |**Description**   |
|:---|:---|
|`%a`|abbreviated weekday name *(e.g., Sun)*|
|`%A`|full weekday name *(e.g., Sunday)*|
|`%b`|abbreviated month name *(e.g., Jan)*|
|`%B`|full month name *(e.g., January)*|
|`%c`|date and time *(e.g., Thu Mar  3 23:05:25 2005)*|
|`%C`|century; like %Y, except omit last two digits (e.g., 20)|
|`%d`|day of month (e.g., 01)|
|`%D`|date; same as %m/%d/%y|
|`%e`|day of month, space padded; same as %_d|
|`%F`|full date; same as %Y-%m-%d|
|`%g`|last two digits of year of ISO week number (see %G)|
|`%G`|year of ISO week number (see %V); normally useful only with %V|
|`%h`|same as %b|
|`%H`|hour (00..23)|
|`%I`|hour (01..12)|
|`%j`|day of year (001..366)|
|`%k`|hour, space padded ( 0..23); same as %_H|
|`%l`|hour, space padded ( 1..12); same as %_I|
|`%m`|month (01..12)|
|`%M`|minute (00..59)|
|`%n`|a newline|
|`%N`|nanoseconds (000000000..999999999)|
|`%p`|locale's equivalent of either AM or PM; blank if not known|
|`%P`|like %p, but lower case|
|`%q`|quarter of year (1..4)|
|`%r`|locale's 12-hour clock time (e.g., 11:11:04 PM)|
|`%R`|24-hour hour and minute; same as %H:%M|
|`%s`|seconds since 1970-01-01 00:00:00 UTC|
|`%S`|second (00..60)|
|`%t`|a tab|
|`%T`|time; same as %H:%M:%S|
|`%u`|day of week (1..7); 1 is Monday|
|`%U`|week number of year, with Sunday as first day of week (00..53)|
|`%V`|ISO week number, with Monday as first day of week (01..53)|
|`%w`|day of week (0..6); 0 is Sunday|
|`%W`|week number of year, with Monday as first day of week (00..53)|
|`%x`|locale's date representation (e.g., 12/31/99)|
|`%X`|locale's time representation (e.g., 23:13:48)|
|`%y`|last two digits of year (00..99)|
|`%Y`|year|
|`%z`|+hhmm numeric time zone (e.g., -0400)|
|`%:z`|+hh:mm numeric time zone (e.g., -04:00)|
|`%::z`|+hh:mm:ss numeric time zone (e.g., -04:00:00)|
|`%:::z`|numeric  time  zone  with  :  to necessary precision (e.g., -04, +05:30)|
|`%Z`|alphabetic time zone abbreviation (e.g., EDT)|
