#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
from typing import Generator

from pacifica.jsonpath.Node import MatchData, Node

from pacifica.jsonpath.nodes.SubscriptNode import SubscriptNode

from pacifica.jsonpath.subscripts.WildcardSubscript import WildcardSubscript

class RecursiveDescentNode(Node):
    def __init__(self, next_node:Node):
        super(RecursiveDescentNode, self).__init__()

        self.next_node = next_node

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield '['
        yield '**'
        yield ']'

        for next_node_token in self.next_node.__jsonpath__():
            yield next_node_token

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        # NOTE Depth-first
        return itertools.chain(self.next_node.match(root_value, current_value), SubscriptNode(self, [WildcardSubscript()]).match(root_value, current_value))
