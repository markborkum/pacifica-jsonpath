#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
from typing import Generator

from pacifica.jsonpath.Node import MatchData
from pacifica.jsonpath.Subscript import Subscript

from pacifica.jsonpath.subscripts.ArrayIndexSubscript import ArrayIndexSubscript
from pacifica.jsonpath.subscripts.ObjectIndexSubscript import ObjectIndexSubscript

class WildcardSubscript(Subscript):
    def __init__(self):
        super(WildcardSubscript, self).__init__()

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield '*'

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        if isinstance(current_value, dict):
            return itertools.chain(*map(lambda index: ObjectIndexSubscript(index).match(root_value, current_value), current_value.keys()))
        elif isinstance(current_value, list):
            return itertools.chain(*map(lambda index: ArrayIndexSubscript(index).match(root_value, current_value), range(len(current_value))))
        else:
            return []
