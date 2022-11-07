---
week: 1
lecture: 1
lang: python
title: Welcome to GAMR1520!
description: The first lecture introduces the module and covers some basic programming concepts including dynamically typed variables.
---


---
# Python as a dynamically typed language

![python logo]({{"assets/img/python-logo.svg" | relative_url}})

This is a brief introduction to the concepts necessary to understand what it means for a language to have dynamically typed variables.

>TLDR;
>Computers will do *exactly* what they are told.
>Its important to understand how to tell them what you want them to do.
>But the most difficult part is knowing what you want them to do in the first place.


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

<figure>
    <img src="{{"assets/img/language-layers.svg" | relative_url}}">
    <figcaption>
        Higher level languages have more abstraction
    </figcaption>
</figure>

Such instructions are provided to the processor in **machine code**, the lowest-level of computer 'language', in which each instruction is represented by a unique combination of bits.


---

## Memory and data types

Data in memory is usually grouped into bytes (typically an 8-bit chunk of data, but not always). 
This is great to store simple things like small integers and multiple bytes can be used to store larger integers.

Complex data can be represented in binary format through standards such as ASCII and unicode for characters and IEEE754 for floating point numbers (i.e. non-integers).

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

>This is what we mean by the **type** of data.
>All data in computers is ultimately stored as zeroes and ones but what those zeroes and ones **means** depends on what you are doing.

---

### Pointers

An important type of data is **pointer** which holds the value of a unique memory address. 
Pointers identify the location of some other data in memory.

<figure>
    <div class="mermaid">
    flowchart RL;
        subgraph data
            direction LR
            0b00000000~~~0b00000001;
        end
        subgraph variables
            direction LR
            a-->0b00000000;
            b-->0b00000001;
            c-->0b00000001;
        end
    </div>
</figure>

32-bits of data are enough to uniquely identify a single byte within 2<sup>32</sup> bytes (4,294,967,296 or 4 GB) of memory.
Every location in memory has a unique address.

---

### Control

Another form of data stored in memory is the computer programme itself. 
The low-level machine-code instructions.

>e.g. read a value from memory, multiply two numbers and write the result back to memory.


```python
a = True
if a:
    a = not a
print(a)
```

The CPU manages the flow through the sequence of instructions by incrementing a counter.
Some instructions can be used to change the counter value.

---

> When we talk about memory and computation its useful to think in terms of small blocks of data, a few zeros and ones.
However, the modern reality is a vast capability.
As a reference point, a Sony Playstation 5 has 16 billion bytes of RAM and can perform over 10 trillion floating point operations per second.

