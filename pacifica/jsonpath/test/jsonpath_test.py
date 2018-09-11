#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
from unittest import TestCase

from pacifica.jsonpath.Node import MatchData
from pacifica.jsonpath.Path import Path

from pacifica.jsonpath.expressions.OperatorExpression import AndVariadicOperatorExpression, EqualBinaryOperatorExpression
from pacifica.jsonpath.expressions.SomeExpression import SomeExpression

from pacifica.jsonpath.nodes.CurrentNode import CurrentNode
from pacifica.jsonpath.nodes.RecursiveDescentNode import RecursiveDescentNode
from pacifica.jsonpath.nodes.RootNode import RootNode
from pacifica.jsonpath.nodes.SubscriptNode import SubscriptNode
from pacifica.jsonpath.nodes.TerminalNode import TerminalNode

from pacifica.jsonpath.subscripts.ArrayIndexSubscript import ArrayIndexSubscript
from pacifica.jsonpath.subscripts.ArraySliceSubscript import ArraySliceSubscript
from pacifica.jsonpath.subscripts.FilterSubscript import FilterSubscript
from pacifica.jsonpath.subscripts.ObjectIndexSubscript import ObjectIndexSubscript
from pacifica.jsonpath.subscripts.WildcardSubscript import WildcardSubscript

class TestNode(TestCase):
    def setUp(self):
        root_value = {
            'hello': 'Hello, world!',
            'languages': [
                'en-GB',
                'en-US',
            ],
        }
        current_value = root_value['hello']

        self._state = [
            {
                '__jsonpath__': '',
                'node': TerminalNode(),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '$',
                'node': RootNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(RootNode(TerminalNode()), root_value, root_value),
                ],
            },
            {
                '__jsonpath__': '@',
                'node': CurrentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(CurrentNode(TerminalNode()), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '[]',
                'node': SubscriptNode(TerminalNode(), []),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [],
            },
            {
                '__jsonpath__': '[?(@)]',
                'node': SubscriptNode(TerminalNode(), [FilterSubscript(SomeExpression(CurrentNode(TerminalNode())))]),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '[?(@),?(@)]',
                'node': SubscriptNode(TerminalNode(), [FilterSubscript(SomeExpression(CurrentNode(TerminalNode()))), FilterSubscript(SomeExpression(CurrentNode(TerminalNode())))]),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '[*]',
                'node': SubscriptNode(TerminalNode(), [WildcardSubscript()]),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [],
            },
            {
                '__jsonpath__': '[*]',
                'node': SubscriptNode(TerminalNode(), [WildcardSubscript()]),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                ],
            },
            {
                '__jsonpath__': '["languages"][*]',
                'node': SubscriptNode(SubscriptNode(TerminalNode(), [WildcardSubscript()]), [ObjectIndexSubscript('languages')]),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(1)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][1]),
                ],
            },
            {
                '__jsonpath__': '["hello","languages"]',
                'node': SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello'), ObjectIndexSubscript('languages')]),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                ],
            },
            {
                '__jsonpath__': '..',
                'node': RecursiveDescentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': current_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, current_value),
                ],
            },
            {
                '__jsonpath__': '..',
                'node': RecursiveDescentNode(TerminalNode()),
                'root_value': root_value,
                'current_value': root_value,
                'match_data_list': [
                    MatchData(TerminalNode(), root_value, root_value),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('hello')]), root_value, root_value['hello']),
                    MatchData(SubscriptNode(TerminalNode(), [ObjectIndexSubscript('languages')]), root_value, root_value['languages']),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(0)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][0]),
                    MatchData(SubscriptNode(SubscriptNode(TerminalNode(), [ArrayIndexSubscript(1)]), [ObjectIndexSubscript('languages')]), root_value, root_value['languages'][1]),
                ],
            },
        ]

    def _assertNodeTestCase(self, **kwargs):
        self.assertEqual(kwargs['__jsonpath__'], kwargs['node'].tojsonpath())

        match_data_list = list(kwargs['node'].match(kwargs['root_value'], kwargs['current_value']))

        self.assertEqual(kwargs['match_data_list'], match_data_list)

        for match_data in match_data_list:
            new_match_data_list = list(match_data.node.match(kwargs['root_value'], kwargs['current_value']))

            self.assertEqual([match_data], new_match_data_list)

    def test_state(self):
        for kwargs in self._state:
            self._assertNodeTestCase(**kwargs)

class TestCloudEvents(TestCase):
    def test_cloudevents(self):
        with open(os.path.join('test_files', 'events.json'), 'r') as io:
            d = json.load(io)

        s = '$[?(@["eventID"] and @["eventType"] = "org.pacifica.metadata.ingest" and @["source"] = "/pacifica/metadata/ingest")]["data"][*][?(@["destinationTable"] = "TransactionKeyValue")]["key"]'

        p = Path.parse_str(s)

        n = RootNode(
                SubscriptNode(
                    SubscriptNode(
                        SubscriptNode(
                            SubscriptNode(
                                SubscriptNode(
                                    TerminalNode(),
                                    [
                                        ObjectIndexSubscript('key'),
                                    ]
                                ),
                                [
                                    FilterSubscript(
                                        EqualBinaryOperatorExpression(
                                            CurrentNode(
                                                SubscriptNode(
                                                    TerminalNode(),
                                                    [
                                                        ObjectIndexSubscript('destinationTable'),
                                                    ]
                                                )
                                            ),
                                            'TransactionKeyValue'
                                        )
                                    ),
                                ]
                            ),
                            [
                                WildcardSubscript(),
                            ]
                        ),
                        [
                            ObjectIndexSubscript('data'),
                        ]
                    ),
                    [
                        FilterSubscript(
                            AndVariadicOperatorExpression(
                                [
                                    SomeExpression(
                                        CurrentNode(
                                            SubscriptNode(
                                                TerminalNode(),
                                                [
                                                    ObjectIndexSubscript('eventID'),
                                                ]
                                            )
                                        ),
                                    ),
                                    EqualBinaryOperatorExpression(
                                        CurrentNode(
                                            SubscriptNode(
                                                TerminalNode(),
                                                [
                                                    ObjectIndexSubscript('eventType'),
                                                ]
                                            )
                                        ),
                                        'org.pacifica.metadata.ingest'
                                    ),
                                    EqualBinaryOperatorExpression(
                                        CurrentNode(
                                            SubscriptNode(
                                                TerminalNode(),
                                                [
                                                    ObjectIndexSubscript('source'),
                                                ]
                                            )
                                        ),
                                        '/pacifica/metadata/ingest'
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            )

        self.assertEqual(n, p.root_node)

        self.assertEqual(s, str(p))

        match_data_list = list(p.match(d))

        self.assertEqual([
            MatchData(Path.parse_str('$["data"][4]["key"]').root_node, d, 'Tag'),
            MatchData(Path.parse_str('$["data"][5]["key"]').root_node, d, 'Taggy'),
            MatchData(Path.parse_str('$["data"][6]["key"]').root_node, d, 'Taggier'),
        ], match_data_list)

        for match_data in match_data_list:
            new_match_data_list = list(match_data.node.match(match_data.root_value, match_data.current_value))

            self.assertEqual([match_data], new_match_data_list)
