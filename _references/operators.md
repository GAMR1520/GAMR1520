---
title: Python operators
week: 1
lang: python
---

Operators are used to perform operations on data.

For example:

```python
1 + 1
2 * 2
```

It is hopefully clear what these expressions mean.
They will resolve to the integer values `2` and `4` respectively.

A valid expression requires two *operands* with an operator between them.

```plaintext
<operand> <operator> <operand>
```

Where an *operand* is a value of some kind (e.g. a literal) and an operator is something like a mathematical operator (`+`, `-` etc.).


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

<table>
    <thead>
        <tr>
        <th colspan="4">Arithmetic operators</th>
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

Comparison operators allow two values to be compared (the clue is in the name!).
They are tests for truth and so always produce boolean outputs.

For example we can test whether one value is greater than another value.

```python
10 > 10     # False
```

In the above case, the result is `False`, since `10` is not greater than `10`.

<table>
    <thead>
        <tr>
        <th colspan="4">Comparison operators</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code><</code></td>
            <td>less than</td>
            <td><code><=</code></td>
            <td>less than or equal to</td>
        </tr>
        <tr>
            <td><code>></code></td>
            <td>greater than</td>
            <td><code>>=</code></td>
            <td>greater than or equal to</td>
        </tr>
        <tr>
            <td><code>==</code></td>
            <td>equal to</td>
            <td><code>!=</code></td>
            <td>not equal to</td>
        </tr>
    </tbody>
</table>

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

>There are similar functions<sup>*</sup> to cast values to other types:
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
The usual precedence applies (brackets are evaluated first, then exponentiation, multiplication and division, addition and subtraction, comparisons, and finally boolean operations). 

Higher precedence operations are evaluated before lower precedence operations.
For example, boolean operations are evaluated last unless they are enclosed in brackets.
So if an expression contains a boolean operator it will determine the meaning of the expression unless there are brackets around the boolean operator.

Study each of these expressions to understand how they are evaluated.

Here, the comparison `>` is the last to be evaluated.

```python
100 > 120 * 6 + 15
```
{: .small-margin}
```plaintext
False
```
{: .small-margin}

Adding brackets changes the meaning.
So the `False` inside the brackets is cast to `0` and becomes part of the calculation.

```python
(100 > 120) * 6 + 15
```
{: .small-margin}
```plaintext
15
```
{: .small-margin}

Again, a comparison returns a Boolean value.

```python
200 / 25 != 2 ** 3
```
{: .small-margin}
```plaintext
False
```
{: .small-margin}

Adding brackets change the meaning completely.

```python
200 / (25 != 2) ** 3
```
{: .small-margin}
```plaintext
200.0
```
{: .small-margin}

Here the Boolean `or` returns the value of the right side.

```python
100 > 120 * 6 + 15 or 200 / (25 != 2) ** 3
```
{: .small-margin}
```plaintext
200.0
```
{: .small-margin}

If the left side of an `or` is *truthy* then it is returned and the right side is not even evaluated.

```python
(100 > 120) * 6 + 15 or 200 / (25 != 2) ** 3
```
{: .small-margin}
```plaintext
15
```
{: .small-margin}

Adding brackets completely changes the meaning again.

```python
(100 > 120) * 6 + (15 or 200) / (25 != 2) ** 3
```
{: .small-margin}
```plaintext
15.0
```
{: .small-margin}


Write some of your own in IDLE and see if you can predict the output correctly.


One wrinkle to note is that chaining comparison operators is allowed.

```python
1 < 2 < 3
```

This is equivalent to the following.

```python
1 < 2 and 2 < 3
```

This can be tricky to follow, so is probably best avoided in all but the simplest cases.

```python
50 > 40 != 50
50 > 40 != 40
50 > 50 != 40
50 > 50 != 50
```
{: .small-margin}

```plaintext
True
False
False
False
```
{: .small-margin}
