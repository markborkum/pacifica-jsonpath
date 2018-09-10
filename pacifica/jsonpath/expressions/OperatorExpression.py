#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod
import json
from typing import Callable, Generator, List

from pacifica.jsonpath.Expression import Expression
from pacifica.jsonpath.Node import Node

from pacifica.jsonpath.expressions.SomeExpression import SomeExpression

class OperatorExpression(Expression):
    pass

class BinaryOperatorExpression(OperatorExpression):
    def __init__(self, token:str, callback:Callable[[object, object], bool], left_node:Node, right_value:object):
        super(BinaryOperatorExpression, self).__init__()

        self.token = token

        self.callback = callback

        self.left_node = left_node

        self.right_value = right_value

    def __jsonpath__(self) -> Generator[str, None, None]:
        for left_node_token in self.left_node.__jsonpath__():
            yield left_node_token

        yield ' '
        yield self.token
        yield ' '

        yield json.dumps(self.right_value)

    def evaluate(self, root_value:object, current_value:object) -> bool:
        return any(map(lambda left_node_match_data: self.callback(left_node_match_data.current_value, self.right_value), self.left_node.match(root_value, current_value)))

class EqualBinaryOperatorExpression(BinaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(EqualBinaryOperatorExpression, self).__init__('=', lambda x, y: x == y, *args, **kwargs)

class NotEqualBinaryOperatorExpression(BinaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(NotEqualBinaryOperatorExpression, self).__init__('!=', lambda x, y: x != y, *args, **kwargs)

def _wrap_callback(callback):
    def wrapped_callback(x, y):
        if (isinstance(x, float) or isinstance(x, int)) and ((isinstance(y, float) or isinstance(y, int))):
            return callback(x, y)
        else:
            return False
    return wrapped_callback

class LessThanBinaryOperatorExpression(BinaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(LessThanBinaryOperatorExpression, self).__init__('<', _wrap_callback(lambda x, y: x < y), *args, **kwargs)

class LessThanOrEqualToBinaryOperatorExpression(BinaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(LessThanOrEqualToBinaryOperatorExpression, self).__init__('<=', _wrap_callback(lambda x, y: x <= y), *args, **kwargs)

class GreaterThanBinaryOperatorExpression(BinaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(GreaterThanBinaryOperatorExpression, self).__init__('>', _wrap_callback(lambda x, y: x > y), *args, **kwargs)

class GreaterThanOrEqualToBinaryOperatorExpression(BinaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(GreaterThanOrEqualToBinaryOperatorExpression, self).__init__('>=', _wrap_callback(lambda x, y: x >= y), *args, **kwargs)

class UnaryOperatorExpression(OperatorExpression):
    def __init__(self, token:str, callback:Callable[[bool], bool], expression:Expression):
        super(UnaryOperatorExpression, self).__init__()

        self.token = token

        self.callback = callback

        self.expression = expression

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield self.token
        yield ' '

        if isinstance(self.expression, UnaryOperatorExpression) or isinstance(self.expression, VariadicOperatorExpression):
            yield '('

        for expression_token in self.expression.__jsonpath__():
            yield expression_token

        if isinstance(self.expression, UnaryOperatorExpression) or isinstance(self.expression, VariadicOperatorExpression):
            yield ')'

    def evaluate(self, root_value:object, current_value:object) -> bool:
        return self.callback(self.expression.evaluate(root_value, current_value))

class NotUnaryOperatorExpression(UnaryOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(NotUnaryOperatorExpression, self).__init__('not', lambda x: not x, *args, **kwargs)

class VariadicOperatorExpression(OperatorExpression):
    def __init__(self, token:str, callback:Callable[[List[bool]], bool], expressions:List[Expression]=[]):
        super(VariadicOperatorExpression, self).__init__()

        self.token = token

        self.callback = callback

        self.expressions = expressions

    def __jsonpath__(self) -> Generator[str, None, None]:
        expressions_count = len(self.expressions)

        if expressions_count == 0:
            pass
        elif expressions_count == 1:
            for expression_token in self.expressions[0].__jsonpath__():
                yield expression_token
        else:
            for expression_index, expression in enumerate(self.expressions):
                if expression_index > 0:
                    yield ' '
                    yield self.token
                    yield ' '

                if isinstance(expression, VariadicOperatorExpression):
                    yield '('

                for expression_token in expression.__jsonpath__():
                    yield expression_token

                if isinstance(expression, VariadicOperatorExpression):
                    yield ')'

    def evaluate(self, root_value:object, current_value:object) -> bool:
        return self.callback(map(lambda expression: expression.evaluate(root_value, current_value), self.expressions))

class AndVariadicOperatorExpression(VariadicOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(AndVariadicOperatorExpression, self).__init__('and', all, *args, **kwargs)

class OrVariadicOperatorExpression(VariadicOperatorExpression):
    def __init__(self, *args, **kwargs):
        super(OrVariadicOperatorExpression, self).__init__('or', any, *args, **kwargs)
