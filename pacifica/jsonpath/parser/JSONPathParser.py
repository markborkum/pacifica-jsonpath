# Generated from pacifica/jsonpath/parser/JSONPath.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u0094\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\5\2\37\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\'")
        buf.write("\n\3\3\3\3\3\5\3+\n\3\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4")
        buf.write("\63\13\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5;\n\5\3\5\3\5\3\5")
        buf.write("\5\5@\n\5\5\5B\n\5\3\5\3\5\3\5\3\5\3\5\5\5I\n\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\5\7P\n\7\3\b\3\b\3\b\5\bU\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\t_\n\t\3\t\3\t\5\tc\n\t\5\te")
        buf.write("\n\t\3\n\3\n\3\13\3\13\3\13\3\13\7\13m\n\13\f\13\16\13")
        buf.write("p\13\13\3\13\3\13\3\13\3\13\5\13v\n\13\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u0080\n\r\f\r\16\r\u0083\13\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u0089\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u0092\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\2\4\3\2\3\4\3\2\b\r\2\u00a0\2\34\3\2\2")
        buf.write("\2\4\"\3\2\2\2\6,\3\2\2\2\bH\3\2\2\2\nJ\3\2\2\2\fL\3\2")
        buf.write("\2\2\16Q\3\2\2\2\20d\3\2\2\2\22f\3\2\2\2\24u\3\2\2\2\26")
        buf.write("w\3\2\2\2\30\u0088\3\2\2\2\32\u0091\3\2\2\2\34\36\7\4")
        buf.write("\2\2\35\37\5\4\3\2\36\35\3\2\2\2\36\37\3\2\2\2\37 \3\2")
        buf.write("\2\2 !\7\2\2\3!\3\3\2\2\2\"&\7\25\2\2#\'\7\5\2\2$\'\7")
        buf.write("\6\2\2%\'\5\6\4\2&#\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'(\3\2")
        buf.write("\2\2(*\7\26\2\2)+\5\4\3\2*)\3\2\2\2*+\3\2\2\2+\5\3\2\2")
        buf.write("\2,\61\5\b\5\2-.\7\30\2\2.\60\5\b\5\2/-\3\2\2\2\60\63")
        buf.write("\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\7\3\2\2\2\63\61")
        buf.write("\3\2\2\2\64I\7\35\2\2\65\66\7\36\2\2\66A\6\5\2\2\67:\7")
        buf.write("\27\2\289\7\36\2\29;\6\5\3\2:8\3\2\2\2:;\3\2\2\2;?\3\2")
        buf.write("\2\2<=\7\27\2\2=>\7\36\2\2>@\6\5\4\2?<\3\2\2\2?@\3\2\2")
        buf.write("\2@B\3\2\2\2A\67\3\2\2\2AB\3\2\2\2BI\3\2\2\2CD\7\33\2")
        buf.write("\2DE\7\31\2\2EF\5\n\6\2FG\7\32\2\2GI\3\2\2\2H\64\3\2\2")
        buf.write("\2H\65\3\2\2\2HC\3\2\2\2I\t\3\2\2\2JK\5\f\7\2K\13\3\2")
        buf.write("\2\2LO\5\16\b\2MN\7\7\2\2NP\5\f\7\2OM\3\2\2\2OP\3\2\2")
        buf.write("\2P\r\3\2\2\2QT\5\20\t\2RS\7\17\2\2SU\5\16\b\2TR\3\2\2")
        buf.write("\2TU\3\2\2\2U\17\3\2\2\2VW\7\16\2\2We\5\20\t\2XY\7\31")
        buf.write("\2\2YZ\5\n\6\2Z[\7\32\2\2[e\3\2\2\2\\^\t\2\2\2]_\5\4\3")
        buf.write("\2^]\3\2\2\2^_\3\2\2\2_b\3\2\2\2`a\t\3\2\2ac\5\32\16\2")
        buf.write("b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2dV\3\2\2\2dX\3\2\2\2d\\")
        buf.write("\3\2\2\2e\21\3\2\2\2fg\5\32\16\2g\23\3\2\2\2hi\7\23\2")
        buf.write("\2in\5\26\f\2jk\7\30\2\2km\5\26\f\2lj\3\2\2\2mp\3\2\2")
        buf.write("\2nl\3\2\2\2no\3\2\2\2oq\3\2\2\2pn\3\2\2\2qr\7\24\2\2")
        buf.write("rv\3\2\2\2st\7\23\2\2tv\7\24\2\2uh\3\2\2\2us\3\2\2\2v")
        buf.write("\25\3\2\2\2wx\7\35\2\2xy\7\27\2\2yz\5\32\16\2z\27\3\2")
        buf.write("\2\2{|\7\25\2\2|\u0081\5\32\16\2}~\7\30\2\2~\u0080\5\32")
        buf.write("\16\2\177}\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\7\26\2\2\u0085\u0089\3\2\2\2\u0086")
        buf.write("\u0087\7\25\2\2\u0087\u0089\7\26\2\2\u0088{\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0089\31\3\2\2\2\u008a\u0092\7\35\2\2\u008b")
        buf.write("\u0092\7\36\2\2\u008c\u0092\5\24\13\2\u008d\u0092\5\30")
        buf.write("\r\2\u008e\u0092\7\20\2\2\u008f\u0092\7\21\2\2\u0090\u0092")
        buf.write("\7\22\2\2\u0091\u008a\3\2\2\2\u0091\u008b\3\2\2\2\u0091")
        buf.write("\u008c\3\2\2\2\u0091\u008d\3\2\2\2\u0091\u008e\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\33\3\2")
        buf.write("\2\2\24\36&*\61:?AHOT^bdnu\u0081\u0088\u0091")
        return buf.getvalue()


class JSONPathParser ( Parser ):

    grammarFileName = "JSONPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'$'", "'**'", "'*'", "'and'", 
                     "'='", "'>='", "'>'", "'<='", "'<'", "'!='", "'not'", 
                     "'or'", "'true'", "'false'", "'null'", "'{'", "'}'", 
                     "'['", "']'", "':'", "','", "'('", "')'", "'?'" ]

    symbolicNames = [ "<INVALID>", "CURRENT_VALUE", "ROOT_VALUE", "RECURSIVE_DESCENT_SUBSCRIPT", 
                      "WILDCARD_SUBSCRIPT", "AND", "EQ", "GE", "GT", "LE", 
                      "LT", "NE", "NOT", "OR", "TRUE", "FALSE", "NULL", 
                      "BRACE_LEFT", "BRACE_RIGHT", "BRACKET_LEFT", "BRACKET_RIGHT", 
                      "COLON", "COMMA", "PAREN_LEFT", "PAREN_RIGHT", "QUESTION", 
                      "ID", "STRING", "NUMBER", "WS" ]

    RULE_jsonpath = 0
    RULE_subscript = 1
    RULE_subscriptables = 2
    RULE_subscriptable = 3
    RULE_expression = 4
    RULE_andExpression = 5
    RULE_orExpression = 6
    RULE_notExpression = 7
    RULE_json = 8
    RULE_obj = 9
    RULE_pair = 10
    RULE_array = 11
    RULE_value = 12

    ruleNames =  [ "jsonpath", "subscript", "subscriptables", "subscriptable", 
                   "expression", "andExpression", "orExpression", "notExpression", 
                   "json", "obj", "pair", "array", "value" ]

    EOF = Token.EOF
    CURRENT_VALUE=1
    ROOT_VALUE=2
    RECURSIVE_DESCENT_SUBSCRIPT=3
    WILDCARD_SUBSCRIPT=4
    AND=5
    EQ=6
    GE=7
    GT=8
    LE=9
    LT=10
    NE=11
    NOT=12
    OR=13
    TRUE=14
    FALSE=15
    NULL=16
    BRACE_LEFT=17
    BRACE_RIGHT=18
    BRACKET_LEFT=19
    BRACKET_RIGHT=20
    COLON=21
    COMMA=22
    PAREN_LEFT=23
    PAREN_RIGHT=24
    QUESTION=25
    ID=26
    STRING=27
    NUMBER=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonpathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT_VALUE(self):
            return self.getToken(JSONPathParser.ROOT_VALUE, 0)

        def EOF(self):
            return self.getToken(JSONPathParser.EOF, 0)

        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_jsonpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJsonpath" ):
                listener.enterJsonpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJsonpath" ):
                listener.exitJsonpath(self)




    def jsonpath(self):

        localctx = JSONPathParser.JsonpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_jsonpath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(JSONPathParser.ROOT_VALUE)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.BRACKET_LEFT:
                self.state = 27
                self.subscript()


            self.state = 30
            self.match(JSONPathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(JSONPathParser.BRACKET_LEFT, 0)

        def BRACKET_RIGHT(self):
            return self.getToken(JSONPathParser.BRACKET_RIGHT, 0)

        def RECURSIVE_DESCENT_SUBSCRIPT(self):
            return self.getToken(JSONPathParser.RECURSIVE_DESCENT_SUBSCRIPT, 0)

        def WILDCARD_SUBSCRIPT(self):
            return self.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0)

        def subscriptables(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptablesContext,0)


        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_subscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript" ):
                listener.enterSubscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript" ):
                listener.exitSubscript(self)




    def subscript(self):

        localctx = JSONPathParser.SubscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subscript)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(JSONPathParser.BRACKET_LEFT)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.RECURSIVE_DESCENT_SUBSCRIPT]:
                self.state = 33
                self.match(JSONPathParser.RECURSIVE_DESCENT_SUBSCRIPT)
                pass
            elif token in [JSONPathParser.WILDCARD_SUBSCRIPT]:
                self.state = 34
                self.match(JSONPathParser.WILDCARD_SUBSCRIPT)
                pass
            elif token in [JSONPathParser.QUESTION, JSONPathParser.STRING, JSONPathParser.NUMBER]:
                self.state = 35
                self.subscriptables()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 38
            self.match(JSONPathParser.BRACKET_RIGHT)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.BRACKET_LEFT:
                self.state = 39
                self.subscript()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscriptable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.SubscriptableContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.SubscriptableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptables" ):
                listener.enterSubscriptables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptables" ):
                listener.exitSubscriptables(self)




    def subscriptables(self):

        localctx = JSONPathParser.SubscriptablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subscriptables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.subscriptable()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSONPathParser.COMMA:
                self.state = 43
                self.match(JSONPathParser.COMMA)
                self.state = 44
                self.subscriptable()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.NUMBER)
            else:
                return self.getToken(JSONPathParser.NUMBER, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COLON)
            else:
                return self.getToken(JSONPathParser.COLON, i)

        def QUESTION(self):
            return self.getToken(JSONPathParser.QUESTION, 0)

        def PAREN_LEFT(self):
            return self.getToken(JSONPathParser.PAREN_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(JSONPathParser.ExpressionContext,0)


        def PAREN_RIGHT(self):
            return self.getToken(JSONPathParser.PAREN_RIGHT, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptable" ):
                listener.enterSubscriptable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptable" ):
                listener.exitSubscriptable(self)




    def subscriptable(self):

        localctx = JSONPathParser.SubscriptableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subscriptable)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(JSONPathParser.NUMBER)
                self.state = 52
                if not self.tryCast(int):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.tryCast(int)")
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.COLON:
                    self.state = 53
                    self.match(JSONPathParser.COLON)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.NUMBER:
                        self.state = 54
                        self.match(JSONPathParser.NUMBER)
                        self.state = 55
                        if not self.tryCast(int):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.tryCast(int)")


                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.COLON:
                        self.state = 58
                        self.match(JSONPathParser.COLON)
                        self.state = 59
                        self.match(JSONPathParser.NUMBER)
                        self.state = 60
                        if not self.tryCast(int):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.tryCast(int)")




                pass
            elif token in [JSONPathParser.QUESTION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(JSONPathParser.QUESTION)
                self.state = 66
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 67
                self.expression()
                self.state = 68
                self.match(JSONPathParser.PAREN_RIGHT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self):
            return self.getTypedRuleContext(JSONPathParser.AndExpressionContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = JSONPathParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.andExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AndExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpression(self):
            return self.getTypedRuleContext(JSONPathParser.OrExpressionContext,0)


        def AND(self):
            return self.getToken(JSONPathParser.AND, 0)

        def andExpression(self):
            return self.getTypedRuleContext(JSONPathParser.AndExpressionContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_andExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)




    def andExpression(self):

        localctx = JSONPathParser.AndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.orExpression()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.AND:
                self.state = 75
                self.match(JSONPathParser.AND)
                self.state = 76
                self.andExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpression(self):
            return self.getTypedRuleContext(JSONPathParser.NotExpressionContext,0)


        def OR(self):
            return self.getToken(JSONPathParser.OR, 0)

        def orExpression(self):
            return self.getTypedRuleContext(JSONPathParser.OrExpressionContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_orExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)




    def orExpression(self):

        localctx = JSONPathParser.OrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.notExpression()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.OR:
                self.state = 80
                self.match(JSONPathParser.OR)
                self.state = 81
                self.orExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NotExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(JSONPathParser.NOT, 0)

        def notExpression(self):
            return self.getTypedRuleContext(JSONPathParser.NotExpressionContext,0)


        def PAREN_LEFT(self):
            return self.getToken(JSONPathParser.PAREN_LEFT, 0)

        def expression(self):
            return self.getTypedRuleContext(JSONPathParser.ExpressionContext,0)


        def PAREN_RIGHT(self):
            return self.getToken(JSONPathParser.PAREN_RIGHT, 0)

        def ROOT_VALUE(self):
            return self.getToken(JSONPathParser.ROOT_VALUE, 0)

        def CURRENT_VALUE(self):
            return self.getToken(JSONPathParser.CURRENT_VALUE, 0)

        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


        def EQ(self):
            return self.getToken(JSONPathParser.EQ, 0)

        def NE(self):
            return self.getToken(JSONPathParser.NE, 0)

        def LT(self):
            return self.getToken(JSONPathParser.LT, 0)

        def LE(self):
            return self.getToken(JSONPathParser.LE, 0)

        def GT(self):
            return self.getToken(JSONPathParser.GT, 0)

        def GE(self):
            return self.getToken(JSONPathParser.GE, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_notExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)




    def notExpression(self):

        localctx = JSONPathParser.NotExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_notExpression)
        self._la = 0 # Token type
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(JSONPathParser.NOT)
                self.state = 85
                self.notExpression()
                pass
            elif token in [JSONPathParser.PAREN_LEFT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 87
                self.expression()
                self.state = 88
                self.match(JSONPathParser.PAREN_RIGHT)
                pass
            elif token in [JSONPathParser.CURRENT_VALUE, JSONPathParser.ROOT_VALUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                _la = self._input.LA(1)
                if not(_la==JSONPathParser.CURRENT_VALUE or _la==JSONPathParser.ROOT_VALUE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.BRACKET_LEFT:
                    self.state = 91
                    self.subscript()


                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0):
                    self.state = 94
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 95
                    self.value()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = JSONPathParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_LEFT(self):
            return self.getToken(JSONPathParser.BRACE_LEFT, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.PairContext,i)


        def BRACE_RIGHT(self):
            return self.getToken(JSONPathParser.BRACE_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self):

        localctx = JSONPathParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 103
                self.pair()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 104
                    self.match(JSONPathParser.COMMA)
                    self.state = 105
                    self.pair()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 111
                self.match(JSONPathParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 114
                self.match(JSONPathParser.BRACE_RIGHT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def COLON(self):
            return self.getToken(JSONPathParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONPathParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = JSONPathParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(JSONPathParser.STRING)
            self.state = 118
            self.match(JSONPathParser.COLON)
            self.state = 119
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(JSONPathParser.BRACKET_LEFT, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.ValueContext,i)


        def BRACKET_RIGHT(self):
            return self.getToken(JSONPathParser.BRACKET_RIGHT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JSONPathParser.COMMA)
            else:
                return self.getToken(JSONPathParser.COMMA, i)

        def getRuleIndex(self):
            return JSONPathParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = JSONPathParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 122
                self.value()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 123
                    self.match(JSONPathParser.COMMA)
                    self.state = 124
                    self.value()
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self.match(JSONPathParser.BRACKET_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 133
                self.match(JSONPathParser.BRACKET_RIGHT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONPathParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(JSONPathParser.NUMBER, 0)

        def obj(self):
            return self.getTypedRuleContext(JSONPathParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JSONPathParser.ArrayContext,0)


        def TRUE(self):
            return self.getToken(JSONPathParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(JSONPathParser.FALSE, 0)

        def NULL(self):
            return self.getToken(JSONPathParser.NULL, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = JSONPathParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(JSONPathParser.NUMBER)
                pass
            elif token in [JSONPathParser.BRACE_LEFT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.obj()
                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.array()
                pass
            elif token in [JSONPathParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.match(JSONPathParser.TRUE)
                pass
            elif token in [JSONPathParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.match(JSONPathParser.FALSE)
                pass
            elif token in [JSONPathParser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.match(JSONPathParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.subscriptable_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def subscriptable_sempred(self, localctx:SubscriptableContext, predIndex:int):
            if predIndex == 0:
                return self.tryCast(int)
         

            if predIndex == 1:
                return self.tryCast(int)
         

            if predIndex == 2:
                return self.tryCast(int)
         




