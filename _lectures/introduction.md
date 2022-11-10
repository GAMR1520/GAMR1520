---
week: 1
lecture: 1
lang: python
title: Welcome to GAMR1520!
description: The first lecture introduces the module and covers some basic programming concepts including dynamically typed variables.
---


---
## Python as a dynamically typed language

<!-- ![python logo]({{"assets/img/python-logo.svg" | relative_url}}) -->

Python has dynamically-typed variables.
In practice, this means that variables can be changed fom one type to another.

```python
a = 1
a = 'two'
```

This lecture provides a sketch of what is happening in this simple programme.

>**TLDR;**
>There is a *lot* going on under the hood with python, even with this simple programme.
>By relinquishing some control to python, your code can be simple and expressive.

>In dynamically typed languages **type information is associated with the data**, not the variable.

---

## A simple model of computation

A basic model of a computer has memory which holds data and a CPU which manages instructions and performs calculations.

<figure>
    <img src="{{"assets/img/Von_Neumann_Architecture.svg" | relative_url}}">
    <figcaption>
        Von Neumann architecture (<a href="https://commons.wikimedia.org/w/index.php?curid=25789639">CC BY-SA 3.0</a>)
    </figcaption>
</figure>

Modern computers are said to be **computationally universal** because they can be programmed to do any computation.

---

## Instruction set

Every processor has an **instruction set** which defines the primitive operations that it can perform.
These are the building blocks from which all computer programmes are constructed.

- data handling and memory
- arithmetic and logic operations
- control flow


<figure>
    <img src="{{"assets/img/language-layers.svg" | relative_url}}">
    <figcaption>
        Higher level languages have more abstraction
    </figcaption>
</figure>

Such instructions are provided to the processor in **machine code**, the lowest-level of computer 'language', in which each instruction is represented by a unique combination of bits.

---


## Compilation

Some computer languages (such as C and Rust) are **compiled** into a format suitable for the CPU to consume directly.

<figure>
    <div class="mermaid">
    flowchart LR;
        subgraph compiled ["Compiled languages (e.g. C, Rust)"]
            source["Source code"]-->compiler[Compiler]
            compiler[Compiler]-->assembler["Assembler"]
        end
        assembler-->machinecode["Machine code"]
        input[Input]-->machinecode
        machinecode-->output[Output]
    </div>
</figure>

This compilation step can produce very efficient code through careful analysis and optimisation. 
However, it needs to be performed specifically for a given hardware architecture and typically requires the programmer to manage all the details of memory management.

>Compilers are *bootstrapped* in another language and then *self-compiled*.
>Assembly languages are said to be *assembled* rather than compiled.
Each assembly language is typically restricted to one processor architecture.

---

## Interpretation

Other languages (such as python and javascript) are compiled to an intermediate form that is **interpreted** by a special programme that actually interacts with the processor.


<figure>
    <div class="mermaid">
    flowchart LR;
        subgraph interpreted ["Interpreted languages (e.g. Python, Javascript)"]
            source["Source code"]-->compiler["Compiler"]
            compiler-->bytecode["Byte code"]
            bytecode-->virtualmachine["Virtual machine"];
        end
        input[Input]-->virtualmachine
        virtualmachine-->output[Output]
    </div>
</figure>

Interpreted languages define their own `byte code` specifications which can be used on any machine.
This makes them portable and very convenient.

>The canonical Python compiler/interpreter implementation is **CPython** (written in *C*).
>Though there are many different implementations (e.g. *IronPython*, *Jython*, *PyPy*)

---

## Memory and data types

Data in memory is usually grouped into bytes (typically an 8-bit chunk of data, but not always). 
This is great to store simple things like small integers and multiple bytes can be used to store larger integers.

Complex data can be represented in binary format through standards such as ASCII and unicode for characters and IEEE754 for floating point numbers (i.e. non-integers).

<figure>
<div class="auto-grid">
    <span>a = 97</span>
    <span>b = 98</span>
    <span>c = 99</span>
    <span>d = 100</span>
    <span>e = 101</span>
    <span>f = 102</span>
    <span>g = 103</span>
    <span>h = 104</span>
    <span>i = 105</span>
    <span>j = 106</span>
    <span>k = 107</span>
    <span>l = 108</span>
    <span>m = 109</span>
    <span>n = 110</span>
    <span>o = 111</span>
    <span>p = 112</span>
    <span>q = 113</span>
    <span>r = 114</span>
    <span>s = 115</span>
    <span>t = 116</span>
    <span>u = 117</span>
    <span>v = 118</span>
    <span>w = 119</span>
    <span>x = 120</span>
    <span>y = 121</span>
    <span>z = 122</span>
</div>
<figcaption><small>if you are interested, <a href="{{"assets/examples/week 1/ascii_data.py" | relative_url}}">here's the code for generating this table</a>.</small></figcaption>
</figure>

>This is what we mean by the **type** of data.
>All data in computers is ultimately stored as zeroes and ones but what those zeroes and ones **means** depends on what you are doing.


---

## Pointers

An important type of data is **pointer** which holds the value of a unique memory address. 
Pointers identify the location of some other data in memory.

<figure>
<div class="mermaid">
flowchart LR;
subgraph somewhere in memory
1
2
end

0x7f3b40df00f0 ---> 1
0x7f3b40df0110 ---> 2
</div>
</figure>

Every location in memory has a unique address.
32-bits of data are enough to uniquely identify a single byte within 2<sup>32</sup> bytes (4,294,967,296 or 4 GB) of memory.

---


## Statically typed variables

In languages with statically typed variables, each variable must be declared with a type that cannot change.
This code in C demonstrates the idea.
We are declaring a variable `a` of type `int` and assigning it to the value 1.
Then the code updates the value of `a`, setting it to 2.

```C
int a = 1;
a = 2;
```

>Both operations will write data into the same chunk of memory.

Since C is a statically typed language, the type of a variable cannot be changed. 

```C
int b = 1;
b = "two";
```

>This code will not compile.

---


## Dynamically typed languages

In dynamically typed languages, types are associated with values, not variables.
All data in python are represented internally as `pyObjects`.
The following code creates a pyObject of type `<int>` with the value `1`.

```python
a = 1
```

In python, variables are simply names, pointing to these complex objects.

<figure>
    <table>
        <tr><th colspan="2">pyObject</th></tr><tr><th>id</th><td>0x7fa8655e00f0</td></tr>
        <tr><th>type</th><td>&lt;class &#x27;int&#x27;&gt;</td></tr>
        <tr><th>value</th><td>1</td></tr>
        <tr><th>refs</th><td>1</td></tr>
    </table>
    <figcaption>A pyObject</figcaption>
</figure>


>The size of the integer `1` in memory is *28 bytes*.
The size of the type `<class 'int'>` is *408 bytes*.
Both are pyObjects.

---

## Inspecting a pyObject's identifier

We can view the identifier of an object in python using `built-in` function `id()`.

```python
id(a)
```
```plaintext
140361231892720
```

>In the CPython implementation, the id is a memory location.
>We can express it as a hexadecimal using an [f-string]({{"python/f-strings" | relative_url}}).
>```python
>f'{id(a):#x}'
>```
>```plaintext
>0x7fa8655e00f0
>```

---

## Inspecting object type

The `built-in` function `type` will allow us to inspect the type of `a`.
The type in this case, is the class `int`.

```python
type(a)
```
```plaintext
<class 'int'>
```

>Types also have a type!
>```python
>type(type(a))
>```
>```plaintext
><class 'type'>
>```

---

## Inspecting attributes

Depending on their type, objects sometimes have methods which we can use.
To get a list of all attributes, we can use the built-in `dir()` function.
The result can be confusing.
String objects have lots of methods.
Many of which are so-called `__dunder__` methods.

```python
dir('hello')
```

```plaintext
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

---

## Ignore the `__dunder__` methods

In python, methods (and other attributes) with *double underscores* are special.
For now, we can ignore them.

```python
[a for a in dir('hello') if not a.startswith('__')]
```

The above is a *list comprehension* which filters the list to only those without the double underscore. 
This leaves the following methods:

```plaintext
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

Notice that the `dir` method returned a `list` of `string` attribute names.
Also notice that we used the `startswith` method in the above list comprehension.

---

## String manipulation

Simple operations are easy.

```python
'hello world'.upper()
'hello world'.capitalize()
'hello world'.title()
'hello world'.split()
'hello world'.split('o')
```
```python
'HELLO WORLD'
'Hello world'
'Hello World'
['hello', 'world']
['hell', 'w', 'rld']
```

>Strings are **immutable** so these methods never change the value of a string.