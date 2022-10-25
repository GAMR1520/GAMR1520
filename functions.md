---
title: User-defined functions
---

![python logo](https://www.python.org/static/community_logos/python-logo-generic.svg)

# GAMR1520: Markup languages and scripting

## User-defined functions

We have already come across built-in functions such as `len()` and `print()` as well as methods available on objects such as `list.append()`.
Here we will introduce user-defined functions using the `def` keyword.

> See also [the official python tutorial section on function definitions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) for a nice introduction.

## Calling functions with arguments

Functions and methods are known as *callable* objects which means they can be called with an argument list between parentheses.

We have seen many examples like this. 

```python
len("hello world")
```
here `len()` is the function and `'hello world'` is a single argument.

Similarly, functions and methods can be called with no arguments or multiple arguments.

```python
empty_list = list()           # No arguments
print()                       # No arguments
print('hello world')          # One argument
print('hello', 'world')       # Two arguments
'hello world'.center(20)      # One argument
'hello world'.center(20, '-') # Two arguments
```

These are all valid usage. 
Depending on the implementation, a function may enforce the number of arguments it requires, raising errors if called incorrectly. 

With these so-called *positional* arguments, the position in the argument list often determines the meaning of an arguments.

Arguments can also be optional, with default values provided.
A concrete example of positional and default arguments is the `str.center` method.

```python
original = 'middle'              # 'middle'
centered = original.center(20)   # '       middle       '
fancy = original.center(20, '=') # '=======middle======='
```

> Try printing the variables `original`, `centered` and `fancy` to see the results for yourself.

In the above case, the first argument to the `str.center()` method determines the length of the returned string.
Using the method with only one argument will pad the string with spaces by default, creating a string with the requested length.
However, by adding a second (optional) argument, we can specify the character to use for padding the result.

> See [the python documentation](https://docs.python.org/3/library/stdtypes.html#str.center) for details.

If we tried swapping the order of the arguments, we will get a `TypeError` because the first argument must be an integer.
If we tried providing an integer or a longer string as the second argument, again we would get a `TypeError` because the method requires a string exactly one character long as the second argument.


## Keyword arguments and default value

Functions and methods can also accept keyword arguments preceded by an identifier (e.g. name="hello") in the list of arguments.

> keyword arguments are always added after any positional arguments

One example of this is the `str.expandtabs()` method.
This method will return a copy of a string in which a tab characters (`\t`) are replaced by one or more spaces.
[The python documentation](https://docs.python.org/3/library/stdtypes.html#str.expandtabs) shows that this method takes a single argument, `tabsize` which has a default value of `8`.

Values for keyword arguments can be passed by position but can also be passed as keywords.
When passed by keyword, they can make function and method calls more explicit and (when good names are used) help clarify what is happening in complex code. 

Examples of basic usage are shown below.

```python
p = '<p>\n\thello\n</p>'          # An HTML paragraph
default = p.expandtabs()          # default tabsize (8)
four = p.expandtabs(4)            # Set implicitly by position
twelve = p.expandtabs(tabsize=12) # Set explicitly by keyword
```

> Try printing the variables `p`, `default`, `four` and `twelve` to see the results for yourself.

As we shall see, keyword arguments are a great a way to make function arguments optional and to provide default values.

> Now, let's look at how to define our own functions.

# Defining custom functions

Functions are a very powerful form of compound statement in python.
They are created using the `def` keyword followed by a valid function name (similar to a variable name), an argument list between parentheses, and a colon.
This is followed by a block of code, which can include a `return` statement.

Here's a simple example:

```python
function greet():
    print('hello world!')
```

When we call our function, it will print our message.

```python
greet()
```

Defining arguments is easy, just put their names (like variables) in the brackets. 

```python
def greet(name):
    print(f'hello {name}!')
```

Now we can call the function with an argument.

```python
greet('pytho')
```

If we don't pass an argument, a TypeError is raised with a useful error message.

```
TypeError: greet() missing 1 required positional argument: 'name'
```

If we pass too many arguments, a different message is provided.

```
TypeError: greet() takes 1 positional argument but 2 were given
```

We can add optional arguments with default values using keywords like this.

```python
def greet(name, greeting='hello'):
    print(f'{greeting} {name}!')
```

This allows for a more flexible function that can be used in more situations.

```python
greet('python')
greet('keyword arguments', greeting='I understand')
```

## Return statements

When we call the above function, it has a *side-effect* of printing to the console. 
We don't always want our functions to have side-effects like this.
In fact, we rarely do, especially if we want our functions to be reusable.

> Hint: We **do** want our functions to be reusable.

A return statement looks like this:

```python
return "some value"
```

> return statements are only valid inside functions

When a `return` statement is reached in a function, the code will exit the function and the function call will evaluate to whatever value was passed to the calling code.
Without any return statements, functions return `None` by default when the code block completes.

In the example above our function did not include a `return` statement. 
So we can see that it returns `None` by assigning it to a variable.

```python
result = greet('world')        # hello world!
print(f'returned: {result}')   # returned: None
```

We can rewrite the function to return the greeting string rather than printing it.

```python
def greet(name, greeting='hello'):
    return f'{greeting} {name}!'
```

Now, in our calling code, we can store the value returned by the function and do what we want with it.

```python
message = greet('world')
print(f'returned: {message}')  # returned: hello world!
```

## Complex functions

Of course, functions are not always *one-liners*.
They can be used to define more complex recipes for manipulating data.

The following code returns a formatted string representation of a list with a title.

```python
def formatted_list(items, title="list"):
    result = items[:]
    result[0:0] = [title.upper()]
    width = max([len(i) for i in result]) + 4
    result[1:1] = ['*' * width]
    result[0:0] = ['*' * width]
    result = [f"*{i.center(width)}*" for i in result]
    result.append(result[0])
    return "\n".join(result)
```

In this case, we can call the function like this.

```python
items = ["apples", "bananas", "cherries"]
fancy_output = formatted_list(items, title="fruit")
print(fancy_output)
```

This produces the following output:

```
**********
* fruit  *
*--------*
* apples *
*bananas *
*cherries*
**********
```

<blockquote class="challenge">
    <header>Time to experiment</header>
    <p>
        Spend some time understanding the above function.
    </p>
    <p>
        Look for literal values inside the functions, e.g. the additional width added to each row or the character used to create the border.
        These are good candidates for keyword parameters.
    </p>
    <p>
        Can you modify the function to add more optional parameters with default values?
    </p>
</blockquote>

# Argument decomposition