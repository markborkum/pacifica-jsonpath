# Generated from pacifica/jsonpath/parser/JSONPath.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u0099\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\5\2\37\n\2\3\2\3\2\3\3\3\3\3\3\5\3&\n\3")
        buf.write("\3\3\3\3\5\3*\n\3\5\3,\n\3\3\4\3\4\3\4\3\4\7\4\62\n\4")
        buf.write("\f\4\16\4\65\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("?\n\5\3\5\3\5\3\5\5\5D\n\5\5\5F\n\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5N\n\5\3\6\3\6\3\7\3\7\3\7\5\7U\n\7\3\b\3\b\3")
        buf.write("\b\5\bZ\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\td\n\t\3")
        buf.write("\t\3\t\5\th\n\t\5\tj\n\t\3\n\3\n\3\13\3\13\3\13\3\13\7")
        buf.write("\13r\n\13\f\13\16\13u\13\13\3\13\3\13\3\13\3\13\5\13{")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u0085\n\r\f")
        buf.write("\r\16\r\u0088\13\r\3\r\3\r\3\r\3\r\5\r\u008e\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0097\n\16\3\16\2")
        buf.write("\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\4\2\3\3\5\5")
        buf.write("\3\2\b\r\2\u00a6\2\34\3\2\2\2\4+\3\2\2\2\6-\3\2\2\2\b")
        buf.write("M\3\2\2\2\nO\3\2\2\2\fQ\3\2\2\2\16V\3\2\2\2\20i\3\2\2")
        buf.write("\2\22k\3\2\2\2\24z\3\2\2\2\26|\3\2\2\2\30\u008d\3\2\2")
        buf.write("\2\32\u0096\3\2\2\2\34\36\7\5\2\2\35\37\5\4\3\2\36\35")
        buf.write("\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\7\2\2\3!\3\3\2\2")
        buf.write("\2\"#\7\4\2\2#%\5\6\4\2$&\5\4\3\2%$\3\2\2\2%&\3\2\2\2")
        buf.write("&,\3\2\2\2\')\5\6\4\2(*\5\4\3\2)(\3\2\2\2)*\3\2\2\2*,")
        buf.write("\3\2\2\2+\"\3\2\2\2+\'\3\2\2\2,\5\3\2\2\2-.\7\25\2\2.")
        buf.write("\63\5\b\5\2/\60\7\30\2\2\60\62\5\b\5\2\61/\3\2\2\2\62")
        buf.write("\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2")
        buf.write("\65\63\3\2\2\2\66\67\7\26\2\2\67\7\3\2\2\28N\7\35\2\2")
        buf.write("9:\7\36\2\2:E\6\5\2\2;>\7\27\2\2<=\7\36\2\2=?\6\5\3\2")
        buf.write("><\3\2\2\2>?\3\2\2\2?C\3\2\2\2@A\7\27\2\2AB\7\36\2\2B")
        buf.write("D\6\5\4\2C@\3\2\2\2CD\3\2\2\2DF\3\2\2\2E;\3\2\2\2EF\3")
        buf.write("\2\2\2FN\3\2\2\2GN\7\6\2\2HI\7\33\2\2IJ\7\31\2\2JK\5\n")
        buf.write("\6\2KL\7\32\2\2LN\3\2\2\2M8\3\2\2\2M9\3\2\2\2MG\3\2\2")
        buf.write("\2MH\3\2\2\2N\t\3\2\2\2OP\5\f\7\2P\13\3\2\2\2QT\5\16\b")
        buf.write("\2RS\7\7\2\2SU\5\f\7\2TR\3\2\2\2TU\3\2\2\2U\r\3\2\2\2")
        buf.write("VY\5\20\t\2WX\7\17\2\2XZ\5\16\b\2YW\3\2\2\2YZ\3\2\2\2")
        buf.write("Z\17\3\2\2\2[\\\7\16\2\2\\j\5\20\t\2]^\7\31\2\2^_\5\n")
        buf.write("\6\2_`\7\32\2\2`j\3\2\2\2ac\t\2\2\2bd\5\4\3\2cb\3\2\2")
        buf.write("\2cd\3\2\2\2dg\3\2\2\2ef\t\3\2\2fh\5\32\16\2ge\3\2\2\2")
        buf.write("gh\3\2\2\2hj\3\2\2\2i[\3\2\2\2i]\3\2\2\2ia\3\2\2\2j\21")
        buf.write("\3\2\2\2kl\5\32\16\2l\23\3\2\2\2mn\7\23\2\2ns\5\26\f\2")
        buf.write("op\7\30\2\2pr\5\26\f\2qo\3\2\2\2ru\3\2\2\2sq\3\2\2\2s")
        buf.write("t\3\2\2\2tv\3\2\2\2us\3\2\2\2vw\7\24\2\2w{\3\2\2\2xy\7")
        buf.write("\23\2\2y{\7\24\2\2zm\3\2\2\2zx\3\2\2\2{\25\3\2\2\2|}\7")
        buf.write("\35\2\2}~\7\27\2\2~\177\5\32\16\2\177\27\3\2\2\2\u0080")
        buf.write("\u0081\7\25\2\2\u0081\u0086\5\32\16\2\u0082\u0083\7\30")
        buf.write("\2\2\u0083\u0085\5\32\16\2\u0084\u0082\3\2\2\2\u0085\u0088")
        buf.write("\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a\7\26\2")
        buf.write("\2\u008a\u008e\3\2\2\2\u008b\u008c\7\25\2\2\u008c\u008e")
        buf.write("\7\26\2\2\u008d\u0080\3\2\2\2\u008d\u008b\3\2\2\2\u008e")
        buf.write("\31\3\2\2\2\u008f\u0097\7\35\2\2\u0090\u0097\7\36\2\2")
        buf.write("\u0091\u0097\5\24\13\2\u0092\u0097\5\30\r\2\u0093\u0097")
        buf.write("\7\20\2\2\u0094\u0097\7\21\2\2\u0095\u0097\7\22\2\2\u0096")
        buf.write("\u008f\3\2\2\2\u0096\u0090\3\2\2\2\u0096\u0091\3\2\2\2")
        buf.write("\u0096\u0092\3\2\2\2\u0096\u0093\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0095\3\2\2\2\u0097\33\3\2\2\2\25\36%)+\63")
        buf.write(">CEMTYcgisz\u0086\u008d\u0096")
        return buf.getvalue()


class JSONPathParser ( Parser ):

    grammarFileName = "JSONPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'..'", "'$'", "'*'", "'and'", 
                     "'='", "'>='", "'>'", "'<='", "'<'", "'!='", "'not'", 
                     "'or'", "'true'", "'false'", "'null'", "'{'", "'}'", 
                     "'['", "']'", "':'", "','", "'('", "')'", "'?'" ]

    symbolicNames = [ "<INVALID>", "CURRENT_VALUE", "RECURSIVE_DESCENT", 
                      "ROOT_VALUE", "WILDCARD_SUBSCRIPT", "AND", "EQ", "GE", 
                      "GT", "LE", "LT", "NE", "NOT", "OR", "TRUE", "FALSE", 
                      "NULL", "BRACE_LEFT", "BRACE_RIGHT", "BRACKET_LEFT", 
                      "BRACKET_RIGHT", "COLON", "COMMA", "PAREN_LEFT", "PAREN_RIGHT", 
                      "QUESTION", "ID", "STRING", "NUMBER", "WS" ]

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
    RECURSIVE_DESCENT=2
    ROOT_VALUE=3
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
            if _la==JSONPathParser.RECURSIVE_DESCENT or _la==JSONPathParser.BRACKET_LEFT:
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

        def RECURSIVE_DESCENT(self):
            return self.getToken(JSONPathParser.RECURSIVE_DESCENT, 0)

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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.RECURSIVE_DESCENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(JSONPathParser.RECURSIVE_DESCENT)
                self.state = 33
                self.subscriptables()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.RECURSIVE_DESCENT or _la==JSONPathParser.BRACKET_LEFT:
                    self.state = 34
                    self.subscript()


                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.subscriptables()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.RECURSIVE_DESCENT or _la==JSONPathParser.BRACKET_LEFT:
                    self.state = 38
                    self.subscript()


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

    class SubscriptablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKET_LEFT(self):
            return self.getToken(JSONPathParser.BRACKET_LEFT, 0)

        def subscriptable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.SubscriptableContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.SubscriptableContext,i)


        def BRACKET_RIGHT(self):
            return self.getToken(JSONPathParser.BRACKET_RIGHT, 0)

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
            self.state = 43
            self.match(JSONPathParser.BRACKET_LEFT)
            self.state = 44
            self.subscriptable()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSONPathParser.COMMA:
                self.state = 45
                self.match(JSONPathParser.COMMA)
                self.state = 46
                self.subscriptable()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(JSONPathParser.BRACKET_RIGHT)
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

        def WILDCARD_SUBSCRIPT(self):
            return self.getToken(JSONPathParser.WILDCARD_SUBSCRIPT, 0)

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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(JSONPathParser.NUMBER)
                self.state = 56
                if not self.tryCast(int):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.tryCast(int)")
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.COLON:
                    self.state = 57
                    self.match(JSONPathParser.COLON)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.NUMBER:
                        self.state = 58
                        self.match(JSONPathParser.NUMBER)
                        self.state = 59
                        if not self.tryCast(int):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.tryCast(int)")


                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.COLON:
                        self.state = 62
                        self.match(JSONPathParser.COLON)
                        self.state = 63
                        self.match(JSONPathParser.NUMBER)
                        self.state = 64
                        if not self.tryCast(int):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.tryCast(int)")




                pass
            elif token in [JSONPathParser.WILDCARD_SUBSCRIPT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(JSONPathParser.WILDCARD_SUBSCRIPT)
                pass
            elif token in [JSONPathParser.QUESTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(JSONPathParser.QUESTION)
                self.state = 71
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 72
                self.expression()
                self.state = 73
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
            self.state = 77
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
            self.state = 79
            self.orExpression()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.AND:
                self.state = 80
                self.match(JSONPathParser.AND)
                self.state = 81
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
            self.state = 84
            self.notExpression()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.OR:
                self.state = 85
                self.match(JSONPathParser.OR)
                self.state = 86
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
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(JSONPathParser.NOT)
                self.state = 90
                self.notExpression()
                pass
            elif token in [JSONPathParser.PAREN_LEFT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(JSONPathParser.PAREN_LEFT)
                self.state = 92
                self.expression()
                self.state = 93
                self.match(JSONPathParser.PAREN_RIGHT)
                pass
            elif token in [JSONPathParser.CURRENT_VALUE, JSONPathParser.ROOT_VALUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                _la = self._input.LA(1)
                if not(_la==JSONPathParser.CURRENT_VALUE or _la==JSONPathParser.ROOT_VALUE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.RECURSIVE_DESCENT or _la==JSONPathParser.BRACKET_LEFT:
                    self.state = 96
                    self.subscript()


                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0):
                    self.state = 99
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.EQ) | (1 << JSONPathParser.GE) | (1 << JSONPathParser.GT) | (1 << JSONPathParser.LE) | (1 << JSONPathParser.LT) | (1 << JSONPathParser.NE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 100
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
            self.state = 105
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 108
                self.pair()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 109
                    self.match(JSONPathParser.COMMA)
                    self.state = 110
                    self.pair()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 116
                self.match(JSONPathParser.BRACE_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(JSONPathParser.BRACE_LEFT)
                self.state = 119
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
            self.state = 122
            self.match(JSONPathParser.STRING)
            self.state = 123
            self.match(JSONPathParser.COLON)
            self.state = 124
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 127
                self.value()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.COMMA:
                    self.state = 128
                    self.match(JSONPathParser.COMMA)
                    self.state = 129
                    self.value()
                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 135
                self.match(JSONPathParser.BRACKET_RIGHT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(JSONPathParser.BRACKET_LEFT)
                self.state = 138
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(JSONPathParser.NUMBER)
                pass
            elif token in [JSONPathParser.BRACE_LEFT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.obj()
                pass
            elif token in [JSONPathParser.BRACKET_LEFT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.array()
                pass
            elif token in [JSONPathParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.match(JSONPathParser.TRUE)
                pass
            elif token in [JSONPathParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.match(JSONPathParser.FALSE)
                pass
            elif token in [JSONPathParser.NULL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
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
         




