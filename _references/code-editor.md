---
week: 1
title: Get a proper text editor
---

Using IDLE for python is OK, but its much more convenient to use a modern text editor.
When we move on to javascript, IDLE will no longer suffice.
So you should start using an editor that can handle both languages.
There are many to choose from.

In the last few years, (since the [sunsetting](https://github.blog/2022-06-08-sunsetting-atom/) of [atom](https://github.com/atom/atom)), my editor of choice has become [vscode](https://code.visualstudio.com/). 
Though it doesn't matter which editor you choose (if you have a favourite, then use it), I am currently recommending *vscode* for this module.

VSCode should already be installed on the lab machines (perhaps identified as *visual studio code*), though it can be installed if not.

> Download and installation should be fairly simple, just [follow the instructions](https://code.visualstudio.com/).
> You may also need to [install python](https://www.python.org/downloads/) on your personal machine.
> If so, get the latest stable version or a version that matches the lab if you prefer.

## Create a file

Once installed, use the *File -> Open folder* option to open your *GAMR1520-labs* folder.
The folder contents should appear on the left panel.

Select a script to edit or create a new one.

> You can close all other tabs

![hello world script in vscode]({{"assets/img/vscode/hello_world.png" | relative_url }})

The editor should detect you are using python and offer to install the python extensions.
Make sure you accept this and get the python tools installed as this will enable some powerful features that will help you when editing code.

Once the installation is complete, you can try it out by opening or creating a *hello_world.py* file and entering/editing the code.

> If it already exists, delete the code and write it again.

![intellisense in vscode]({{"assets/img/vscode/intellisense.png" | relative_url }})

The editor will make suggestions as you type based on its knowledge of python.
If you type `print` then the python documentation for the `print()` function is displayed as you type.
This extremely useful for discovering new parts of the language as well as looking up the precise syntax, argument options and meanings without resorting to the python documentation directly.
It is certainly a huge upgrade from using IDLE.

## Executing code

There are two main ways to execute python code.
If you are using vscode then you can press *Ctrl + F5* to *run without debugging*.
This will execute the current file in a terminal.

![terminal in vscode]({{"assets/img/vscode/terminal.png" | relative_url }})

> See where I have highlighted the output in the terminal panel

The more generally applicable way to execute code is to simply run the `python` executable via a command line interface such as *powershell*, *cmd* or *git bash* which are all installed on the lab machines.


Use `cd` to change directory to a location where you have saved python scripts.

```console
cd H:\GAMR1520\GAMR1520-labs\lab-1.1\
```

> Your path might be different

Run the `python` programme with the filename as the only argument.

```console
python hello_world.py
```
```plaintext
hello world
```

> On a mac or linux machine the terminal responds to the same commands, although it may be *python3* rather than *python*.
> ![linux terminal]({{"assets/img/vscode/linux_terminal.png" | relative_url }})


It doesn't matter which approach you choose but you will need to get familiar with executing python files.

> If you are stuck and/or confused then this page doesn't explain *your* situation well enough. 
Let me know and I will update the page.