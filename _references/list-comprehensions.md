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
my_iterable = range(1, 6)

result = []
for element in my_iterable:
    result.append(f"player_{element}")
```

The above code will correctly generate our list.
However, it will also leave a reference to the variable `element` in memory with the value `4`.

We can achieve the same result more efficiently, without this side effect with a list comprehension.

```python
my_iterable = range(1, 6)

result = [f"player_{element}" for element in my_iterable]
```

The above code does exactly the same thing in one concise statement.
We specify, within square brackets, the output we want, followed by our for loop.

This has many advantages and can be very powerful, for example, we can apply a function within a list comprehension.

```python
def do_something_complex(item):
    return int(((item + 10) * 3.5)**0.5)

result = [do_something_complex(i) for i in range(10)]

print(result)
```

```plaintext
[5, 6, 6, 6, 7, 7, 7, 7, 7, 8]
```

The above code defines a function to do a simple calculation.
We then assign `result` to a list comprehension which iterates over `range(10)` applying the calculation to each value and returns a list containing all the results.

### Filtering

Try adding a modified `if` clause to the end of the comprehension.
This can be used to simply filter an iterable.

```python
[i for i in range(10) if i > 2]
```
```plaintext
[3, 4, 5, 6, 7, 8, 9]
```

We can still convert the output whilst filtering on the input.

```python
[do_something_complex(i) for i in range(10) if i > 2]
```
```plaintext
[6, 7, 7, 7, 7, 7, 8]
```

But we can also return the input whilst filtering on the converted data.

```python
[i for i in range(10) if do_something_complex(i) == 7]
```
```plaintext
[4, 5, 6, 7, 8]
```

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

## Set comprehensions

As you can imagine, a set comprehension is very similar.

```python
{do_something_complex(i) for i in range(10)}
```
```plaintext
{8, 5, 6, 7}
```
