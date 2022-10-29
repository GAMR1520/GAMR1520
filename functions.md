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
len('hello world')
```
here `len()` is the function and `'hello world'` is a single argument.

Similarly, functions and methods can be called with no arguments or multiple arguments.

```python
empty_list = list()
print()
print('hello world')
print('hello', 'world')
'hello world'.center(20)
'hello world'.center(20, '-')
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
def greet():
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
greet('python')
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
For more direct interaction with functions we can take advantage of the fact that function calls resolve to a value that can be used in our programme.

If we add `return` statements into a function, we can *return* a value for use by the calling code. 

Return statements look like this.

```python
return 'some value'
return 1000000
return
```

> return statements are only valid inside functions.
> Without any return statements, functions return `None` by default when the code block completes.

When a `return` statement is reached in a function, the code will exit the function back to the calling code and the function call will evaluate to whatever value was passed to the return statement.

In the example above our function did not include a `return` statement. 
We can assign the function call to a variable.

```python
result = greet('world')        # hello world!
print(f'returned: {result}')   # returned: None
```

As expected, the code prints `'returned: None'`.

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

Functions are a powerful feature in any programming language.
We can think of them as tools for extending the language with new capabilities.
Extracting common operations into simple functions can make code more efficient, more maintainable and easier to read.

## Complex functions

Of course, functions are not always *one-liners*.
They can be used to define more complex recipes for manipulating data.

The following code returns a formatted string representation of a list with a title.

```python
def formatted_list(items, title='list'):
    width = max([len(i) for i in items + [title]]) + 4
    hline = '*' * width
    result = [hline, title, hline] + items + [hline]
    result = [f'*{i.center(width)}*' for i in result]
    return "\n".join(result)
```

Internal to the function we go through several steps to generate the formatted output.

- calculate a width for the list based on the longest element (including the title) plus four characters (to add two spaces on each side of the longest element)
- define a horizontal line of the correct length
- create a list of each row in the output including the title and several formatted rows 
- format each element in the list to have the given width, adding extra formatting to the edges
- return the elements as a string, joined with a newline character

> Study the function and play with it.
> Don't worry if it seems complex. 
> This code evolved over time.
> For details, see the [refactoring](refactoring) page.

In this case, we can call the function like this.

```python
items = ['apples', 'bananas', 'cherries']
title = 'fruit'
fancy_output = formatted_list(items, title=title)
print(fancy_output)
```

This produces the following output:

```plaintext
**************
*   fruit    *
**************
*   apples   *
*  bananas   *
*  cherries  *
**************
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
    <p>
        Try to generate something like this with a function call.
    </p> 
    <pre><code class="language-plaintext">++++++++++++++++++++++++++++++++
+            fruit             +
++++++++++++++++++++++++++++++++
+            apples            +
+           bananas            +
+           cherries           +
++++++++++++++++++++++++++++++++</code><pre>   
</blockquote>

# Special cases

We have covered the basics of functions in python but there is some additional useful syntax it's worth knowing about.
You will sometimes see code like this with an asterisk before an argument:

```python
def greet(*names):
    for name in names:
        print(f'hello {name}')

greet("python", "functions", "arguments")
```

In this case the asterisk indicates that all positional arguments passed into the function should be merged into a single tuple containing all the values in order.
In the example, the argument `names` will contain a tuple containing the three positional arguments provided.
Since the tuple is a sequence, we can access values at a given index or simply loop over them all.

We can see more detail in the following example:

```python
def print_argument_details(*args):
    print(type(args), args)

print_argument_details('hello', 'world', 15, True)
```

This produces the following output:

```plaintext
<class 'tuple'> ('hello', 'world', 15, True)
```

> Notice that the `print()` function makes use of this feature.
> We can add as many items as we want to print.
> ```python
> print(1, 2, 3)
> ```

A similar but opposite result can also be achieved when calling functions or methods.
We can pass a tuple into a function prepended with an asterisk to unpack the tuple into separate arguments

```python
args = (20, '+')
print('hello world'.center(*args))
```

Our `args` tuple is split into two arguments.

Try it without the asterisk.

```python
args = (20, '+')
print('hello world'.center(args))
```

This generates an error because the first argument should be an integer, but we passed a tuple.

We can in fact pass any iterable value in this way.
Going back to the `greet()` function we defined earlier.


```python
greet(*"hello")
print_argument_details(*'hello')
```

This decomposes the string into individual characters which are then passed as separate arguments and recombined into the tuple that is processed by the functions. 

```plaintext
hello h!
hello e!
hello l!
hello l!
hello o!
<class 'tuple'> ('h', 'e', 'l', 'l', 'o')
```

The `**` operator works in a similar fashion to convert between keyword arguments and dictionaries.
We can construct a similar set of examples as follows.

```python
def greet2(**things):
    for name in things:
        print(f'{name} is {things[name]}!')

def print_kwargument_details(**kwargs):
    print(type(kwargs), kwargs)

greet2(python="amazing", mind="blown")
print_kwargument_details(python="amazing", mind="blown")
```

This can be useful when passing unknown optional arguments through a function to another function.

```python
def complicated(a, b, c, d='default', e='default', f='default'):
    print(a, b, c, d, e, f)


def simple(**kwargs):
    complicated(0, 0, 0, **kwargs)
```

In the above code we have created a new, simpler version of the complicated function that can be called with no arguments, but it still retains the optional arguments just like the original.

```python
simple()
simple(d='new value')
simple(e='new value')
simple(f='new value')
simple(d='new value', e='new value', f='new value')
```

