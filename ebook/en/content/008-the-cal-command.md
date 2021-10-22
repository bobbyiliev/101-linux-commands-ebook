# The `cal` Command
The `cal` command displays a formatted calendar in the terminal. If no options are specified, cal displays the current month, with the current day highlighted.

### Syntax:
```
cal [general options] [-jy] [[month] year]
```

### Options:
|**Option**|**Description**|
|:--|:--|
|`-h`|Don't highlight today's date.|
|`-m month`|Specify a month to display. The month specifier is a full month name (e.g., February), a month abbreviation of at least three letters (e.g., Feb), or a number (e.g., 2). If you specify a number, followed by the letter "f" or "p", the month of the following or previous year, respectively, display. For instance, `-m 2f` displays February of next year.|
|`-y year`|Specify a year to display. For example, `-y 1970` displays the entire calendar of the year 1970.|
|`-3`|Display last month, this month, and next month.|
|`-1`|Display only this month. This is the default.|
|`-A num`|Display num months occurring after any months already specified. For example, `-3 -A 3` displays last month, this month, and four months after this one; and `-y 1970 -A 2` displays every month in 1970, and the first two months of 1971.|
|`-B num`|Display num months occurring before any months already specified. For example, `-3 -B 2` displays the previous three months, this month, and next month.|
|`-d YYYY-MM`|Operate as if the current month is number MM of year YYYY.|

### Examples:
1. Display the calendar for this month, with today highlighted.
```
cal
```

2. Same as the previous command, but do not highlight today.
```
cal -h
```

3. Display last month, this month, and next month.
```
cal -3
```
4. Display this entire year's calendar.
```
cal -y
```

5. Display the entire year 2000 calendar.
```
cal -y 2000
```

6. Same as the previous command.
```
cal 2000
```

7. Display the calendar for December of this year.
```
cal -m [December, Dec, or 12]
```

10. Display the calendar for December 2000.
```
cal 12 2000
```
