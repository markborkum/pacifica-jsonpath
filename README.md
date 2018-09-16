# python-jsonpath2
[![Build Status](https://travis-ci.org/pacifica/template-jsonpath.svg?branch=master)](https://travis-ci.org/pacifica/python-jsonpath2)
[![Build status](https://ci.appveyor.com/api/projects/status/eg2r1y37yvxi0b5p?svg=true)](https://ci.appveyor.com/project/pacifica/python-jsonpath2)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d6149dbe182a3c761089/test_coverage)](https://codeclimate.com/github/pacifica/python-jsonpath2/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/f2dba248b1a7966e5a49/maintainability)](https://codeclimate.com/github/pacifica/python-jsonpath2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f2dba248b1a7966e5a49/test_coverage)](https://codeclimate.com/github/pacifica/python-jsonpath2/test_coverage)

This repository contains an implementation of [JSONPath](http://goessner.net/articles/JsonPath/) ([XPath](https://www.w3.org/TR/xpath/all/) for [JSON](https://www.json.org/)) for the Python programming language.

## API

### `Path` class

The `jsonpath2.Path.Path` class represents a JSONPath.

```python
>>> s = '{"hello":"Hello, world!"}'
'{"hello":"Hello, world!"}'
>>> import json
>>> d = json.loads(s)
{'hello':'Hello, world!'}
>>> from jsonpath2.Path import Path
>>> p = Path.parse_str('$["hello"]')
<jsonpath2.Path.Path object>
>>> list(map(lambda match_data: match_data.current_value, p.match(d)))
['Hello, world!']
>>> list(map(lambda match_data: match_data.node.tojsonpath(), p.match(d)))
['$["hello"]']
```

This class is constructed with respect to the given instance of the `jsonpath2.Path.RootNode` class (viz., the `root_node` property).

#### `parse_str(strdata)` class method

Parse the given string and return a new instance of this class.

#### `parse_file(fileName, encoding='ascii')` class method

Parse the contents of the given file and return a new instance of this class.

#### `match(root_value)` instance method

Match the given JSON data structure against this instance.
For each match, yield an instance of the `jsonpath2.Node.MatchData` class.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `__str__()` instance method

Returns the string representation of this instance.

#### `root_node` property

The root node of the abstract syntax tree for this instance.

### `Node` abstract class

The `jsonpath2.Node.Node` class represents the abstract syntax tree for a JSONPath.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `__jsonpath__()` instance method

Yields the lexer tokens for the string representation of this instance.

#### `match(root_value, current_value)` instance method

Match the given root and current JSON data structures against this instance.
For each match, yield an instance of the `jsonpath2.Node.MatchData` class.

#### `tojsonpath()` instance method

Returns the string representation of this instance.

### `MatchData` class

The `jsonpath2.Node.MatchData` class represents the JSON value and context for a JSONPath match.

This class is constructed with respect to a root JSON value, a current JSON value, and an abstract syntax tree node.

#### `__eq__(other)` instance method

Tests if two instances are equal.

#### `root_value` property

The root JSON value.

#### `current_value` property

The current JSON value (i.e., the matching JSON value).

#### `node` property

The abstract syntax tree node.

## Syntax

| XPath | JSONPath | Description |
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

| JSONPath Filter Expression | Description |
| - | - |
| `$` or `@` | nested JSONPath (returns `true` if any match exists; otherwise, returns `false`) |
| `=`, `!=`, `>`, `>=`, `<`, `<=` | binary operator, where left-hand operand is a nested JSONPath and right-right operand is a JSON value (returns `true` if any match exists; otherwise, returns `false`) |
| `and`, `or`, `not` | Boolean operator, where operands are JSONPath filter expressions |
| `(` ... `)` | parentheses |
