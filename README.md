# Graph Theory

Y3S2 Graph Theory Project

## Description

A Python programme that can build a non-deterministic finite automaton (NFA) from a regular expression, and
can use the NFA to check if the regular expression matches a given string of text.

## Running

### Usage

```sh
match -r REGEX -t TEXT
```

#### Arguments

| Argument | Description |
| -------- | ---------- |
| `-r/--regex` | The regular expression to match. |
| `-t/--text` | The string of text to match the regular expression against. |
| `-h/--help` | Prints some help text. |

#### Example

From inside the root of the repository, run:

```sh
$ python3 -m match -r "a.b|b*" -t "bbbbbbbb"

True
```

## Installing

From inside the root of the repository, run:

```sh
$ pip3 install .
```

Now you should be able to run the package while omitting the `python3`.

```sh
$ match --help
```

### Removing

You can uninstall it again by running `pip3 uninstall match`.

## Testing

### Run All Tests

```sh
$ python3 -m unittest discover
```

### Run a Single Test

```sh
$ python3 tests/[file_name].py
```
