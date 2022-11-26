---
title: Python string formatting
week: 2
lang: python
---

Python strings are powerful objects with lots of capabilities and methods to learn.
The [main documentation on string methods](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#string-methods) is long and may be difficult to navigate at first.

This is a quick introduction to the some useful string formatting approaches.

## Formatted string literals (*f-strings*)

Before we look at string methods, we should discuss [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) or *f-strings*.
For many string formatting operations, f-strings are perfect.

Consider this simple programme.

```python
name = input('Enter your name: ')
print(name + ' has ' + str(len(name)) + ' letters.')
```

This is a bit complicated.
The code relies on concatenating strings using the `+` operator.
Concatenating strings like this is not good practice.
For both efficiency and clarity.
We can improve it by using the so-called *f-string* formatting system.

*F-strings* allow python expressions to be embedded within string literals.
We create them by adding an `f` character *before* the first quotation mark and placing python expressions inside the string within curly braces.

Using f-strings, the above code can be rewritten

```python
name = input('Enter your name: ')
print(f"{name} has {len(name)} letters.")
```

> We no longer need to use `str()` because interpolated expressions in f-strings are automatically converted to strings.

Notice how much easier the code is to read.

```python
name = input('Enter your name: ')
greeting = f'Hello {name}'
print(greeting)
```

A slightly more complicated example.

```python
name = input('Enter your name: ')
print(f'Hello {name}, your name has {len(name)} letters.')
```

This is much more intuitive to read than the concatenated example above.

We can use formatting codes with *f-strings* by adding extra codes inside the curly brackets.
For example, adding an `=` symbol after a variable will output a handy debug message.

```python
msg = 'hello world'
print(f'{msg=}')
```
```plaintext
msg='hello world'
```

> Read more about formatting codes that can be used in f-strings in [the python documentation](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals).

## Common string methods

Strings, like all values, are objects.
String objects have *a lot* of methods we can use to generate new strings.
These methods are built into the string object itself.

> Strings are immutable so its not possible to *change* the value of a particular string.
All the following methods will generate new strings, based on the current object.

### `upper()`

We can generate an uppercase version of the string using the `upper()` method.

```python
'hello world'.upper()
```
```plaintext
HELLO WORLD
```

> `lower()` has the equivalent effect, converting to lowercase. 

### `title()`

We can generate an titlecase version of the string using the `title()` method.
This capitalises each word.

```python
'hello world'.title()
```
```plaintext
Hello World
```

### `capitalize()`

We can generate a capitalized version of the string using the `capitalize()` method.
This capitalises only the first word.

```python
'hello world'.capitalize()
```
```plaintext
Hello world
```

### `center()`

The `center()` method generates a new string with a given length.
The new string contains the original string, centered and padded by the specified character.

```python
'hello world'.center(20, "=")
```
```plaintext
====hello world=====
```

In this case, we need to specify arguments.
The first argument is how long the string should be (in characters).
The second argument is the character to use for padding.
This is an optional argument, the default value used if no argument is provided is a space.

>This may not seem very useful when we are working with literals.
>The value is more apparent when we are working with variables in memory.

<figure>
    <img src="{{"assets/img/string-methods.png" | relative_url}}" alt="string methods in IDLE">
    <figcaption>strings are objects</figcaption>
</figure>

>In the figure we can see that these methods can be applied to convert unknown strings into the format we may need to e.g. report back to the user or conduct comparisons.

## Testing strings

There are a number of methods which will return Boolean values.

The `istitle()`, `isupper()` and `islower()` methods will return `True` if the string is titlecase, uppercase or lowercase respectively.

```python
print('hello world'.istitle())
print('hello world'.isupper())
print('hello world'.islower())
```
```plaintext
False
False
True
```

Similarly, `endswith()`, `startswith()`, `isalpha()`, `isnumeric()` and `isalnum()` will test whether a string has certain properties.

```python
print('hello world'.endswith('orld'))
print('hello world'.startswith('hel'))
print('hello world'.isalpha())
print('hello world'.isnumeric())
print('hello world'.isalnum())
```
```plaintext
True
True
False
False
False
```

> `isalpha()` returns `False` due to the space character.
`isalnum()` returns `False` because both `isalpha()` and `isnumeric()` return `False`.

### Splitting

The `split()` method will divide the string on a specified character and return a list of the fragments.