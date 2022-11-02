---
layout: python_lab
title: Python operators
---

Operators are used to perform operations on data.

For example:

```python
1 + 1
2 * 2
```

It is hopefully clear what these expressions mean.
They will resolve to the integer values `2` and `4` respectively.

A valid expression requires two operands with an operator between them.

```plaintext
<operand> <operator> <operand>
```

Where an operand is a value of some kind (e.g. a literal) and an operator is something like a mathematical operator (`+`, `-` etc.).


>Getting the form wrong will lead to a syntax error.
>```python
>123 123
>123 +
>/ 123
>* 123 *
>```
>The above examples all fail because they have no sensible meaning.

## Arithmetic operators

Arithmetic operators contain few surprises.
The addition operator (`+`) adds numbers together. 
The multiplication operator (`*`) multiplies numbers together.
The following table lists the most common operators.

<figure>
<table>
    <thead>
        <tr>
        <th style="text-align:right"></th>
        <th style="text-align:left"></th>
        <th style="text-align:right"></th>
        <th style="text-align:left"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>+</code></td>
            <td>addition</td>
            <td><code>-</code></td>
            <td>subtraction</td>
        </tr>
        <tr>
            <td><code>*</code></td>
            <td>multiplication</td>
            <td><code>/</code></td>
            <td>division</td>
        </tr>
        <tr>
            <td><code>%</code></td>
            <td>modulus (remainder)</td>
            <td><code>//</code></td>
            <td>floor division</td>
        </tr>
        <tr>
            <td><code>**</code></td>
            <td>exponentiation</td>
            <td colspan="2"></td>
        </tr>
    </tbody>
</table>
<figcaption>arithmetic operators</figcaption>
</figure>

All of these can be used with integers and floats.
If both of the operands are integers, then the output is usually an integer (except for division, which outputs a float), otherwise its usually a float.

<figure>
    <img src="{{"/assets/img/arithmetic-operations.png" | relative_url }}" alt="arithmetic operations in IDLE">
    <figcaption>examples of arithmetic operations</figcaption>
</figure>

Hopefully the results are not surprising.
Arithmetic naturally applies to integers and floating point values.

Note that Boolean values will be treated as integers in arithmetic operations.

```python
True + True     # 2
True * False    # 0
True * 3.5      # 3.5
False * 3.5     # 0.0
```

>We will also see later that some of these operators can be used with sequence data types such as strings and lists like this.
>```python
>'hello' + ' ' + 'world'
>[1, 2, 3] + [4, 5, 6]
>```
>What's a list?
>We're getting there!

## Comparison operators

Comparison operators allow two values to be compared (obviously!).
They are tests for truth and so always produce boolean outputs.

For example we can test whether one value is greater than another value.

```python
10 > 10     # False
```

In the above case, the result is `False`, since `10` is not greater than `10`.

||||comparison operators|
|--:|:--|--:|:--|
|`<`|less than|`<=`|less than or equal to|
|`>`|greater than|`>=`|greater than or equal to|
|`==`|equal to|`!=`|not equal to| 

Their application to integers and floats are obvious.

<figure>
    <img src="{{"/assets/img/logical-operations.png" | relative_url }}" alt="logical operations in IDLE">
    <figcaption>examples of logical operations</figcaption>
</figure>

When used with strings, the comparison is alphanumeric.

```python
'b' > 'a'   # True
'A' > 'a'   # False
```

>Lowercase values are considered greater than uppercase values.
>This is because the unicode codepoints for the uppercase letters are before the lowercase letters.
>We can see this by using the built-in function `ord()` which will return the unicode code point for any one-character string.
>```python
>ord('A')    # 65
>ord('B')    # 66
>ord('a')    # 97
>ord('b')    # 98
>```

For longer sequences, the first elements are compared and only if they are equal will further elements be compared. 
Substrings are considered less than longer strings. 

```python
'abc' < 'abca'  # True
'abc' < 'Abca'  # False
```

## Logical operators

We can also use standard logical operators such as `not`, `and` and `or`. 

```python
not True
True and False
True or False
```

These also work with data types other than Boolean values.
Though it is not advisable to do this unless you understand precisely how it works.

>From [the documentation on boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations):
>
>"The operator `not` yields `True` if its argument is false, `False` otherwise."
>
>"The expression x `and` y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned."
>
>"The expression x `or` y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned."

This relies on the fact that all data types have a *truth value*.
That is, all values can be evaluated as a Boolean.
We can see this by using the built-in function `bool()` to *cast* a value to a boolean value.

```python
bool(1)         # True
bool(0)         # False
bool(-1)        # True
bool(2.1)       # True
bool(0.0)       # False
bool('hello')   # True
bool('')        # False
bool([1, 2, 3]) # True
bool([])        # False
```

Basically, everything evaluates to `True` unless it is zero or empty.

>There are similar functions* to cast values to other types:
>```python
>bool("zero")   # True
>int(1.0)       # 1
>float(5)       # 5.0
>str(1000)      # '1000'
>tuple('OK')    # ('O', 'K')
>list('WAT')    # ['W', 'A', 'T']
>dict(['OK'])   # {'O': 'K'}
>```
>[Built-in functions](https://docs.python.org/3/library/functions.html) are part of the basic python toolkit.
>We will introduce a number of other useful built-in functions in this set of exercises.
>
>*actually, these are not all strictly functions, some are type constructors.

The explicit casting to a boolean is not required when evaluating the *truthiness* of a value.
Python will actually call `bool()` for you here.

```python
not 12      # False
12 or 15    # 12
'' or 15    # 15
12 and 15   # 15
'' and 15   # ''
``` 

>This feature allows for some very *clear* code, as we shall see later when we look at conditionals and loops. 
>The Python community values clarity very highly.

Combinations of operators are fine, this can get as complicated as you like.
The usual precedence applies (brackets are evaluated first, then exponentiation, multiplication and division, addition and subtraction and finally comparisons and boolean operations). 

Higher precedence operations are evaluated before lower precedence operations.

Look at each of these expressions and try to predict how they will be evaluated.

```python
100 > 120 * 6 + 15
(100 > 120) * 6 + 15
200 / 25 != 2 ** 3
200 / (25 != 2) ** 3
100 > 120 * 6 + 15 or 200 / 25 != 2 ** 3
100 > 120 * 6 + 15 or 200 / (25 != 2) ** 3
(100 > 120) * 6 + 15 or 200 / (25 != 2) ** 3
(100 > 120) * 6 + (15 or 200) / (25 != 2) ** 3
```

Try them out in IDLE and see if you predicted correctly.

Notice that, for example, the comparison operations are evaluated last unless they are enclosed in brackets.

