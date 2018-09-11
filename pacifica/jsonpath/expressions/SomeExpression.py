#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator

from pacifica.jsonpath.Expression import Expression
from pacifica.jsonpath.Node import Node

class SomeExpression(Expression):
    def __init__(self, next_node:Node):
        super(SomeExpression, self).__init__()

        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def evaluate(self, root_value:object, current_value:object) -> bool:
        for next_node_match_data in self.next_node.match(root_value, current_value):
            return True

        return False
