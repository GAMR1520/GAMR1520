---
week: 1
title: Compound statements
lang: python
---

Compound statements define blocks of code that should be executed in particular ways or under certain circumstances.
They are used for conditional statements, loops, function and class definitions, context managers and error handling.

Compound statements are made up of one or more *clauses*.
Clauses have a *header* and an indented *code block*.
The type of clause and any extra information provided, control whether and in what context the code block will be executed.

This is a simple compound statement with just one clause:

```python
if balanceA >= amount:
    balanceA -= amount
    balanceB += amount
```

The header defines the type of clause with a keyword (one of `if`, `elif`, `else`, `while`, `for`, `def`, `with`, `try`, `except` or `class`).

> There are a few newer compound statements, but we won't cover them in this module

Different clauses have different syntax.
Some (e.g. `try` or `else`) just include the keyword followed by a colon (`:`), whilst others (e.g. `if` or `for`) require additional expressions to be included as part of the header.

> In the above example, an `if` clause requires an expression that evaluates to a boolean value.
Comparison operators are commonly used for this, but any valid python expression is allowed.
>
> This example code is incomplete.
It demonstrates the structure of a compound statement.
If you run this code, it will raise a NameError because the variables have not been defined.

The details are different with different compound statements, but clause headers will always begin with a keyword (`if` in this case) and will end in a colon (`:`).

## Indentation

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


## Nesting compound statement

Compound statements can be nested.
In the CPython implementation, there used to be a low limit to how deeply nested you could go.
Reportedly 15 or 20 levels deep.
I tried an extended version of this in 3.10.6 and could not find any limit.

```python
a = 1
if a:
    if a:
        if a:
            if a:
                if a:
                    if a:
                        if a:
                            if a:
                                if a:
                                    if a:
                                        if a:
                                            if a:
                                                print(a)
```

Nevertheless, if you find your code is three levels deep and you need more levels of nesting you might want to think about refactoring your code for the sake of readability.

> **"Flat is better than nested."** - The zen of python

Adding a function is a nice way to break nesting across separate blocks and flatten out code.

```python
def something_nested(a):
    for i in a:
        for j in a:
            print(i, j)

data = [3, 2, 6]
for d in data:
    something_nested(range(d))

```

## Compound statements and interactive interpreters

Compound statements can be entered into interactive interpreters such as the IDLE shell, but its a bit tricky and annoying.

After entering the `if` clause (don't forget the colon), press enter and the prompt should automatically indent.
Continue typing the code block, line by line, pressing enter at the end of each line.
Once finished, press enter again to indicate the code block is complete.

<figure>
    <img src="{{"assets/img/conditional.png" | relative_url}}" alt="compound statements in IDLE">
    <figcaption>Compound statements in the IDLE shell</figcaption>
</figure>

Its often easier to write small code snippets into files and add `print()` statements to see what's going on.

> For more information, check out the python documentation on [compound statements](https://docs.python.org/3/reference/compound_stmts.html).
