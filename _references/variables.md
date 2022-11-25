---
title: Variables and assignment
week: 1
lang: python
---


In the [operators]({{"references/operators" | relative_url}}) examples we used [literal values]({{"references/literals" | relative_url}}) such as `True`, `'hello'`, `120` and `1.0`.
When these literal values are interpreted, the data they represent are stored in memory.
In our very simple, one-line programmes we combined literals with operators and the calculations were also applied in memory before the result was displayed by the interactive interpreter.

Because we no longer have a reference to these values, neither the literal values, nor the results of the calculations are accessible to our programme.
However, the data remain in memory until the Python *garbage collector* finds them and frees up the memory for reuse.
Python automatically does this with any data our programme cannot access.

Variables allow us to access and manipulate values in memory across multiple python expressions.
We can capture meaningful values in memory and use them in our programme by assigning them to variables.

We use the `=` operator for assignment.
Try the following.

```python
a = 1
```

The code is assigning the value `1` to a name `a`.
This causes the value `1` to be stored in memory and provides our programme with access to this value via the name `a`.

> The data stored in memory includes more than just the value `1`.
It includes information about the type of data and more.

If we want to see the value of `a` we can simply evaluate the variable, just like we did with literals. 
The expression `a` evaluates to `1`.

<figure>
    <img src="{{"assets/img/assignment.png" | relative_url}}" alt="assignment in IDLE">
    <figcaption>Assignment to, and subsequent evaluation of, a variable</figcaption>
</figure>

>You may notice that IDLE generates no output for the assignment operation.
>This is because assignment operations evaluate to the special value `None`.
>IDLE outputs nothing when expressions evaluate to `None`
>You can confirm this by entering the `None` literal value into IDLE.
>```python
>None
>```
>Again, IDLE generates no output.
>`None` is different from `0` or `False`, it represents no value.

## Variable names

OK, `a` can be a fine name for a variable.
However, in most cases a variable should be given a meaningful name, [reflecting its usage in the code](https://peps.python.org/pep-0008/#overriding-principle).
It is good practice to use [multi_word_names](https://peps.python.org/pep-0008/#function-and-variable-names), separated with underscores as necessary, whilst keeping the [line length](https://peps.python.org/pep-0008/#maximum-line-length) of your code within ~79 characters. 

In older versions of Python, variable names were restricted to all uppercase and lowercase letters [A-Z] and underscores.
Digits were also allowed, but not for the first character.
Keywords, such as `while`, `if`, `def` and `for` are not allowed.

Since Python 3, this scheme was extended to allow unicode characters.
So this is fine:

```python
π = 3.14159
```

If you choose an invalid variable name you will get a syntax error.

```python
# SyntaxError, can't start with a number!
2π = 3.14159 * 2            

# SyntaxError, no spaces allowed!
hello world = 3.14159 * 2   

# SyntaxError, def is a keyword!
def = 5                     
```

One thing to be careful of is to avoid using the names of built-in functions or modules, especially if you are using them in your code.
The following code replaces the built-in `bool()` function with another value and so raises an error when we try to treat the `bool` name as if it still referenced the `bool()` function.

```python
bool(1)            # True
bool = 'hello'     # Overwrites bool with a new value
bool(1)            # TypeError, 'str' object is not callable
```

The error tells us that `bool` is a 'str' object and is not callable.
This is the clue we need to review the code and identify where we assign a string to the name `bool`.

> Error messages usually hold the answer or a big clue about what went wrong.
> It's very important to study the message in detail.
> See [learning from errors]({{"references/errors" | relative_url }}) for more on this.

In terms of style, there are guidelines.
The classic style guide for python code [PEP8](https://peps.python.org/pep-0008/) (the eighth Python Enhancement Proposal) suggests "lowercase with words separated by underscores as necessary to improve readability" for both variable and function names.

```python
variable_name = function_name()
```

Whereas, class names are always capitalised, using upper camel case rather than underscores at word boundaries.

```python
my_instance = MyClass()
```

We also expect spaces around operators under most circumstances.

```python
variable_name= function_name()   # No!
variable_name = function_name()  # Yes!
my_instance=MyClass()            # Bad!
my_instance = MyClass()          # Good!
```

> All moderately experienced developers will notice if you break these laws and will consider it as a style bug in your code!
> You should read [PEP8](https://peps.python.org/pep-0008/) once you have a basic grasp of python concepts as it will help you to align your style with the community and write better code.

## NameError

If we try to evaluate a variable that has not yet been created, the result is a particular error called a `NameError`.

<figure>
    <img src="{{"assets/img/name_error.png" | relative_url}}" alt="NameError in IDLE">
    <figcaption>Accessing variables without defining them first results in a NameError</figcaption>
</figure>

The error message is clear on the last line of output, *"NameError: name 'b' is not defined"*.
This error would crash our programme if we did not handle it.

## Assigning to expressions

We have seen that we need a valid variable name on the left hand side of the assignment operator (`=`).

The value on the right hand side of the assignment operator can be any valid python expression. 
This allows us to store calculated values.

For example:

```python
a = 1 + 1
a = a * 2
```

> This is a fundamental operation in programming, we can store values in memory and manipulate them in a stepwise fashion, line by line.

The right hand side is evaluated first and then the result is assigned to the variable on the left hand side.

For convenience, python also includes augmented assignment expressions which modify the value on the left side directly.

```python
a += 1
```

This is equivalent to calculating the value and then assigning.

```python
a = a + 1
``` 

This can be done with all the arithmetic operations.

<table>
    <tr><th colspan="2">augmented assignment operators</th></tr>
    <tr><td><code>+=</code></td><td>addition assignment</td></tr>
    <tr><td><code>-=</code></td><td>subtraction assignment</td></tr>
    <tr><td><code>*=</code></td><td>multiplication assignment</td></tr>
    <tr><td><code>/=</code></td><td>division assignment</td></tr>
    <tr><td><code>%=</code></td><td>modulo assignment</td></tr>
    <tr><td><code>//=</code></td><td>floor division assignment</td></tr>
    <tr><td><code>**=</code></td><td>exponentiation assignment</td></tr>
</table>
