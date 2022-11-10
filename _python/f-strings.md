---
title: Python string formatting
week: 1
---

Consider this simple programme.

```python
name = input('Enter your name: ')
print(name + ' has ' + str(len(name)) + ' letters.')
```

This is a bit complicated.
Concatenating strings like this is not good practice.
For efficiency and clarity.
We can improve it by using the so-called f-string formatting system.

F-strings allow python expressions to be embedded within strings.
We create them by adding an `f` character *before* the first quotation mark and placing python expressions inside the string within curly braces.

```python
name = input('Enter your name: ')
greeting = f'Hello {name}'
print(greeting)
```

A more complicated example.

```python
name = input('Enter your name: ')
print(f'Hello {name}, your name has {len(name)} letters.')
```

This is much more intuitive to read than the concatenated example above.

> Interpolated expressions in f-strings are automatically converted to strings.
