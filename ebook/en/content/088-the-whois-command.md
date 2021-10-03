# The `whois` command

The `whois` command in Linux to find out information about a domain, such as the owner of the domain, the owner’s contact information, and the nameservers that the domain is using.

### Examples:

1. Performs a whois query for the domain name: 	

```
whois {Domain_name}
```

2. -H option omits the lengthy legal disclaimers that many domain registries deliver along with the domain information.

```
whois -H {Domain_name}
```

### Syntax:

```
whois [ -h HOST ] [ -p PORT ] [ -aCFHlLMmrRSVx ] [ -g SOURCE:FIRST-LAST ] 
      [ -i ATTR ] [ -S SOURCE ] [ -T TYPE ] object
```
```
whois -t TYPE
```
```
whois -v TYPE
```
```
whois -q keyword
```


### Additional Flags and their Functionalities:

|**Flag**   |**Description**   |
|:---|:---|
|`-h HOST`, `--host HOST`|Connect to HOST.|
|`-H`|Do not display the legal disclaimers some registries like to show you.|
|`-p`, `--port PORT`|Connect to PORT.|
|`--verbose`|Be verbose.|
|`--help`|Display online help.|
|`--version`|Display client version information. Other options are flags understood by whois.ripe.net and some other RIPE-like servers.|
|`-a`|Also search all the mirrored databases.|
|`-b`|Return brief IP address ranges with abuse contact.|
|`-B`|Disable object filtering *(show the e-mail addresses)*|
|`-c`|Return the smallest IP address range with a reference to an irt object.|
|`-d`|Return the reverse DNS delegation object too.|
|`-g SOURCE:FIRST-LAST`|Search updates from SOURCE database between FIRST and LAST update serial number. It's useful to obtain Near Real Time Mirroring stream.|
|`-G`|Disable grouping of associated objects.|
|`-i ATTR[,ATTR]...`|Search objects having associated attributes. ATTR is attribute name. Attribute value is positional OBJECT argument.|
|`-K`|Return primary key attributes only. Exception is members attribute of set object which is always returned. Another exceptions are all attributes of objects organisation, person, and role that are never returned.|
|`-l`|Return the one level less specific object.|
|`-L`|Return all levels of less specific objects.|
|`-m`|Return all one level more specific objects.|
|`-M`|Return all levels of more specific objects.|
|`-q KEYWORD`|Return list of keywords supported by server. KEYWORD can be version for server version, sources for list of source databases, or types for object types.|
|`-r`|Disable recursive look-up for contact information.|
|`-R`|Disable following referrals and force showing the object from the local copy in the server.|
|`-s SOURCE[,SOURCE]...`|Request the server to search for objects mirrored from SOURCES. Sources are delimited by comma and the order is significant. Use `-q` sources option to obtain list of valid sources.|
|`-t TYPE`|Return the template for a object of TYPE.|
|`-T TYPE[,TYPE]...`|Restrict the search to objects of TYPE. Multiple types are separated by a comma.|
|`-v TYPE`|Return the verbose template for a object of TYPE.|
|`-x`|Search for only exact match on network address prefix.|
