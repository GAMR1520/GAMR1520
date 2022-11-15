---
week: 1
lecture: 2
lang: python
title: Python internals
description: Python code is simple because python does  lot of the work for us. This lecture delves into the details, looking at what is actually happening under the hood when we write simple programmes.
---

---

## Reminder

Even the simplest value in python is a complex object.
If we create an integer, we are instantiating an object of type `int`.
This gives us access to a lot of *magic*.

```python
a = 1
```

<figure>
    <table>
        <tr><th colspan="2">pyObject</th></tr><tr><th>id</th><td>0x7fa8655e00f0</td></tr>
        <tr><th>type</th><td>&lt;class &#x27;int&#x27;&gt;</td></tr>
        <tr><th>value</th><td>1</td></tr>
        <tr class="highlight"><th>refs</th><td>1</td></tr>
    </table>
    <figcaption>A pyObject</figcaption>
</figure>

The memory allocated to our objects is managed for us by the python interpreter.
Objects will be cleared from memory once they are no longer accessible to our programme.
This is achieved by *counting references*.

---

## Reference counting

```python
a = "hello"
```
<figure class="grid2by2">
    <div class="mermaid">
    flowchart LR;
    subgraph python variables
        a
    end
    subgraph One reference to pyObject
        hello
    end
    a -- 0x7f3b40df00f0 ---> hello
    </div>
</figure>
```python
b = a
```
<figure>
    <div class="mermaid">
    flowchart LR;
    subgraph python variables
        a
        b
    end
    subgraph Two references to pyObject
        hello
    end

    a -- 0x7f3b40df00f0 ---> hello
    b -- 0x7f3b40df00f0 ---> hello
    </div>
</figure>

---

## Reference counting

```python
a = "hello"
b = a
a = "world"
```

<figure>
    <div class="mermaid">
    flowchart LR;
    subgraph python variables
        a
        b
    end
    subgraph One reference each
        hello
        world
    end
    a -- 0x7f3b40d83f70 ---> world
    b -- 0x7f3b40df00f0 ---> hello
    </div>
</figure>

A new pyObject is created at location `0x7f3b40d83f70` containing the string `'world'`.
The variable `a` points to the new object.
The variable `b` still points to the original object.

---

## Reference counting

```python
a = "hello"
b = a
a = "world"
b = "world"
```
<figure>
    <div class="mermaid">
    flowchart LR;
    subgraph python variables
        a
        b
    end
    subgraph 'hello' has no more references
        hello
        world
    end
    a -- 0x7f3b40d83f70 ---> world
    b -- 0x7f3b40d83f70 ---> world
    </div>
</figure>

The pyObject at `0x7f3b40df00f0`, containing the string `'hello'` no longer has any references.
It will be identified by the garbage collector and the memory will be freed for use.

---


## Reference counting *implementation detail*

Simple objects like Boolean values and smaller integers are automatically reused and are not garbage collected.

```python
id(100)
id(100)
```
These would be expected to generate different identifiers.
Each statement should create a value in memory, return it's location, and immediately set the reference count to zero.

```plaintext
140397168938320
140397168938320
```

We get *the same identifier*, indicating that the same location in memory was used for both objects, even though no variable was created referencing the object.
>This is an implementation detail and should not be relied upon in code.

---

## Reference counting *implementation detail*

If we create larger objects, the behaviour is as expected.
They will be created on demand and destroyed quickly.

```python
id(1000000000)
id(1000000000)
```

Each statement creates a separate object in memory, which is discarded immediately.

```plaintext
140397166989520
140397166989936
```
>The numbers are different, this is what you should be assuming.
Data in memory are erased very quickly once no longer referenced. 


---

## Control flow

Another form of data stored in memory is the computer programme itself. 
The low-level machine-code instructions, e.g. 

>1. Read a value from memory
>1. Read another value from memory 
>1. Multiply two numbers
>1. Write the result back to memory
>1. Go back to step 2

```python
if False:
    print("never printed")
```

The CPU manages the flow through the sequence of instructions by incrementing a counter.
Some instructions can be used to change the counter value.

Python byte code is similar.

---

## A function that does nothing

Here's a function that does nothing.

```python
def nothing():
    pass
```

>the `pass` does nothing but syntactically it is necessary to avoid an `IndentationError`

This is the resulting *byte code*.

```plaintext
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      0       None
83      RETURN_VALUE    None    None
```

This loads `None` and returns it.
Functions always return a value and they will return `None` by default.

---

## A function that assigns a value to a variable

Here's something a bit more advanced (!).

```python
def assign():
    a = 1
```

...and the resulting *byte code*.

```plaintext
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      1       1
125     STORE_FAST      0       a
100     LOAD_CONST      0       None
83      RETURN_VALUE    None    None
```

It loads the constant (literal), `1` and stores it in variable `a`.
It then loads `None` and returns it.

---

## Returning a value

This function does a tiny bit more, it returns the value of `a`.

```python
def assign_and_return():
    a = 1
    return a
```

...and the resulting *byte code*.

```plaintext
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      1       1
125     STORE_FAST      0       a
124     LOAD_FAST       0       a
83      RETURN_VALUE    None    None
```

We can see, the code does the same but it loads from `a` rather than loading `None`.

---

## Taking an argument

This function receives a single argument and returns it.

```python
def return_argument(a):
    return a

```

...and the resulting *byte code*.


```plaintext
OPCODE  OPNAME          ARG     ARGVAL
124     LOAD_FAST       0       a
83      RETURN_VALUE    None    None
```

The variable `a` is already available.
So it just loads it and returns it.

---

## Addition

What happens when we add numbers?

```python
def return_argument_plus_one(a):
    return a + 1

```

The *byte code* includes a new `BINARY_ADD` code.

```plaintext
OPCODE  OPNAME          ARG     ARGVAL
124     LOAD_FAST       0       a
100     LOAD_CONST      1       1
23      BINARY_ADD      None    None
83      RETURN_VALUE    None    None
```

We load the value `a`, load the constant `1`, add them (presumably add can only take two arguments) and return.

---

## Multiple arguments

A similar example, with two arguments.

```python
def return_argument_product_minus_one(a, b):
    return a * b - 1

```

The resultant *byte code* loads the arguments `a` and `b`, multiplies them, loads the constant `1`, subtracts it and returns the result.


```plaintext
OPCODE  OPNAME          ARG     ARGVAL
124     LOAD_FAST       0       a
124     LOAD_FAST       1       b
20      BINARY_MULTIPLY None    None
100     LOAD_CONST      1       1
24      BINARY_SUBTRACT None    None
83      RETURN_VALUE    None    None

```
---

## Conditionals

A simple `if` statement, returning either `a` or `b`.

```python
def conditional_result(a, b):
    if a:
        return a
    else:
        return b
```

The *byte code* loads `a` and then includes a `POP_JUMP_IF_FALSE` code which will *jump* to code `8` if the loaded value (i.e. `a`) is `False`.
There are two paths to a return code.

```plaintext
        OPCODE  OPNAME                  ARG     ARGVAL
0       124     LOAD_FAST               0       a
2       114     POP_JUMP_IF_FALSE       4       8
4       124     LOAD_FAST               0       a
6       83      RETURN_VALUE            None    None
8       124     LOAD_FAST               1       b
10      83      RETURN_VALUE            None    None
```

---

## Alternative implementation

A neater implementation takes advantage of the `or` operator. 

```python
def conditional_result_alt(a, b):
    return a or b
```

The *byte code* is clearly more efficient, using `JUMP_IF_TRUE_OR_POP`.

```plaintext
        OPCODE  OPNAME                  ARG     ARGVAL
0       124     LOAD_FAST               0       a
2       112     JUMP_IF_TRUE_OR_POP     3       6
4       124     LOAD_FAST               1       b
6       83      RETURN_VALUE            None    None
```