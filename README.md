# Pacifica JSONPath
[![Build Status](https://travis-ci.org/pacifica/template-jsonpath.svg?branch=master)](https://travis-ci.org/pacifica/pacifica-jsonpath)
[![Build status](https://ci.appveyor.com/api/projects/status/eg2r1y37yvxi0b5p?svg=true)](https://ci.appveyor.com/project/pacifica/pacifica-jsonpath)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d6149dbe182a3c761089/test_coverage)](https://codeclimate.com/github/pacifica/pacifica-jsonpath/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/f2dba248b1a7966e5a49/maintainability)](https://codeclimate.com/github/pacifica/pacifica-jsonpath/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f2dba248b1a7966e5a49/test_coverage)](https://codeclimate.com/github/pacifica/pacifica-jsonpath/test_coverage)

This repository contains the Pacifica implementation of [JSONPath](http://goessner.net/articles/JsonPath/) ([XPath](https://www.w3.org/TR/xpath/all/) for [JSON](https://www.json.org/)).

## API

### `Path` class

The `pacifica.jsonpath.Path.Path` class represents the abstract syntax tree for a Pacifica JSONPath.

```python
>>> s = '{"hello":"Hello, world!"}'
'{"hello":"Hello, world!"}'
>>> import json
>>> d = json.loads(s)
{'hello':'Hello, world!'}
>>> from pacifica.jsonpath.Path import Path
>>> p = Path.parse_str('$["hello"]')
<pacifica.jsonpath.Path.Path object>
>>> list(map(lambda match: match.current_value, p.match(d)))
['Hello, world!']
```

This class is constructed with respect to the given instance of the `pacifica.jsonpath.Path.RootNode` class (viz., the `node` attribute).

#### `parse_str(strdata)` class method

Parse the given string and return a new instance of this class.

#### `parse_file(fileName, encoding)` class method

Parse the contents of the given file and return a new instance of this class.

#### `match(root_value)` instance method

Match the given JSON data structure against this instance.
For each match, yield an instance of the `pacifica.jsonpath.Node.MatchData` class.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `__str__()` instance method

Returns the string representation of this instance.

#### `root_node` attribute

The root node of the abstract syntax tree for this instance.

### `MatchData` class

The `pacifica.jsonpath.Node.MatchData` class represents the JSON value and context for a Pacifica JSONPath match.

This class is constructed with respect to a root JSON value, a current JSON value, and an abstract syntax tree node.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `root_value` attribute

The root JSON value.

#### `current_value` attribute

The current JSON value (i.e., the matching JSON value).

#### `node` attribute

The abstract syntax tree node.

## Syntax

| XPath | Pacifica JSONPath | Description |
| - | - | - |
| `/` | `$` | the root JSON value |
| `.` | `@` | the current JSON value |
| `/` | `.` or `[]` | child operator |
| `//` | `..` | recursive descent (depth-first search) |
| `*` | `*` | wildcard (all elements of a JSON array; all values of a JSON object; otherwise none) |
| `[]` | `[]` | subscript operator |
| <code>&#124;</code> | `[,]` | union operator (for two or more subscript operators) |
| n/a | `[start:end:step]` | slice operator (subset of elements of a JSON array) |
| `[]` | `?()` | filter expression (for use with subscript operator) |

| Pacifica JSONPath Filter Expression | Description |
| - | - |
| `$` or `@` | nested Pacifica JSONPath (returns `true` if any match exists; otherwise, returns `false`) |
| `=`, `!=`, `>`, `>=`, `<`, `<=` | binary operator, where left-hand operand is a nested Pacifica JSONPath and right-right operand is a JSON value (returns `true` if any match exists; otherwise, returns `false`) |
| `and`, `or`, `not` | Boolean operator, where operands are Pacifica JSONPath filter expressions |
| `(` ... `)` | parentheses |
