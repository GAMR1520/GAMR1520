---
week: 2
title: Learning from errors
lang: python
---

>This is based on Python 3.10. 
In the recent Python release, version 3.11, error messages are upgraded to provide even more information.

Sometimes we ask python to do something that it just cannot do.

```python
a = "hello world".split()
b = a[4]
```

The first line converts our string into a 2-element list.
But when python evaluates the second line, it comes across a problem.

We are trying to access the fourth element of `a`, but there are only two elements in the list.

> Imagine your programme is getting the fourth word from some user input.
This problem could occur if the user enters too few words.

The fourth index position doesn't exist and python can't provide a reasonable result. 
So it **raises** an `IndexError`.

>Your output won't be identical to this

```plaintext
Traceback (most recent call last):
  File "the/path/to/index_error.py", line 2, in <module>
    b = a[4]
IndexError: list index out of range
```
>Whenever you see an error message like this, make sure you study it in detail.
>Notice the indentation, this indicates structure.
>If something is indented, then it 'belongs to' the level above.

## Interpreting the output

Error messages are designed to be helpful.
Though they may seem intimidating at first, they often point you directly to the exact problem in your code.

If you look at the result, you can see it actually contains only two things.

1. The *traceback*
1. The *error* itself

The traceback details exactly what the programme was doing when the error occurred, specifically which lines of code were being executed.

> For example, if the error occurs within a function 

The error gives details about what went wrong.

### The traceback

The first line of the error message describes what is coming.

```plaintext
Traceback (most recent call last):
```

The following (indented) output is a full trace of the nested context in which the error occurred.

- The traceback can be quite long.
- It is ordered with the most recent items last.

In this case, the error occurred at the top level of our programme, so there is only one entry in the traceback.

```plaintext
  File "the/path/to/index_error.py", line 2, in <module>
    b = a[4]
```
> Here, `the/path/to/index_error.py` refers to the actual location of your python file.
On my linux laptop it was very long so I replaced it with the above for simplicity.
You should see something which makes sense on your machine.

The details of this entry will be different depending on precisely how it was called.
In this case, the problem was in the specified file, on line 2.
The `<module>` indicates it was not inside a function or a class, but at the top level scope within the file.

Conveniently, the error message also includes a copy of the offending statement, which we should also find in the file on line 2.

### The error message

**The actual error message is usually the last line of the output**.

```plaintext
IndexError: list index out of range
```

Great!
This is exactly what happened.
The `IndexError` part is the generic error type.
The message `list index out of range` tells us more precisely what we did wrong.

It seems that the *list index* we used (`4`) was *out of range*.
With this very specific information, we can study the code leading up to the error to establish what happened.
In this case, we can see that the list has only two elements, so something in our logic is wrong.

## Start at the end and work backwards

If we run the file using IDLE, the output is slightly different.

```plaintext
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "the/path/to/index_error.py", line 2, in <module>
    b = a[4]
IndexError: list index out of range
```
>Don't panic if the error trace is long, just remember to *start at the end and work backwards*.

Because the IDLE programme was the actual *entry point*, we have an additional entry at the beginning of the traceback.
This is explaining exactly how the programme reached the error.
It points to line 578 in the `run.py` module in the IDLE codebase.
Apparently, the `runcode` function is what executed our code (presumably this is triggered by `f5` or the menu item within the IDLE interface).

This isn't useful for us to know because the problem was in our code.
This will often be what you see when an error occurs.
Sometimes there is a long list of context before we get to the important information.

So start at the end and read the error messages backwards.
Usually, you will find the error immediately.
In complex programmes with many nested function calls, you may need to go further up to find how the code came to raise the error and where the problem began.

## Common types of errors

### SyntaxError

If your code is syntactically incorrect then a SyntaxError is raised.

```python
a = 1 - 
```
>One minus what? 

```plaintext
  File "the/path/to/syntax_error.py", line 1
    a = 1 - 
            ^
SyntaxError: invalid syntax
```

In this case you may get a simpler trace because no code was executed.
The error was caught at *compile-time*, when the code ws parsed.

> As opposed to *run-time*, when the code was executed.

The output also may point to the error within the line using a caret (`^`).

### NameError

A `NameError` will be raised if we try to use a variable without assigning it a value first.

```python
print(hello)
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/name_error.py", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined. Did you mean: 'help'?
```
{: .small-margin}
In recent versions of python the error messages may suggest built-in functions that are close in case of a typo.

### IndexError

We have seen an index error.
Here's the same example with a longer stack trace.

```python
def b(arg):
    return a(arg).upper()

def a(arg):
    return arg[4]

data = "hello world".split()
c = b(data)
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/index_error.py", line 8, in <module>
    c = b(data)
  File "path/to/index_error.py", line 2, in b
    return a(arg).upper()
  File "path/to/index_error.py", line 5, in a
    return arg[4]
IndexError: list index out of range
```
{: .small-margin}

Notice how the stack trace shows that the error occurred when calling `b()` which then called `a()` in which the actual error happened.
This allows us to trace exactly what parameters were involved and where they came from.
In this case we would need to look to see what the value of the `data` variable was.

### KeyError

Similar to `IndexError`, when working with dictionaries we can raise a `KeyError` if we use a key that doesn't exist.

```python
data = {'hello': 'world'}
print(data['banana'])
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/key_error.py", line 2, in <module>
    print(data['banana'])
KeyError: 'banana'
```
{: .small-margin}

If a default value would be useful in your code then an approach is to use `dict.get()` which can return a default value if the requested key is not found.

```python
data = {'hello': 'world'}
print(data.get('banana', None))
```

This will print `None` because the key was not found but we provided `None` as a default value to `dict.get()`.


### TypeError

A `TypeError` indicates that you are trying to do something that cannot be done with the type of data you are using.
Simple examples include basic operations.
For example, we cannot divide a number by a string.

```python
1 / 'hello'
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/type_error1.py", line 1, in <module>
    1 / 'hello'
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```
{: .small-margin}

The error message for a `TypeError` is usually very clear.
In this case it is clearly saying that the `int` and `str` types do not support the `/` operator. 

A `TypeError` will also be raised if a function is called with the wrong number of arguments.

```python
def a():
    pass

a(1)
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/type_error2.py", line 4, in <module>
    a(1)
TypeError: a() takes 0 positional arguments but 1 was given
```
{: .small-margin}

### AttributeError

An `AttributeError` refers to the attributes of a function, class or module. 
It will be raised if code tries to access an attribute that doesn't exist.

```python
import random

random.not_a_real_attribute
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/attribute_error.py", line 2, in <module>
    random.not_a_real_attribute
AttributeError: module 'random' has no attribute 'not_a_real_attribute'
```
{: .small-margin}

If we try to call a missing attribute/method on any object, the same error will be raised.

```python
'hello'.missing_method()
```
{: .small-margin}
```plaintext
Traceback (most recent call last):
  File "path/to/attribute_error.py", line 5, in <module>
    'hello'.missing_method()
AttributeError: 'str' object has no attribute 'missing_method'
```
{: .small-margin}

Logically, python will try to access the method before it can call it.

>See more on exceptions in [the python documentation](https://docs.python.org/3/library/exceptions.html)