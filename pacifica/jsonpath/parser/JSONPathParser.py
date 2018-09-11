# Generated from pacifica/jsonpath/parser/JSONPath.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u00a2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\2\3\2\3\3\3\3\5\3\'")
        buf.write("\n\3\3\3\3\3\3\3\5\3,\n\3\3\3\5\3/\n\3\3\3\3\3\3\3\5\3")
        buf.write("\64\n\3\5\3\66\n\3\3\4\3\4\3\4\3\4\7\4<\n\4\f\4\16\4?")
        buf.write("\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\5\6I\n\6\3\6\3\6")
        buf.write("\5\6M\n\6\5\6O\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6W\n\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\5\b^\n\b\3\t\3\t\3\t\5\tc\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nm\n\n\3\n\3\n\5\nq\n\n\5")
        buf.write("\ns\n\n\3\13\3\13\3\f\3\f\3\f\3\f\7\f{\n\f\f\f\16\f~\13")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u0084\n\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\7\16\u008e\n\16\f\16\16\16\u0091\13\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u0097\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00a0\n\17\3\17\2\2\20\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\2\5\4\2\t\t\35\35\4\2\3\3")
        buf.write("\21\21\3\2\22\27\2\u00b1\2\36\3\2\2\2\4\65\3\2\2\2\6\67")
        buf.write("\3\2\2\2\bB\3\2\2\2\nV\3\2\2\2\fX\3\2\2\2\16Z\3\2\2\2")
        buf.write("\20_\3\2\2\2\22r\3\2\2\2\24t\3\2\2\2\26\u0083\3\2\2\2")
        buf.write("\30\u0085\3\2\2\2\32\u0096\3\2\2\2\34\u009f\3\2\2\2\36")
        buf.write(" \7\3\2\2\37!\5\4\3\2 \37\3\2\2\2 !\3\2\2\2!\"\3\2\2\2")
        buf.write("\"#\7\2\2\3#\3\3\2\2\2$&\5\6\4\2%\'\5\4\3\2&%\3\2\2\2")
        buf.write("&\'\3\2\2\2\'\66\3\2\2\2(+\7\4\2\2),\5\6\4\2*,\5\b\5\2")
        buf.write("+)\3\2\2\2+*\3\2\2\2,.\3\2\2\2-/\5\4\3\2.-\3\2\2\2./\3")
        buf.write("\2\2\2/\66\3\2\2\2\60\61\7\5\2\2\61\63\5\b\5\2\62\64\5")
        buf.write("\4\3\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65$\3")
        buf.write("\2\2\2\65(\3\2\2\2\65\60\3\2\2\2\66\5\3\2\2\2\678\7\6")
        buf.write("\2\28=\5\n\6\29:\7\7\2\2:<\5\n\6\2;9\3\2\2\2<?\3\2\2\2")
        buf.write("=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2@A\7\b\2\2A\7")
        buf.write("\3\2\2\2BC\t\2\2\2C\t\3\2\2\2DW\7\36\2\2EN\7\37\2\2FH")
        buf.write("\7\n\2\2GI\7\37\2\2HG\3\2\2\2HI\3\2\2\2IL\3\2\2\2JK\7")
        buf.write("\n\2\2KM\7\37\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NF\3\2")
        buf.write("\2\2NO\3\2\2\2OW\3\2\2\2PW\7\t\2\2QR\7\13\2\2RS\7\f\2")
        buf.write("\2ST\5\f\7\2TU\7\r\2\2UW\3\2\2\2VD\3\2\2\2VE\3\2\2\2V")
        buf.write("P\3\2\2\2VQ\3\2\2\2W\13\3\2\2\2XY\5\16\b\2Y\r\3\2\2\2")
        buf.write("Z]\5\20\t\2[\\\7\16\2\2\\^\5\16\b\2][\3\2\2\2]^\3\2\2")
        buf.write("\2^\17\3\2\2\2_b\5\22\n\2`a\7\17\2\2ac\5\20\t\2b`\3\2")
        buf.write("\2\2bc\3\2\2\2c\21\3\2\2\2de\7\20\2\2es\5\22\n\2fg\7\f")
        buf.write("\2\2gh\5\f\7\2hi\7\r\2\2is\3\2\2\2jl\t\3\2\2km\5\4\3\2")
        buf.write("lk\3\2\2\2lm\3\2\2\2mp\3\2\2\2no\t\4\2\2oq\5\34\17\2p")
        buf.write("n\3\2\2\2pq\3\2\2\2qs\3\2\2\2rd\3\2\2\2rf\3\2\2\2rj\3")
        buf.write("\2\2\2s\23\3\2\2\2tu\5\34\17\2u\25\3\2\2\2vw\7\30\2\2")
        buf.write("w|\5\30\r\2xy\7\7\2\2y{\5\30\r\2zx\3\2\2\2{~\3\2\2\2|")
        buf.write("z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2\2\177\u0080\7")
        buf.write("\31\2\2\u0080\u0084\3\2\2\2\u0081\u0082\7\30\2\2\u0082")
        buf.write("\u0084\7\31\2\2\u0083v\3\2\2\2\u0083\u0081\3\2\2\2\u0084")
        buf.write("\27\3\2\2\2\u0085\u0086\7\36\2\2\u0086\u0087\7\n\2\2\u0087")
        buf.write("\u0088\5\34\17\2\u0088\31\3\2\2\2\u0089\u008a\7\6\2\2")
        buf.write("\u008a\u008f\5\34\17\2\u008b\u008c\7\7\2\2\u008c\u008e")
        buf.write("\5\34\17\2\u008d\u008b\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0092\u0093\7\b\2\2\u0093\u0097\3")
        buf.write("\2\2\2\u0094\u0095\7\6\2\2\u0095\u0097\7\b\2\2\u0096\u0089")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0097\33\3\2\2\2\u0098\u00a0")
        buf.write("\7\36\2\2\u0099\u00a0\7\37\2\2\u009a\u00a0\5\26\f\2\u009b")
        buf.write("\u00a0\5\32\16\2\u009c\u00a0\7\32\2\2\u009d\u00a0\7\33")
        buf.write("\2\2\u009e\u00a0\7\34\2\2\u009f\u0098\3\2\2\2\u009f\u0099")
        buf.write("\3\2\2\2\u009f\u009a\3\2\2\2\u009f\u009b\3\2\2\2\u009f")
        buf.write("\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\35\3\2\2\2\27 &+.\63\65=HLNV]blpr|\u0083\u008f")
        buf.write("\u0096\u009f")
        return buf.getvalue()


class JSONPathParser ( Parser ):

    grammarFileName = "JSONPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'$'", "'..'", "'.'", "'['", "','", "']'", 
                     "'*'", "':'", "'?'", "'('", "')'", "'and'", "'or'", 
                     "'not'", "'@'", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'{'", "'}'", "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "NUMBER", "WS" ]

    RULE_jsonpath = 0
    RULE_subscript = 1
    RULE_subscriptables = 2
    RULE_subscriptableBareword = 3
    RULE_subscriptable = 4
    RULE_expression = 5
    RULE_andExpression = 6
    RULE_orExpression = 7
    RULE_notExpression = 8
    RULE_json = 9
    RULE_obj = 10
    RULE_pair = 11
    RULE_array = 12
    RULE_value = 13

    ruleNames =  [ "jsonpath", "subscript", "subscriptables", "subscriptableBareword", 
                   "subscriptable", "expression", "andExpression", "orExpression", 
                   "notExpression", "json", "obj", "pair", "array", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    ID=27
    STRING=28
    NUMBER=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonpathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            self.state = 28
            self.match(JSONPathParser.T__0)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__1) | (1 << JSONPathParser.T__2) | (1 << JSONPathParser.T__3))) != 0):
                self.state = 29
                self.subscript()


            self.state = 32
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

        def subscriptables(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptablesContext,0)


        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def subscriptableBareword(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptableBarewordContext,0)


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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.subscriptables()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__1) | (1 << JSONPathParser.T__2) | (1 << JSONPathParser.T__3))) != 0):
                    self.state = 35
                    self.subscript()


                pass
            elif token in [JSONPathParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(JSONPathParser.T__1)
                self.state = 41
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [JSONPathParser.T__3]:
                    self.state = 39
                    self.subscriptables()
                    pass
                elif token in [JSONPathParser.T__6, JSONPathParser.ID]:
                    self.state = 40
                    self.subscriptableBareword()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__1) | (1 << JSONPathParser.T__2) | (1 << JSONPathParser.T__3))) != 0):
                    self.state = 43
                    self.subscript()


                pass
            elif token in [JSONPathParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(JSONPathParser.T__2)
                self.state = 47
                self.subscriptableBareword()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__1) | (1 << JSONPathParser.T__2) | (1 << JSONPathParser.T__3))) != 0):
                    self.state = 48
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

        def subscriptable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.SubscriptableContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.SubscriptableContext,i)


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
            self.state = 53
            self.match(JSONPathParser.T__3)
            self.state = 54
            self.subscriptable()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSONPathParser.T__4:
                self.state = 55
                self.match(JSONPathParser.T__4)
                self.state = 56
                self.subscriptable()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(JSONPathParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptableBarewordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JSONPathParser.ID, 0)

        def getRuleIndex(self):
            return JSONPathParser.RULE_subscriptableBareword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptableBareword" ):
                listener.enterSubscriptableBareword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptableBareword" ):
                listener.exitSubscriptableBareword(self)




    def subscriptableBareword(self):

        localctx = JSONPathParser.SubscriptableBarewordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subscriptableBareword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==JSONPathParser.T__6 or _la==JSONPathParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def expression(self):
            return self.getTypedRuleContext(JSONPathParser.ExpressionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_subscriptable)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(JSONPathParser.NUMBER)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JSONPathParser.T__7:
                    self.state = 68
                    self.match(JSONPathParser.T__7)
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.NUMBER:
                        self.state = 69
                        self.match(JSONPathParser.NUMBER)


                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==JSONPathParser.T__7:
                        self.state = 72
                        self.match(JSONPathParser.T__7)
                        self.state = 73
                        self.match(JSONPathParser.NUMBER)




                pass
            elif token in [JSONPathParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(JSONPathParser.T__6)
                pass
            elif token in [JSONPathParser.T__8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(JSONPathParser.T__8)
                self.state = 80
                self.match(JSONPathParser.T__9)
                self.state = 81
                self.expression()
                self.state = 82
                self.match(JSONPathParser.T__10)
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
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
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
        self.enterRule(localctx, 12, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.orExpression()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.T__11:
                self.state = 89
                self.match(JSONPathParser.T__11)
                self.state = 90
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
        self.enterRule(localctx, 14, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.notExpression()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JSONPathParser.T__12:
                self.state = 94
                self.match(JSONPathParser.T__12)
                self.state = 95
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

        def notExpression(self):
            return self.getTypedRuleContext(JSONPathParser.NotExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(JSONPathParser.ExpressionContext,0)


        def subscript(self):
            return self.getTypedRuleContext(JSONPathParser.SubscriptContext,0)


        def value(self):
            return self.getTypedRuleContext(JSONPathParser.ValueContext,0)


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
        self.enterRule(localctx, 16, self.RULE_notExpression)
        self._la = 0 # Token type
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(JSONPathParser.T__13)
                self.state = 99
                self.notExpression()
                pass
            elif token in [JSONPathParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(JSONPathParser.T__9)
                self.state = 101
                self.expression()
                self.state = 102
                self.match(JSONPathParser.T__10)
                pass
            elif token in [JSONPathParser.T__0, JSONPathParser.T__14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                _la = self._input.LA(1)
                if not(_la==JSONPathParser.T__0 or _la==JSONPathParser.T__14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__1) | (1 << JSONPathParser.T__2) | (1 << JSONPathParser.T__3))) != 0):
                    self.state = 105
                    self.subscript()


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__15) | (1 << JSONPathParser.T__16) | (1 << JSONPathParser.T__17) | (1 << JSONPathParser.T__18) | (1 << JSONPathParser.T__19) | (1 << JSONPathParser.T__20))) != 0):
                    self.state = 108
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JSONPathParser.T__15) | (1 << JSONPathParser.T__16) | (1 << JSONPathParser.T__17) | (1 << JSONPathParser.T__18) | (1 << JSONPathParser.T__19) | (1 << JSONPathParser.T__20))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 109
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
        self.enterRule(localctx, 18, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
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

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.PairContext,i)


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
        self.enterRule(localctx, 20, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(JSONPathParser.T__21)
                self.state = 117
                self.pair()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.T__4:
                    self.state = 118
                    self.match(JSONPathParser.T__4)
                    self.state = 119
                    self.pair()
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 125
                self.match(JSONPathParser.T__22)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(JSONPathParser.T__21)
                self.state = 128
                self.match(JSONPathParser.T__22)
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
        self.enterRule(localctx, 22, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(JSONPathParser.STRING)
            self.state = 132
            self.match(JSONPathParser.T__7)
            self.state = 133
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONPathParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONPathParser.ValueContext,i)


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
        self.enterRule(localctx, 24, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(JSONPathParser.T__3)
                self.state = 136
                self.value()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONPathParser.T__4:
                    self.state = 137
                    self.match(JSONPathParser.T__4)
                    self.state = 138
                    self.value()
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 144
                self.match(JSONPathParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(JSONPathParser.T__3)
                self.state = 147
                self.match(JSONPathParser.T__5)
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
        self.enterRule(localctx, 26, self.RULE_value)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONPathParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(JSONPathParser.STRING)
                pass
            elif token in [JSONPathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(JSONPathParser.NUMBER)
                pass
            elif token in [JSONPathParser.T__21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.obj()
                pass
            elif token in [JSONPathParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.array()
                pass
            elif token in [JSONPathParser.T__23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.match(JSONPathParser.T__23)
                pass
            elif token in [JSONPathParser.T__24]:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.match(JSONPathParser.T__24)
                pass
            elif token in [JSONPathParser.T__25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 156
                self.match(JSONPathParser.T__25)
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





