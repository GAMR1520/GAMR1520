---
week: 2
title: User-defined functions
lang: python
---

We have already come across built-in functions such as `len()` and `print()` as well as methods available on objects such as `list.append()`.
Here we will introduce user-defined functions using the `def` keyword.

> See also [the official python tutorial section on function definitions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) for a nice introduction.

{% include toc.md %}

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

> The comments are indicating the results here. 
Try printing the variables `original`, `centered` and `fancy` to see the results for yourself.

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

> Again, the comments are indicating the results.
Try printing the variables `p`, `default`, `four` and `twelve` to see the results for yourself.

As we shall see, keyword arguments are a great a way to make function arguments optional and to provide default values.

> Now, let's look at how to define our own functions.

## Defining custom functions

Functions are a very powerful form of compound statement in python.
They are created using the `def` keyword followed by a valid function name (similar to a variable name), an argument list between parentheses, and a colon.
This is followed by a block of code, which can include a `return` statement.

Here's a simple example:

```python
def greet():
    print('hello world!')
```

We can now access the function by name.
The act of defining a function creates a variable of type `function`.

```python
print(greet)
print(type(greet))
```
{: .small-margin}
```plaintext
<function greet at 0x7f7a8208fd90>
<class 'function'>
```
{: .small-margin}

When we call our function, it will print our message.

```python
greet()
```

Choosing good names is famously one of the hardest problems in programming. 

> "There are only two hard things in Computer Science: cache invalidation and naming things."
> [*Phil Karlton*](https://www.karlton.org/2017/12/naming-things-hard/)

Function names will become embedded in our programmes.
We are effectively creating our own extensions to the language.
When we read our code it should be obvious what we are doing.

Obviously we need to avoid clashes, i.e. don't name your function `print()` or `def()`.


> In terms of code style, we should be using lower-case letters and can use underscores as necessary (following [PEP8](https://peps.python.org/pep-0008/#function-and-variable-names)).

### Arguments

Defining arguments is easy, just put argument names (like variables) in the brackets. 

```python
def greet(name):
    print(f'hello {name}!')
```

Now we can call the function with an argument.

```python
greet('python')
```

The function can take our argument and use it to generate the output.

```plaintext
hello python!
```

If we don't pass an argument, a TypeError is raised with a useful error message.

```python
greet()
```
{: .small-margin}
```plaintext
TypeError: greet() missing 1 required positional argument: 'name'
```
{: .small-margin}

If we pass too many arguments, a different message is provided.
```python
greet('python', 3)
```
{: .small-margin}
```plaintext
TypeError: greet() takes 1 positional argument but 2 were given
```
{: .small-margin}

### Optional/default arguments

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
{: .small-margin}
```plaintext
hello python!
I understand keyword arguments!
```
{: .small-margin}

### Return statements

When we call the above function, it has a *side-effect* of printing to the console.
For more direct interaction with functions we can take advantage of the fact that function calls resolve to a value that can be used in our programme.

If we add `return` statements into a function, we can *return* a value for use by the calling code. 

Return statements look like this.

```python
def my_function():    
    return 'some value'
```

> `return` statements are only valid inside functions.
You can add as many as you need but be careful because code after a `return` statement will not be reached.

When a `return` statement is reached in a function, the code will exit the function back to the calling code and the function call will evaluate to whatever value was passed to the return statement.

In the `greet` function above, we did not include a `return` statement. 
Without any `return` statements, functions return `None` by default when the code block completes.

We can assign the function call to a variable.

```python
result = greet('world')
print(f'returned: {result}')
```
{: .small-margin}
```plaintext
hello world!
returned: None
```
{: .small-margin}

As expected, the code prints `'returned: None'`.

We can rewrite the function to return the greeting string rather than printing it.

```python
def greet(name, greeting='hello'):
    return f'{greeting} {name}!'
```

Now, in our calling code, we can store the value returned by the function and do what we want with it.

```python
message = greet('world')
print(f'returned: {message}')
```
{: .small-margin}
```plaintext
returned: hello world!
```
{: .small-margin}

Functions are a powerful feature in any programming language.
We can think of them as tools for extending the language with new capabilities.
Extracting common operations into simple functions can make code more efficient, more maintainable and easier to read.

## More complex functions

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


## Argument unpacking

We have covered the basics of functions in python but there is some additional useful syntax it's worth knowing about.

> The following covers advanced techniques for developing intuitive and useful functions.
Don't worry if this is confusing.
You can skip it if this is the first time you are working with functions.
You can come back to this page when you have some more experience of writing code and hopefully it will make more sense.

In particular we can `pack` and `unpack` arguments.
In normal code, outside of functions, you might see this kind of thing:

```python
a = 1, 2
```

Here `a` becomes the tuple `(1, 2)`.

An extension of this:

```python
a, b = 1, 2
```

Here, both sides of the assignment operator are comma-separated and the same length.
On the left we have two variables and on the right we have two literals.
So `a` becomes `1` and `b` becomes `2`.
This *just works* and can be useful, but can also be less readable so use it sparingly.

One case where it is extremely useful is if we want to swap the values of variables.

```python
a, b = b, a
```

Again, this *just works*.
The values of the variables are swapped.

We can also specify that multiple values should be packed into a single variable as a list by using an asterisk (`*`), like this.

```python
a, *b = 1, 2, 3
```

This results in `a` taking the value `1` and `b` becomes the list `[2, 3]`.

and finally, we can also do this:

```python
a, *b, c = 1, 2, 3, 4
```
In which case, the first and last values (`1` and `4`) are allocated to `a` and `c` respectively and the remaining values (`2` and `3`) are packed into `b` as a list.

A similar approach can be taken with function arguments.

### Arbitrary argument lists

> see also [the python documentation](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)

You will sometimes see code like this with an asterisk before an argument:

```python
def greet(*names):
    for name in names:
        print(f'hello {name}')

greet("python", "functions", "arguments")
```

In this case the asterisk indicates that all positional arguments passed into the function should be merged into a single tuple containing all the values in order.
In the example, the argument `names` will contain a tuple containing the three positional arguments provided.

```plaintext
hello python
hello functions
hello arguments
```

So no matter how many positional arguments are provided, they will be merged into a single tuple which will preserve the order in which the arguments were provided.
Our function can access the third argument using `names[2]`, but this may raise an `indexError` since there is no guarantee that the calling code provided three arguments.

We can see the tuple in the following example:

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
> We can add as many positional arguments as we want to print.
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
Going back to the `greet()` and `print_argument_details()` functions we defined earlier.


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

### Keyword argument packing

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
{: .small-margin}
```plaintext
python is amazing!
mind is blown!
<class 'dict'> {'python': 'amazing', 'mind': 'blown'}
```
{: .small-margin}


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
{: .small-margin}
```plaintext
0 0 0 default default default
0 0 0 new value default default
0 0 0 default new value default
0 0 0 default default new value
0 0 0 new value new value new value
```
{: .small-margin}

So, functions are really nice.
They are very useful for encapsulating a reusable recipe that may be used in multiple places.