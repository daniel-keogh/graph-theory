# Graph Theory

Y3S2 Graph Theory Project

## Description

A Python programme that can build a non-deterministic finite automaton (NFA) from a regular expression, and
can use the NFA to check if the regular expression matches any given string of text.

## Usage

```sh
match [-h] -r REGEXP -t TEXT
```

### Arguments

| Argument | Descripion |
| -------- | ---------- |
| `-r/--regexp` | The regular expression to match. |
| `-t/--text` | The string of text to match the regular expression against. |
| `-h/--help` | Prints some help text. |

#### Example

```sh
$ python3 match -r a.b|b* -t bbbbbbbb

True
```
