# The `expr` command

The `expr` command evaluates a given expression and displays its corresponding output. It is used for basic operations like addition, subtraction, multiplication, division, and modulus on integers and Evaluating regular expressions, string operations like substring, length of strings etc.

## Syntax

```
expr expression
```

## Few Examples:
1. ### Perform basic arithmetic operations using expr command
```
expr 7 + 14
expr 7 * 8
```

2. ### Comparing two expressions
```
x=10
y=20
res=`expr $x = $y`
echo $res
```

3. ### Match the numbers of characters in two strings
```
expr alphabet : alpha
```
4. ### Find the modulus value
```
expr 20 % 30  
```
5. ### Extract the substring
```
a=HelloWorld
b=`expr substr $a 6 10`
echo $b
```
### Additional Flags and their Functionalities

|**Flag** |**Description**   |
:---|:---|
|`--version`|output version information and exit|
|`--help`|Display this help and exit|


For more details: [Expr on Wikipedia](https://en.wikipedia.org/wiki/Expr)