# Graph Theory Overview

## Contents

- [Introduction](#introduction)
    - [What are Regular Expressions?](#what-are-regular-expressions)
- [Run](#run)
    - [Installing Python](#installing-python)
    - [Running the Program](#running-the-program)
    - [Installing with pip](#installing-with-pip)
- [Testing](#testing)
- [Algorithms](#algorithms)
    - [Finite Automata Primer](#finite-automata-primer)
    - [Thompson's Construction](#thompsons-construction)
    - [Shunting Yard Algorithm](#shunting-yard-algorithm)
- [References and Further Materials](#references-and-materials)

## Introduction

The purpose of this document is to provide an explanation of the project work contained in this repository, pitched at students in the year below.

This repository contains a program written in the Python programming language that than can be used to determine if a regular expression matches a given string of text.
If the string is a match, `True` will be printed to the console, and `False` will be printed otherwise.

### What are Regular Expressions?

A regular expression is a sequence of characters that describes a pattern of character strings. The characters in a regular expression can be either literal characters,
with no special meaning, or so-called *metacharacters* which describe certain sets of characters. For instance, the metacharacter `\d` represents a digit, while `\w` represents
a single alphanumeric character. In this project only a handful of some of the most common metacharacters are implemented.

Regular expressions have a wide variety of use-cases. For instance they can be used to used to perform user input validation (e.g. valitating emails, phone numbers, etc).
They are also commonly used in performing "find and replace" operations on files, wherein every string in a file that matches a given regex is replaced with another string.
Such a feature is available in many popular text editors like Visual Studio Code or Sublime Text.

## Run

### Installing Python

In order to get started with running and testing the program you'll first need to have access to Python.

> Python is an interpreted, interactive, object-oriented programming language.
> It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes.
> Python combines remarkable power with very clear syntax.
> \- [General Python FAQ](https://docs.python.org/3/faq/general.html#general-information)

The Python interpreter is freely available on all major platforms and below I will describe how you can get it set up on your own local machine.

#### Linux

If you are on Linux, chances are Python already comes prepackaged with whatever distribution you are using. However, just to be sure,
you can quickly check if it is installed by running `python3 --version`.

![Check Python Version][version]

Instructions for installing can vary depending on your distribution, but on Debian-based distros (Ubuntu, Linux Mint, etc.) you can easily install whatever version is in the
repositories by running `sudo apt install python3`.

##### Installing Newer Versions

Often the version of Python that is in the repositories may be older than the current stable release. For example, on my Ubuntu 18.04 installation the version in the repos is 3.6.9,
whereas the latest version is 3.8.3. To get the very latest version you can add the "deadsnakes" Personal Package Archive (PPA).

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

2. Launch the executable and follow the installation. **Make sure the checkbox "Add Python 3.8 to PATH" is ticked**.

    ![Windows Installation][win-path]

#### Using Python

You should now be able to execute Python scripts by simply running the `python` (or `python3` on Linux) command followed by the name of the script you want to run.
By installing Python you will also have access to a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) enviroment, wherein you can execute simple Python commands.

![Python REPL][repl]

### Running the Program

After cloning the repository the program can be run as follows, using the `-m` argument in order to execute the code in the `__main__.py` module.

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

Tests are located in the `tests/` directory and are written using the [`unittest`](https://docs.python.org/3/library/unittest.html) package from the Python standard library.

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

In order to more adequately explain the algorithms in the code, it is necessary to provide a brief primer on automata theory.

### Finite Automata Primer

Like regular expressions, finite automata are useful tools for recognising patterns in text. Any regular expression can be converted into an equivalant finite
automaton which recognises the same set of strings.

A finite automaton is made up of several parts:

- A set of states and rules for going from one state to another, depending on the input symbol.
- An "alphabet" that indicates the input symbols the automaton recognises.
- A start state with an arrow pointing at it from nowhere.
- A set of accept states, typically represented by a state with a double circle.
- A set of arrows/edges going from one state to another. These arrows are also called transitions.

#### Example

![Finite Automaton][dfa]

The above state diagram has three states, `{q0, q1, q2}` and accepts strings over the alphabet `{0, 1}`.

When the automaton recieves an input string we read each symbol in the string one by one, following the arrow labelled with the given input symbol. After reading the entire string,
if we are located in an accept state (i.e. q1), we *accept* the string and if not, we *reject* it.

The below table is included to attempt to illustrate the result of reading the string "10111" over the automaton pictured above.

| Input | Transition |
| :---: | :--------: |
|   1   | q0 &#8594; q1 |
|   0   | q1 &#8594; q2 |
|   1   | q2 &#8594; q1 |
|   1   | q1 &#8594; q1 |
|   1   | q1 &#8594; q1 |

Because after reading the string "10111" we are in an accept state, we say the automaton accepts the string "10111".

#### Non Determinism

The diagram above is an example of a *Deterministic* finite state automaton (DFA), but finite automata may also be *Nondeterministic* (NFA).
The main difference between the two are as follows:

- An NFA may have arrows labeled with members of either the input alphabet or with an epsilon (&epsilon;), which represents the empty string.
- Every state of a DFA always has exactly one arrow for each symbol in the alphabet. In an NFA, a state may have zero, one, or many arrows for each input symbol.
- Every NFA can be converted into an equivalant DFA, however constructing NFAs is typically easier.

##### Computing NFAs

![Non Deterministic Finite Automaton][nfa]

As you can see from above, when reading a string over an NFA there may be multiple paths through which you could proceed for a given input character. For instance, if the
input string was again "10111" there are two possible paths you could follow when reading the first character (q0 &#8594; q0 *or* q0 &#8594; q1).

In order to compute such a string, the NFA will simply follow both paths simultaneously. It does this by splitting into multiple copies of itself, with each copy following
one of the possible paths. If later there are again multiple possible paths, the machine will split once again. Something similar happens whenever a state with an epsilon-labelled
arrow is encountered. Without reading any further input, the machine will automatically split into multiple copies of itself, with one following the epsilon-labelled arrow and
the other remaining at the current state.

Finally, if a given input symbol does not appear on any of the arrows exiting the state currently occupied by a copy of the machine, that copy of the machine dies.
At the end of the input, if any of the remaining copies of the machine are in an accept state, we say the NFA accepts the input string.

> Nondeterminism may be viewed as a kind of parallel computation wherein
> multiple independent "processes" or "threads" can be running concurrently.
> When the NFA splits to follow several choices, that corresponds to a process
> "forking" into several children, each proceeding separately. If at least one of
> these processes accepts, then the entire computation accepts.
> \- Michael Sipser, Introduction to the Theory of Computation (3rd Edition, ch.1, pg. 48).

### Thompson's Construction

The main algorithm used in the program is known as [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction).

As mentioned previously, any regular expression can be converted into an equivalant finite automaton which recognises the same set of strings. Thompsons's Construction is
a method of transforming a regular expression into its equivalent NFA.

Thompson's algorithm works by building small NFA fragments that represent part of a regular expression,
and then composing larger NFAs from those smaller NFA fragments, with a different construction for each operator.

#### Performance

The algorithm offers a significant performance boost over the more complex, real-world regular expression implementations
used in programming languages like Perl, Python, and many others.

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

Dijkstra's Shunting Yard Algorithm is used for converting a regular expression written in infix notation to postfix,
also known as Reverse Polish notation (RPN), a mathematical notation in which operators follow their operands.

Expressions written in Reverse Polish can be easily interpreted by utilising a stack, and are more efficient than the infix equivalent as only a single
read over the expression is required in order to fully evaluate it, reducing execution time & computer memory access. Also, since the order of operations is determined
solely by each operator's position in the expression, RPN does not use parentheses to specify the precedence of operators. Hence, they are omitted in the output.

## References and Further Materials

- Introduction to the Theory of Computation by Michael Sipser (3rd Edition) - The above sections about automata theory are adapted heavily from Chapter One of this book.

- [RegexOne Interactive Tutorial](https://regexone.com/) - The best online tutorial I found for learning to use regular expressions.

- [Regular Expression Matching Can Be Simple And Fast - Russ Cox](https://swtch.com/~rsc/regexp/regexp1.html).

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

<!-- DFA Images -->
[dfa]: https://user-images.githubusercontent.com/37158241/82128921-ea5c9700-97b6-11ea-8ea2-710862c58698.png "DFA"

[nfa]: https://user-images.githubusercontent.com/37158241/82148091-1f65f980-984a-11ea-83f4-8aaf24173eff.png "NFA"

<!-- NFA Images -->
[union]: https://user-images.githubusercontent.com/37158241/76761641-b13c8200-6787-11ea-8821-7d3c31744855.png "Union"

[kleene]: https://user-images.githubusercontent.com/37158241/76747391-f6a18500-6770-11ea-8104-1d70db17d268.png "Kleene Star"

[concat]: https://user-images.githubusercontent.com/37158241/76760396-7e918a00-6785-11ea-80cf-ea910d507358.png "Concatenation"

[optional]: https://user-images.githubusercontent.com/37158241/76747393-f7d2b200-6770-11ea-9f3b-eed4eb2fbf1a.png "Optional"

[plus]: https://user-images.githubusercontent.com/37158241/76747394-f7d2b200-6770-11ea-8891-2632ec9ccec5.png "Plus Operator"
