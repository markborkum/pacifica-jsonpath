#!/usr/bin/python
# -*- coding: utf-8 -*-

import antlr4

from pacifica.jsonpath.expressions.OperatorExpression import AndVariadicOperatorExpression, EqualBinaryOperatorExpression, GreaterThanBinaryOperatorExpression, GreaterThanOrEqualToBinaryOperatorExpression, LessThanBinaryOperatorExpression, LessThanOrEqualToBinaryOperatorExpression, NotEqualBinaryOperatorExpression, NotUnaryOperatorExpression, OrVariadicOperatorExpression
from pacifica.jsonpath.expressions.SomeExpression import SomeExpression

from pacifica.jsonpath.nodes.CurrentNode import CurrentNode
from pacifica.jsonpath.nodes.RecursiveDescentNode import RecursiveDescentNode
from pacifica.jsonpath.nodes.RootNode import RootNode
from pacifica.jsonpath.nodes.SubscriptNode import SubscriptNode
from pacifica.jsonpath.nodes.TerminalNode import TerminalNode

from pacifica.jsonpath.parser.JSONPathLexer import JSONPathLexer
from pacifica.jsonpath.parser.JSONPathListener import JSONPathListener
from pacifica.jsonpath.parser.JSONPathParser import JSONPathParser

from pacifica.jsonpath.subscripts.ArrayIndexSubscript import ArrayIndexSubscript
from pacifica.jsonpath.subscripts.ArraySliceSubscript import ArraySliceSubscript
from pacifica.jsonpath.subscripts.FilterSubscript import FilterSubscript
from pacifica.jsonpath.subscripts.ObjectIndexSubscript import ObjectIndexSubscript
from pacifica.jsonpath.subscripts.WildcardSubscript import WildcardSubscript

class _ConsoleErrorListener(antlr4.error.ErrorListener.ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError('line {}:{} {}'.format(line, column, msg))

class _JSONPathListener(JSONPathListener):
    def __init__(self, _stack=[]):
        super(_JSONPathListener, self).__init__()

        self._stack = _stack

    def exitJsonpath(self, ctx:JSONPathParser.JsonpathContext):
        if ctx.getToken(JSONPathParser.T__0, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            self._stack.append(RootNode(next_node))
        else:
            raise ValueError()

    def exitSubscript(self, ctx:JSONPathParser.SubscriptContext):
        if ctx.getToken(JSONPathParser.T__3, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            if bool(ctx.subscriptableBareword()):
                subscriptable_nodes = [self._stack.pop()]
            elif bool(ctx.subscriptables()):
                subscriptable_nodes = self._stack.pop()
            else:
                raise ValueError()

            self._stack.append(RecursiveDescentNode(SubscriptNode(next_node, subscriptable_nodes)))
        elif ctx.getToken(JSONPathParser.T__4, 0) is not None:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            if bool(ctx.subscriptableBareword()):
                subscriptable_nodes = [self._stack.pop()]
            else:
                raise ValueError()

            self._stack.append(SubscriptNode(next_node, subscriptable_nodes))
        else:
            if bool(ctx.subscript()):
                next_node = self._stack.pop()
            else:
                next_node = TerminalNode()

            if bool(ctx.subscriptables()):
                subscriptable_nodes = self._stack.pop()
            else:
                raise ValueError()

            self._stack.append(SubscriptNode(next_node, subscriptable_nodes))

    def exitSubscriptables(self, ctx:JSONPathParser.SubscriptablesContext):
        subscriptable_nodes = []

        for subscriptable_ctx in ctx.getTypedRuleContexts(JSONPathParser.SubscriptableContext):
            subscriptable_node = self._stack.pop()

            subscriptable_nodes.insert(0, subscriptable_node)

        self._stack.append(subscriptable_nodes)

    def exitSubscriptableBareword(self, ctx:JSONPathParser.SubscriptableBarewordContext):
        if bool(ctx.ID()):
            text = ctx.ID().getText()

            self._stack.append(ObjectIndexSubscript(text))
        elif ctx.getToken(JSONPathParser.T__6, 0) is not None:
            self._stack.append(WildcardSubscript())
        else:
            raise ValueError()

    def exitSubscriptable(self, ctx:JSONPathParser.SubscriptableContext):
        if bool(ctx.STRING()):
            text = ctx.STRING().getText()[1:-1]

            self._stack.append(ObjectIndexSubscript(text))
        elif bool(ctx.NUMBER()):
            if ctx.getToken(JSONPathParser.T__7, 0) is not None:
                if bool(ctx.NUMBER(0)):
                    text = ctx.NUMBER(0).getText()

                    if ('.' in text) or ('E' in text) or ('e' in text):
                        start = float(text)
                    else:
                        start = int(text)
                else:
                    start = None

                if bool(ctx.NUMBER(1)):
                    text = ctx.NUMBER(1).getText()

                    if ('.' in text) or ('E' in text) or ('e' in text):
                        end = float(text)
                    else:
                        end = int(text)
                else:
                    end = None

                if bool(ctx.NUMBER(2)):
                    text = ctx.NUMBER(2).getText()

                    if ('.' in text) or ('E' in text) or ('e' in text):
                        step = float(text)
                    else:
                        step = int(text)
                else:
                    step = None

                self._stack.append(ArraySliceSubscript(start, end, step))
            else:
                text = ctx.NUMBER(0).getText()

                if ('.' in text) or ('E' in text) or ('e' in text):
                    self._stack.append(ArrayIndexSubscript(float(text)))
                else:
                    self._stack.append(ArrayIndexSubscript(int(text)))
        elif ctx.getToken(JSONPathParser.T__6, 0) is not None:
            self._stack.append(WildcardSubscript())
        elif ctx.getToken(JSONPathParser.T__8, 0) is not None:
            expression = self._stack.pop()

            self._stack.append(FilterSubscript(expression))
        else:
            raise ValueError()

    def exitAndExpression(self, ctx:JSONPathParser.AndExpressionContext):
        expressions = []

        if bool(ctx.andExpression()):
            expression = self._stack.pop()

            if isinstance(expression, AndVariadicOperatorExpression):
                expressions = expression.expressions + expressions
            else:
                expressions.insert(0, expression)

        expression = self._stack.pop()

        if isinstance(expression, AndVariadicOperatorExpression):
            expressions = expression.expressions + expressions
        else:
            expressions.insert(0, expression)

        if len(expressions) == 0:
            raise ValueError()
        if len(expressions) == 1:
            self._stack.append(expressions[0])
        else:
            self._stack.append(AndVariadicOperatorExpression(expressions))

    def exitOrExpression(self, ctx:JSONPathParser.OrExpressionContext):
        expressions = []

        if bool(ctx.orExpression()):
            expression = self._stack.pop()

            if isinstance(expression, OrVariadicOperatorExpression):
                expressions = expression.expressions + expressions
            else:
                expressions.insert(0, expression)

        expression = self._stack.pop()

        if isinstance(expression, OrVariadicOperatorExpression):
            expressions = expression.expressions + expressions
        else:
            expressions.insert(0, expression)

        if len(expressions) == 0:
            raise ValueError()
        if len(expressions) == 1:
            self._stack.append(expressions[0])
        else:
            self._stack.append(OrVariadicOperatorExpression(expressions))

    def exitNotExpression(self, ctx:JSONPathParser.NotExpressionContext):
        if ctx.getToken(JSONPathParser.T__13, 0) is not None:
            expression = self._stack.pop()

            if isinstance(expression, NotUnaryOperatorExpression):
                self._stack.append(expression.expression)
            else:
                self._stack.append(NotUnaryOperatorExpression(expression))
        elif (ctx.getToken(JSONPathParser.T__0, 0) is not None) or (ctx.getToken(JSONPathParser.T__14, 0) is not None):
            if bool(ctx.value()):
                right_value = self._stack.pop()

                if bool(ctx.subscript()):
                    next_node = self._stack.pop()
                else:
                    next_node = TerminalNode()

                if ctx.getToken(JSONPathParser.T__0, 0) is not None:
                    left_node = RootNode(next_node)
                elif ctx.getToken(JSONPathParser.T__14, 0) is not None:
                    left_node = CurrentNode(next_node)
                else:
                    raise ValueError()

                if ctx.getToken(JSONPathParser.T__15, 0) is not None:
                    self._stack.append(EqualBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.T__16, 0) is not None:
                    self._stack.append(NotEqualBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.T__17, 0) is not None:
                    self._stack.append(LessThanBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.T__18, 0) is not None:
                    self._stack.append(LessThanOrEqualToBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.T__19, 0) is not None:
                    self._stack.append(GreaterThanBinaryOperatorExpression(left_node, right_value))
                elif ctx.getToken(JSONPathParser.T__20, 0) is not None:
                    self._stack.append(GreaterThanOrEqualToBinaryOperatorExpression(left_node, right_value))
                else:
                    raise ValueError()
            else:
                if bool(ctx.subscript()):
                    next_node = self._stack.pop()
                else:
                    next_node = TerminalNode()

                self._stack.append(SomeExpression(CurrentNode(next_node)))
        else:
            pass

    def exitObj(self, ctx:JSONPathParser.ObjContext):
        values = []

        for pair_ctx in ctx.getTypedRuleContexts(JSONPathParser.PairContext):
            value = self._stack.pop()

            values.insert(0, value)

        obj = {}

        for index, pair_ctx in enumerate(ctx.getTypedRuleContexts(JSONPathParser.PairContext)):
            key = pair_ctx.STRING().getText()[1:-1]

            obj[key] = values[index]

        self._stack.append(obj)

    def exitArray(self, ctx:JSONPathParser.ArrayContext):
        array = []

        for value_ctx in ctx.getTypedRuleContexts(JSONPathParser.ValueContext):
            value = self._stack.pop()

            array.insert(0, value)

        self._stack.append(array)

    def exitValue(self, ctx:JSONPathParser.ValueContext):
        if bool(ctx.STRING()):
            text = ctx.STRING().getText()[1:-1]

            self._stack.append(text)
        elif bool(ctx.NUMBER()):
            text = ctx.NUMBER().getText()

            if ('.' in text) or ('E' in text) or ('e' in text):
                self._stack.append(float(text))
            else:
                self._stack.append(int(text))
        elif bool(ctx.obj()):
            pass
        elif bool(ctx.array()):
            pass
        elif ctx.getToken(JSONPathParser.T__23, 0) is not None:
            self._stack.append(True)
        elif ctx.getToken(JSONPathParser.T__24, 0) is not None:
            self._stack.append(False)
        elif ctx.getToken(JSONPathParser.T__25, 0) is not None:
            self._stack.append(None)
        else:
            raise ValueError()

def _parse_input_stream(input_stream:antlr4.InputStream) -> RootNode:
    lexer = JSONPathLexer(input_stream)

    token_stream = antlr4.CommonTokenStream(lexer)

    parser = JSONPathParser(token_stream)

    parser.addErrorListener(_ConsoleErrorListener())

    tree = parser.jsonpath()

    walker = antlr4.ParseTreeWalker()

    listener = _JSONPathListener(_stack=[])

    walker.walk(listener, tree)

    return listener._stack.pop()

def parse_file(*args, **kwargs) -> RootNode:
    file_stream = antlr4.FileStream(*args, **kwargs)

    return _parse_input_stream(file_stream)

def parse_str(*args, **kwargs) -> RootNode:
    input_stream = antlr4.InputStream(*args, **kwargs)

    return _parse_input_stream(input_stream)
