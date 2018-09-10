#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import Generator

from pacifica.jsonpath.Node import MatchData
from pacifica.jsonpath.Subscript import Subscript

class ObjectIndexSubscript(Subscript):
    def __init__(self, index:str):
        super(ObjectIndexSubscript, self).__init__()

        self.index = index

    def __jsonpath__(self) -> Generator[str, None, None]:
        yield json.dumps(self.index)

    def match(self, root_value:object, current_value:object) -> Generator[MatchData, None, None]:
        if isinstance(current_value, dict) and (self.index in current_value):
            return [MatchData(self, root_value, current_value[self.index])]
        else:
            return []
