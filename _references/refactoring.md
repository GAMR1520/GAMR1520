---
title: Refactoring
lang: python
week: 2
---

Great code does not emerge fully formed and beautiful.
It usually starts off as a rough and limited prototype or proof-of-concept and evolves incrementally through multiple refactors.
Hopefully, each refactor improves the efficiency, functionality or readability, even just a tiny bit.
The impact of the accumulation of many small steps can be significant.
With experience, the step sizes can increase.

## An example

In a command-line application, we need to show our user lists of items.
Let's design a function to print out a list of items to the terminal.

Imagine a shopping list.

```python
shopping = ['apples', 'bananas', 'cherries']
```

A function which takes a list as input is a good starting point.
We can start by literally just printing the list, as is.

```python
def formatted_list(items):
    print(items)
```

We use the function in our application like this.

```python
shopping = ['apples', 'bananas', 'cherries']
formatted_list(shopping)
```

...and the output looks like this:

```plaintext
['apples', 'bananas', 'cherries']
```

This works!
It meets the core use case, allowing the user to see the items on their list.

But our users don't like how it looks.
The brackets are confusing.
It wraps when the list gets long.
They want each item on its own line.

So we update the function to loop over the list and print each item.

```python
def formatted_list(items):
    for item in items:
        print(item)
```

This works well in a basic way and can be used in the application.

```plaintext
apples
bananas
cherries
```

### Add a title

The scope of our application grows.
Users now have multiple lists to manage and need to know which list they are viewing.
We need to display a title clearly above the list.

So we make a small modification to our function.
The function now optionally takes a `title` argument.
We print the title before we print the list items, like this.

```python
def formatted_list(items, title="list"):
    print(title)
    for item in items:
        print(item)
```

All our existing calling code still works, but the output is a bit confusing because the title is not differentiated from the list items.

```plaintext
list
apples
bananas
cherries
```

We need to upgrade again.

### Add a separator

So we decide to add a separator between the title and the list items.

```python
def formatted_list(items, title="list"):
    print(title)
    print('-------')
    for item in items:
        print(item)
```

This helps to differentiate the title from the list.

```plaintext
list
-------
apples
bananas
cherries
```

We can also update our calling code to specify a different title.

```python
shopping = ['apples', 'bananas', 'cherries']
formatted_list(shopping, title='shopping')
```

This seems to be working well enough for our application.

```plaintext
shopping
-------
apples
bananas
cherries
```

### Edge cases

Now we have a couple of cases where it doesn't work so well.

Short items are annoying us because the separator is too long.

```plaintext
L1
-------
A
B
C
```

Long items also annoy us.

```plaintext
Shopping
-------
I need some red apples
I also need large bananas 
I need 400g of cherries
```

We decide the separator should match the longest item.

> You decide what your functions should do.

So we update the separator to adapt to the provided items.

```python
def formatted_list(items, title="list"):
    width = max([len(i) for i in items])
    print(title)
    print('-' * width)
    for item in items:
        print(item)
```

The result in the case of long items is now less distressing.

```plaintext
Shopping
-------------------------
I need some red apples
I also need large bananas
I need 400g of cherries
```

But we notice that the title length should perhaps also be taken into account.

```plaintext
My list of short items
-
A
B
C
```

So again, we upgrade the code to handle this.

```python
def formatted_list(items, title="list"):
    width = max([len(i) for i in items])
    width = max(width, len(title))
    print(title)
    print('-' * width)
    for item in items:
        print(item)
```

This upgrade has the intended impact.

```plaintext
My list of short items
----------------------
A
B
C
```

> Notice the code is getting quite long and complex through incremental additions but the calling code can remain nice and simple.

### Getting fancy

On a whim, we decide we want a border around the whole list like this.

```plaintext
**************
*  shopping  *
**************
*   apples   *
*  bananas   *
*  cherries  *
**************
```

This means we need to make each string the same length and add a single character on each end.

We need to convert this:

```plaintext
apples
```

...into something like this:

```plaintext
*   apples   *
```

So it can be integrated into the formatted output.

We know we can use `str.center()` to pad a string with spaces, and we understand [f-strings](f-strings), so we experiment with this kind of thing.

```python
string_to_pad = "hello"
padded_string = f"*{string_to_pad.center(20)}*"
```

In the above code, is doesn't matter what length the original string is, it will be neatly converted to the specified width and have extra characters added.

> Experimenting with a simplified example like this (a *proof-of-concept*) can be helpful when planning an upgrade.
> The proof-of-concept only deals with the change we want to see, not the whole function.
> Once we have a proof-of-concept working, we can integrate it into our code.

We can attempt a basic integration of this idea into our function by upgrading the main print statement.

```python
def formatted_list(items, title="list"):
    width = max([len(i) for i in items])
    width = max(width, len(title))
    print(title)
    print('-' * width)
    for item in items:
        print(f"*{item.center(width)}*") # <- here
```

The output is not quite what we wanted, but we can see this just needs a bit of work.

```plaintext
shopping
--------
* apples *
*bananas *
*cherries*
```

We can notice a few issues:

- The title and separator need to be padded like the items.
- We need a top and bottom border too.
- We need to add a bit more padding around everything.

> We will leave the first issue until last, simply because it requires more explanation.

We think horizontal borders will be easy to add so we test a little *proof-of-concept* example in the python interpreter.

```python
print('*' * width + 2)
```

We want to add two extra characters to the width so the border matches the items.
But our code produces an error.

```plaintext
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

This is because the `*` operator has precedence over the `+` operator.

>Python computes the `*` operation first, giving something like this.
>```python
>print('***********' + 2)
>```
>It thinks we are trying to add an integer to a string.

We can add brackets to cause the addition to happen first.

```python
print('*' * (width + 2))
```

Integrating this with our function is simple enough.

```python
def formatted_list(items, title="list"):
    width = max([len(i) for i in items])
    width = max(width, len(title))
    print('*' * (width + 2))               # <- here
    print(title)
    print('-' * width)
    for item in items:
        print(f"*{item.center(width)}*")
    print('*' * (width + 2))               # <- and here
```

> This code is repeated, should we refactor it?
> Yes, probably.
> But we can live with it for a short while if we promise to do it later.
> A *prototype* solution like this can be messy as long as it is tidied up.

The result is still incomplete, but we can see we are making progress.

```plaintext
**********
shopping
--------
* apples *
*bananas *
*cherries*
**********
```

Adding a bit more padding is easy, we can just add a fixed amount to the width calculation.
In this case I've added 4 so we get two characters of additional padding on each side.

```python
def formatted_list(items, title="list"):
    width = max([len(i) for i in items])
    width = max(width, len(title)) + 4  # <- here
    print('*' * (width + 2))
    print(title)
    print('-' * width)
    for item in items:
        print(f"*{item.center(width)}*")
    print('*' * (width + 2))
```

The result is looking encouraging.

```plaintext
**************
shopping
------------
*   apples   *
*  bananas   *
*  cherries  *
**************
```

The last thing to do is to add the border around the title and the separator.
This is actually pretty easy.
We can add the `str.center()` logic for the title and replace the separator with similar code to the top and bottom borders.

```python
def formatted_list(items, title="list"):
    width = max([len(i) for i in items])
    width = max(width, len(title)) + 4
    print('*' * (width + 2))
    print(f"*{title.center(width)}*")   # <- here
    print('*' * (width + 2))            # <- and here
    for item in items:
        print(f"*{item.center(width)}*")
    print('*' * (width + 2))
```

The result looks pretty good.

```plaintext
**************
*  shopping  *
**************
*   apples   *
*  bananas   *
*  cherries  *
**************
```

> Try running the function with different inputs.
> It works pretty well, but there are limits.

### Don't repeat yourself

Now we have working code, we can look at it with a critical eye and identify opportunities to improve.
One obvious issue with this code is that it contains a lot of repetition.
For example, the character `*` is referenced seven times as a literal string.
We can move this into another keyword argument (`ch`) and provide a default value.

```python
def formatted_list(items, title="list", ch='*'):
    width = max([len(i) for i in items])
    width = max(width, len(title)) + 4
    print(ch * (width + 2))
    print(f"{ch}{title.center(width)}{ch}")
    print(ch * (width + 2))
    for item in items:
        print(f"{ch}{item.center(width)}{ch}")
    print(ch * (width + 2))
```

With this, our existing code still works, but we can now optionally specify a character for the border.

```python
shopping = ['apples', 'bananas', 'cherries']
formatted_list(shopping, title="shopping", ch='^')
```

We also repeat the code `ch * (width + 2)` three times.
This represents a horizontal line, so let's assign it to a variable `hline` and reuse it.

```python
def formatted_list(items, title="list", ch='*'):
    width = max([len(i) for i in items])
    width = max(width, len(title)) + 4
    hline = ch * (width + 2)
    print(hline)
    print(f"{ch}{title.center(width)}{ch}")
    print(hline)
    for item in items:
        print(f"{ch}{item.center(width)}{ch}")
    print(hline)
```

Fantastic.
The code still works.

### A bigger refactoring

Now the final obvious example of repetition is the use of `str.center()`.

These two lines are very similar.

```python
print(f"{ch}{title.center(width)}{ch}")
print(f"{ch}{item.center(width)}{ch}")
```

So how can we refactor the code to remove this repeated logic?

One way is to step back and think about generating the output in two steps.

1. Create a list with each line of output, including the horizontal lines.
1. Loop over the list and apply the vertical lines to each row as we print them.

This will change our code radically and needs to be carefully planned.

The first thing we need to do is to remove any code that prints our `hline` or `title`.
These will be added to the list and printed in the loop.

```python
def formatted_list(items, title="list", ch='*'):
    width = max([len(i) for i in items])
    width = max(width, len(title)) + 4
    hline = ch * (width + 2)
    for item in items:
        print(f"{ch}{item.center(width)}{ch}")
```

This simplifies the code a bit, but we've lost our title and most of the border.

```plaintext
*   apples   *
*  bananas   *
*  cherries  *
```

> Oh no, it's broken!
> Don't worry, we are about to fix it.
> Sometimes we need a bit of creative destruction.
> Just remember to save a copy of your code before you make drastic changes.
> Or use a version control system.

The main update is to add in all the elements we want to print into the loop.
Consider a new list like this.

```python
result = [hline, title, hline] + items + [hline]
```

We are using the `+` operator on three lists which concatenates them into a new list.

We must also reduce the `hline` back down to `width` characters rather than `(width + 2)`.
Then we can loop over this list and add the padding and vertical border characters.

Integrate it into your code like this.

```python
def formatted_list(items, title="list", ch='*'):
    width = max([len(i) for i in items])
    width = max(width, len(title)) + 4
    hline = ch * width
    result = [hline, title, hline] + items + [hline]
    for item in result:
        print(f"{ch}{item.center(width)}{ch}")
```

This works beautifully and is looking a lot simpler than our previous working version.

But we can simplify the width calculation a bit further.
Currently we calculate the width in two steps.
First, we use a [list comprehension]({{"references/list-comprehensions" | relative_url}}) to get the lengths of each item and take the max value. 
Then we compare this with the length of the title and add four.

We can easily merge the items with the title within the list comprehension.
This will allow us to reduce the calculation to one line.

```python
width = max([len(i) for i in items + [title]]) + 4
```

>If we thought this was not clear enough, we could expand it more usefully like this.
>
>```python
>widths = [len(i) for i in items + [title]]
>width = max(widths) + 4
>```
>
>This decomposes the logic more clearly than the original.

### One final refactor

We realise that our function should probably not be doing the printing.
We want the formatted string to be returned by the function so the calling code can decide what to do with it.

This is now fairly easy.
We can use a list comprehension to apply the `str.center()` and `f-string` transformation to each item in the `result` list.
Then finally, we use the `str.join()` method to connect all the elements with a *newline* character.

```python
def formatted_list(items, title="list", ch='*'):
    width = max([len(i) for i in items + [title]]) + 4
    hline = ch * width
    result = [hline, title, hline] + items + [hline]
    result = [f"{ch}{i.center(width)}{ch}" for i in result]
    return "\n".join(result)
```

The end result is a function with a lot going on.
Most of the lines in the function are doing fairly complex work.
The output is exactly as intended.

## Conclusion

Code can start simple and develop incrementally.
In fact, this is very often a suitable way to solve a coding problem.
Start by solving the problem in the most basic and naive way possible and incrementally work towards a more sophisticated solution.

As a rough plan, repeat these steps until its *"good enough"* for you.

1. Start with a simple proof-of-concept (ask, *can* this approach work?)
1. Produce a very simple prototype
1. Check the result (ask, *does* this approach work?)
1. Consider possible improvements

It can be daunting to consider creating your own functions.
Using this approach can help to begin the process of writing code.

> When presented with complex and advanced looking code provided by more experienced developers.
> Remember that the code may have begun life as a much simpler prototype solution that was incrementally improved to become more sophisticated over several iterations.