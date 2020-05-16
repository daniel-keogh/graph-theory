# Graph Theory Overview

## Contents

- [Introduction](#introduction)
    - [What are Regular Expressions](#what-are-regular-expressions)
    - [Non Deterministic Finite Automata](#non-deterministic-finite-automata)
- [Run](#run)
    - [Installing Python](#installing-python)
    - [Running the Program](#running-the-program)
    - [Installing with pip](#installing-with-pip)
- [Testing](#testing)
- [Algorithms](#algorithms)
    - [Thompson's Construction](#thompsons-construction)
    - [Shunting Yard Algorithm](#shunting-yard-algorithm)
- [References](#references)

## Introduction

The purpose of this document is to provide an explanation of the project work contained in this repository, pitched at students in the year below.

This repository contains a program written in the Python programming language that than can be used to determine if a regular expression
matches a given string of text. If the string is a match, `True` will be printed to the console, and `False` will be printed otherwise.

### What are Regular Expressions

TODO:

### Non Deterministic Finite Automata

## Run

### Installing Python

In order to get started you'll first need to have access to Python.

> Python is an interpreted, interactive, object-oriented programming language.
> It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes.
> Python combines remarkable power with very clear syntax.
> \- [General Python FAQ](https://docs.python.org/3/faq/general.html#general-information)

The Python interpreter is freely available on all major platforms and below I will describe how you can get it set up on your own local machine.

#### Linux

If you are on Linux, chances are Python already comes prepackaged with whatever distribution you are using. However, just to be sure,
you can quickly check if it is installed by running `python3 --version`.

![Check Python Version][version]

Instructions for installing can vary depending on your distribution, but on Debian-based distos (Ubuntu, Linux Mint, etc.) you can easily install
whatever version is in the repositories by running `sudo apt install python3`.

##### Installing Newer Versions

Often the version of Python that is in the repositories may be older than the current stable release. For example, on my Ubuntu 18.04 installation
the version in the repos is 3.6.9, whereas the latest version is 3.8.3. To get the very latest version you can add the "deadsnakes"
Personal Package Archive (PPA).

```sh
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.8
```

Doing the above will allow you to avail of newer features in the language, but you'll need to write `python3.8` before running any scripts.

![Python Versions][versions]

#### Windows

Since Windows does not ship with Python preinstalled you will need to install it manually:

##### Steps

1. Visit [python.org](https://www.python.org/downloads/) and download the latest version (currently 3.8.3).

    ![Python Website][python-org]

2. Launch the executable and follow the installation. Make sure the checkbox "Add Python 3.8 to PATH" is ticked.

    ![Windows Installation][win-path]

#### Using Python

You should now be able to execute Python scripts by simple running the `python` command followed by the name of the script you want to run.
By installing Python you will also have access to a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) enviroment, wherein
you can execute simple Python commands.

![Python REPL][repl]

### Running the Program

The program can be run as follows, using the `-m` argument in order to execute the code in the `__main__.py` module.

```sh
$ python3 -m match -r REGEX -t TEXT
```

#### Command-Line Arguments

| Argument | Description |
| -------- | ---------- |
| `-h/--help` | Prints a help message and then exits. |
| `-v/--version` | Shows the program's version number then and exits. |
| `-r/--regex` | The regular expression to match. |
| `-t/--text` | The string of text you want to try and match against the pattern defined by the regular expression. |

##### Example

![Running Example][run]

### Installing with pip

pip is the package management system used by Python and can be used to install third-party packages from [Python Package Index (PyPI)](https://pypi.org/).
You can also use pip to install this package locally on your machine. Doing so will allow you to run the program system-wide, whilst omitting the `python3 -m`.

To install the package with pip, run the following from inside the root of the repository:

```sh
$ sudo pip3 install .
```

![PIP Example][pip]

**_Note:_** On Ubuntu, you may first need to `apt install python3-pip` before running the above command.

#### Removing

You can uninstall it again by running `sudo pip3 uninstall match`.

## Testing

Tests are located in the `tests/` directory and are written using the [`unittest`](https://docs.python.org/3/library/unittest.html) package
from the Python standard library.

### Run All Tests

```sh
$ python3 -m unittest discover
```

!["Testing Example"][tests]

### Run a Single Test File

```sh
$ python3 tests/[file_name].py
```

## Algorithms

This section provides an overview of the main algorithms present in the code.

### Thompson's Construction

The main algorithm used in the program is known as [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction), a method of
transforming a regular expression into an equivalent NFA. The code works by composing small NFA fragments that represent part of the regular expression,
and then proceeding to build larger NFAs from those smaller NFA fragments. If the given string is accepted by the NFA, the program will output `True`,
and `False` otherwise.

#### Thompson's Construction Summary

Thompson's construction is a method of transforming a regular expression into a non-deterministic finite automaton (NFA). Like regular expressions, NFAs
are a way of describing sets of character strings, and every valid regular expression will have an equivalent NFA that matches the same set of strings.

Thompson's algorithm works by building small NFA fragments that represent part of a regular expression, and then composing larger NFAs from those
smaller NFA fragments, with a different construction for each operator.

#### Performance

The algorithm offers a significant performance boost over the more
complex, real-world regular expression implementations used in programming
languages like Perl, Python, and others.

#### Operators Supported

The below operators/metacharacters are implemented:

| Operator | Represents | NFA Fragment \* |
| :------: | :--------- | :-----------: |
| `.` | Concatenation. | ![concat] |
| `\|` | Alternation/Union. | ![union] |
| `?` | Zero-or-one occurrences of a character. | ![optional] |
| `+` | One-or-more occurrences of a character. | ![plus] |
| `*` | Zero-or-more occurrences of a character. | ![kleene] |

\* NFA fragment diagrams taken from [these slides](https://github.com/ianmcloughlin/slides-thompson/blob/master/slides.pdf)
on Thompson's Construction.

### Shunting Yard Algorithm

Dijkstra's Shunting Yard Algorithm is a method of converting an infix expression to postfix,
also known as Reverse Polish notation (RPN), a mathematical notation in which operators follow their operands.

Expressions written in Reverse Polish can be easily interpreted by utilising a stack, and are more efficient than the infix
equivalent as only a single read over the expression is required in order to fully evaluate it, reducing execution time &
computer memory access. Also, since the order of operations is determined solely by each operator's position in the expression,
RPN does not use parentheses to specify the precedence of operators. Hence, they are omitted in the output.

## References

- https://realpython.com/installing-python/

<!-- GIFS -->
[version]: https://user-images.githubusercontent.com/37158241/80839859-f3b10580-8bf3-11ea-9c93-c58503aea16f.gif "Checking Python Version"

[tests]: https://user-images.githubusercontent.com/37158241/80839857-f27fd880-8bf3-11ea-95da-6335b697e3d7.gif "Testing"

[pip]: https://user-images.githubusercontent.com/37158241/80839860-f3b10580-8bf3-11ea-97a5-613e1d3d8b43.gif "PIP"

[run]: https://user-images.githubusercontent.com/37158241/80839862-f4499c00-8bf3-11ea-9fd8-52a1270d9e67.gif "Running the Program"

<!-- Images -->
[versions]: https://user-images.githubusercontent.com/37158241/82095647-62638800-96f7-11ea-9209-acb64b3431de.png "Linux Versions"

[win-path]: https://user-images.githubusercontent.com/37158241/82117686-b7d87d00-9769-11ea-9655-c1ceee336901.png "Windows Installation"

[repl]: https://user-images.githubusercontent.com/37158241/82095650-62fc1e80-96f7-11ea-8d2e-801c20f32d37.png "Python REPL"

[python-org]: https://user-images.githubusercontent.com/37158241/82116460-ef432b80-9761-11ea-931a-18d25bb9810d.png "Python Website"

<!-- NFA Images -->
[union]: https://user-images.githubusercontent.com/37158241/76761641-b13c8200-6787-11ea-8821-7d3c31744855.png "Union"

[kleene]: https://user-images.githubusercontent.com/37158241/76747391-f6a18500-6770-11ea-8104-1d70db17d268.png "Kleene Star"

[concat]: https://user-images.githubusercontent.com/37158241/76760396-7e918a00-6785-11ea-80cf-ea910d507358.png "Concatenation"

[optional]: https://user-images.githubusercontent.com/37158241/76747393-f7d2b200-6770-11ea-9f3b-eed4eb2fbf1a.png "Optional"

[plus]: https://user-images.githubusercontent.com/37158241/76747394-f7d2b200-6770-11ea-8891-2632ec9ccec5.png "Plus Operator"
