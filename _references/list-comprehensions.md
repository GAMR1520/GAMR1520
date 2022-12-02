---
week: 2
title: List comprehensions
lang: python
---

List comprehensions provide a concise way to create new lists from iterables.
For example, if we wanted to create a list like this:

```plaintext
['player_1', 'player_2', 'player_3', 'player_4', 'player_5']
```

We could use a `range()` object to create the numbers and a loop that appends strings onto a new list.

```python
result = []
for element in range(1, 6):
    result.append(f"player_{element}")
```

The above code will correctly generate our list.
However, it will also leave a reference to the variable `element` in memory with the value `4`.

We can achieve the same result more efficiently, without this side effect with a [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

```python
my_iterable = range(1, 6)

result = [f"player_{element}" for element in my_iterable]
```

The above code does exactly the same thing in one concise statement.
We specify, within square brackets, the output we want, followed by our for loop.

Here's another example.

```python
squares = [x**2 for x in range(10)]
```

Just like a `for` loop, we need an iterable (here we are using `range(10)`) and a variable (`x` in this case) to reference each element of the iterable in turn.
The first term inside the list comprehension (`x**2`) is what will be output into each element of the resulting list.

So we can do something like this.

```python
ones = [1 for _ in range(100)]
```

> By convention, the variable name `_` is chosen for variables we don't use.

In this case we are generating a list of 100 `1`'s.

List comprehensions have many advantages and can be a very powerful way to transform data iteratively, for example, we can apply a function within a list comprehension.

```python
def do_something_complex(item):
    return int(((item + 10) * 3.5)**0.5)

result = [do_something_complex(i) for i in range(10)]

print(result)
```
{: .small-margin}
```plaintext
[5, 6, 6, 6, 7, 7, 7, 7, 7, 8]
```
{: .small-margin}

The above code defines a function to do a simple calculation.
We then assign `result` to a list comprehension which iterates over `range(10)` applying the calculation to each value and returns a list containing all the results.

> The function could be very complicated, calling other code and doing much more manipulation.
> The key with list comprehensions is that they are a nice way to aggregate results into a list.
> They convert one list (or any iterable) into another list. 

### Filtering

Try adding a modified `if` clause to the end of the comprehension.
This can be used to filter an iterable, ignoring values that don't meet the specified criteria.

```python
[i for i in range(10) if i > 2]
```
{: .small-margin}

```plaintext
[3, 4, 5, 6, 7, 8, 9]
```
{: .small-margin}

We can still convert the output whilst filtering on the input.

```python
[do_something_complex(i) for i in range(10) if i > 2]
```
{: .small-margin}
```plaintext
[6, 7, 7, 7, 7, 7, 8]
```
{: .small-margin}


But we can also return the input whilst filtering on the converted data.

```python
[i for i in range(10) if do_something_complex(i) == 7]
```
{: .small-margin}
```plaintext
[4, 5, 6, 7, 8]
```
{: .small-margin}

Indeed, we can output whatever we want.
For example, we can produce a tuple of values for each filtered input.

```python
[(i, i**2) for i in range(10) if do_something_complex(i) == 7]
```
{: .small-margin}
```plaintext
[(4, 16), (5, 25), (6, 36), (7, 49), (8, 64)]
```
{: .small-margin}

If you ever need a list in which each element is calculated in some way, a list comprehension is usually the right thing to do.

```python
[list(range(1, i+2)) for i in range(3)]
[tuple(word) for word in "hello world".split()]
```

If you find yourself declaring an empty list and appending items to it within a loop, then you should consider whether a list comprehension would make your code neater and clearer.

> Sometimes complex list comprehension code can become very long and difficult to read.
> In these cases, you may want to extract a function or perhaps fall back to a simple loop.
> In the end, readability is what counts.

## Dictionary comprehensions

The same example can be modified to generate a dictionary rather than a list.
The form is intuitive, like the list comprehension.

```python
{f"player_{i}": i for i in range(1, 6)}
```

```plaintext
{
    'player_1': 1, 
    'player_2': 2, 
    'player_3': 3, 
    'player_4': 4, 
    'player_5': 5
}
```

We can also do things like swapping keys and values using `dict.items()`.

```python
data = {2: 'apples', 14: 'bananas', 23: 'cherries'}
data = {value: key for key, value in data.items()}
```

> Make sure you understand this.
Ask if your not sure.

## Set comprehensions

As you can imagine, a set comprehension is very similar.
Just use curly brackets.

```python
{do_something_complex(i) for i in range(10)}
```
{: .small-margin}
```plaintext
{8, 5, 6, 7}
```
{: .small-margin}