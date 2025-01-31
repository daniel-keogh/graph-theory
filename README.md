# Graph Theory

Y3S2 Graph Theory Project

## Description

A Python program that can build a non-deterministic finite automaton (NFA) from a regular expression, and
can use the NFA to check if the regular expression matches a given string of text.

The program uses an algorithm known as [Thompson's construction](https://en.wikipedia.org/wiki/Thompson%27s_construction),
a method of transforming a regular expression into an equivalent NFA. The code works by composing small NFA fragments
that represent part of the regular expression, and then proceeding to build larger NFAs from those smaller NFA fragments.
If the given string is accepted by the NFA, the program will output `True`, and
`False` otherwise.

### Operators

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

## Running

The program can be run as follows, using the `-m` argument in order to execute the `__main__.py` module.

```sh
$ python3 -m match -r REGEX -t TEXT
```

### Command-Line Arguments

| Argument | Description |
| -------- | ---------- |
| `-h/--help` | Prints a help message and then exits. |
| `-v/--version` | Shows the program's version number then and exits. |
| `-r/--regex` | The regular expression to match. |
| `-t/--text` | The string of text you want to try and match against the pattern defined by the regular expression. |

#### Example

![Running Example][run]

## Installing with pip

From inside the root of the repository, run:

```sh
$ sudo pip3 install .
```

This will allow you to run the program system-wide, while omitting the `python3 -m`.

![PIP Example][pip]

**_Note:_** You may first need to `apt install python3-pip` before installing.

### Removing

You can uninstall it again by running `sudo pip3 uninstall match`.

## Testing

Tests are located in the `tests/` directory.

### Run All Tests

```sh
$ python3 -m unittest discover --verbose
```

!["Testing Example"][tests]

### Run a Single Test

```sh
$ python3 tests/[file_name].py
```

## Documentation

The documentation for this project is deployed on [GitHub Pages](https://daniel-keogh.github.io/graph-theory/).

### Building the Docs

**_Note:_** You may first need to install the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation generator.
On Debian-based Linux distributions this can be done by running:

```sh
$ sudo apt install python3-sphinx
```

You should then be able to run `make html` from within the `docs/` directory to reproduce the HTML files, which will be
placed in the `_build/html` directory.

!["Sphinx Example"][docs]

### Notes

- The docstrings thoughout this project follow the reStructuredText (reST) format outlined in [PEP 287](https://www.python.org/dev/peps/pep-0287/).

- The contents of the `docs/` directory were mostly auto-generated using the `sphinx-quickstart` command,
followed by `sphinx-apidoc -o . ../match --separate` to create the RST files.

<!-- Console Images -->
[run]: https://user-images.githubusercontent.com/37158241/76702521-5a20a980-66c2-11ea-8813-589fd489a5e3.PNG "Running the Program"

[pip]: https://user-images.githubusercontent.com/37158241/80708607-e1e03d00-8ae3-11ea-95cb-239ddf52259c.PNG "PIP Install"

[tests]: https://user-images.githubusercontent.com/37158241/82117563-b3f82b00-9768-11ea-8a72-61f49be8d8fc.PNG "Testing"

[docs]: https://user-images.githubusercontent.com/37158241/76702668-75d87f80-66c3-11ea-9db0-50f4fc75f2b8.PNG "Sphinx Build"

<!-- NFA Images -->
[union]: https://user-images.githubusercontent.com/37158241/76761641-b13c8200-6787-11ea-8821-7d3c31744855.png "Union"

[kleene]: https://user-images.githubusercontent.com/37158241/76747391-f6a18500-6770-11ea-8104-1d70db17d268.png "Kleene Star"

[concat]: https://user-images.githubusercontent.com/37158241/76760396-7e918a00-6785-11ea-80cf-ea910d507358.png "Concatenation"

[optional]: https://user-images.githubusercontent.com/37158241/76747393-f7d2b200-6770-11ea-9f3b-eed4eb2fbf1a.png "Optional"

[plus]: https://user-images.githubusercontent.com/37158241/76747394-f7d2b200-6770-11ea-8891-2632ec9ccec5.png "Plus Operator"
