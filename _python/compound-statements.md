---
layout: python_lab
week: 1
title: Compound statements
---

Essentially, compound statements define blocks of code that should be executed in particular ways or under certain circumstances.

Compound statements are made up of `clauses`.
Clauses have a `header` and an indented code block.
The headers typically control whether and how the code blocks will be executed.
There may be multiple clauses in a compound statement.

This is a simple compound statement with just one clause:

```python
if balanceA >= amount:
    balanceA -= amount
    balanceB += amount
```

> This example code is incomplete.
We are just showing the structure of a compound statement.
If you run this code, it will raise a NameError because the variables have not been defined.

The details are different with different compound statements, but clause headers will always begin with a keyword (`if` in this case) and will end in a colon (`:`).

The code block following the header consists of one or more indented statements and must end with a *dedent*, when the code returns to the original indentation level, this indicates the end of the code block.

**Be very careful with indentation!**
It is part of the syntax in python, this keeps the code clean and readable.
Often, if you get the indentation wrong, your code will not run. 
This is good because you can locate the problem and resolve it.
However, in some cases, a mistake in the indentation can lead to code which runs without error, but does not behave as intended.

This code:

```python
a = 1
if a > 0:
    print('incrementing')
    a += 1

print(a)
```

has a subtly different behaviour to the this code.

```python
a = 1
if a > 0:
    print('incrementing')
    a += 1

    print(a)
```

The difference between the two examples is the indentation level of the last line of code.

> Do not continue until you can clearly state the difference between these examples.
>
> Hint, they initially appear to produce the same result.
> Try them both after changing the first line to `a = 0`.

> For more information, check out the python documentation on [compound statements](https://docs.python.org/3/reference/compound_stmts.html).
