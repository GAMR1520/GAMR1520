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
The variable `b` points to the new object.
The variable `a` still points to the original object.

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

---

## Reference counting *implementation detail*

Simple objects like Boolean values and smaller integers are automatically reused and are not garbage collected.

```python
id(100)
id(100)
```
These two statements, evaluated independently would be expected to generate different identifiers.
The first statement should create a value in memory, return it's location, and immediately set the reference count to zero.
The second statement is expected to do the same.

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

## Control

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

---


> Even the Boolean values `True` and `False` are objects and require 28 bytes of memory in python!
>
>Luckily there is only ever one copy of `True` and one copy of `False` stored in memory when running a python programme.
>
>The `bool` class is 408 bytes.

---


## Byte code

```python
def nothing():
    pass
```

```plaintext
OPCODE  OPNAME        ARG   ARGVAL
100     LOAD_CONST    0     None
 83     RETURN_VALUE  None  None
```

---

## More byte code

```python
def something():
    return True
```

```plaintext
OPCODE  OPNAME        ARG   ARGVAL
100     LOAD_CONST    1     True
 83     RETURN_VALUE  None  None
```

```python
def something_else():
    return 'hello'
```

```plaintext
OPCODE  OPNAME        ARG   ARGVAL
100     LOAD_CONST    1     True
 83     RETURN_VALUE  None  None
```

---

## Byte code

```python
def this_thing(a):
    return a
```

```plaintext
OPCODE  OPNAME        ARG   ARGVAL
124     LOAD_FAST     0     'a'
 83     RETURN_VALUE  None  None
```

```python
def these_things(a, b):
    return (a, b)
```

```plaintext
OPCODE  OPNAME        ARG   ARGVAL
124     LOAD_FAST     0     'a'
124     LOAD_FAST     1     'b'
102     BUILD_TUPLE   2     2
 83     RETURN_VALUE  None  None
```

---



---

## A function that does nothing

```python
def nothing():
    pass
```

```plaintext
nothing
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      0       None
83      RETURN_VALUE    None    None
```

---

## Assigning a value to a variable

```python
def assign():
    a = 1
```
```plaintext
assign
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      1       1
125     STORE_FAST      0       a
100     LOAD_CONST      0       None
83      RETURN_VALUE    None    None
```

---

## Assigning twice

```python
def assign_twice():
    a = 1
    b = 1
```
```plaintext
assign_twice
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      1       1
125     STORE_FAST      0       a
100     LOAD_CONST      1       1
125     STORE_FAST      1       b
100     LOAD_CONST      0       None
83      RETURN_VALUE    None    None
```

---

## Returning something

```python
def assign_and_return():
    a = 1
    return a
```
```plaintext
assign_and_return
OPCODE  OPNAME          ARG     ARGVAL
100     LOAD_CONST      1       1
125     STORE_FAST      0       a
124     LOAD_FAST       0       a
83      RETURN_VALUE    None    None
```

---


