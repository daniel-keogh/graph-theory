# Graph Theory

Y3S2 Graph Theory Project

## Description

A Python programme that can build a non-deterministic finite automaton (NFA) from a regular expression, and
can use the NFA to check if the regular expression matches any given string of text.

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

## Tests

From inside the root of the repository, run:

```sh
$ cd tests/
$ python3 <file_name>
```

## Docs

Documentation can be generated as follows:

```sh
$ cd docs/
$ make html
```
