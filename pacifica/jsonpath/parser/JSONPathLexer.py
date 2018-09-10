# Generated from pacifica/jsonpath/parser/JSONPath.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u00d8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\7\34\u0095\n\34\f\34\16\34\u0098\13\34")
        buf.write("\3\35\3\35\3\35\7\35\u009d\n\35\f\35\16\35\u00a0\13\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\5\36\u00a7\n\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\5\"\u00b4\n\"\3\"\3")
        buf.write("\"\3\"\6\"\u00b9\n\"\r\"\16\"\u00ba\5\"\u00bd\n\"\3\"")
        buf.write("\5\"\u00c0\n\"\3#\3#\3#\7#\u00c5\n#\f#\16#\u00c8\13#\5")
        buf.write("#\u00ca\n#\3$\3$\5$\u00ce\n$\3$\3$\3%\6%\u00d3\n%\r%\16")
        buf.write("%\u00d4\3%\3%\2\2&\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\2=\2")
        buf.write("?\2A\2C\37E\2G\2I \3\2\f\5\2C\\aac|\6\2\62;C\\aac|\n\2")
        buf.write("$$\61\61^^ddhhppttvv\5\2\62;CHch\5\2\2!$$^^\3\2\62;\3")
        buf.write("\2\63;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u00dd\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2C\3\2\2\2\2I\3\2\2\2\3K\3\2\2\2\5")
        buf.write("M\3\2\2\2\7O\3\2\2\2\tQ\3\2\2\2\13T\3\2\2\2\rV\3\2\2\2")
        buf.write("\17X\3\2\2\2\21Z\3\2\2\2\23\\\3\2\2\2\25^\3\2\2\2\27`")
        buf.write("\3\2\2\2\31b\3\2\2\2\33f\3\2\2\2\35i\3\2\2\2\37m\3\2\2")
        buf.write("\2!o\3\2\2\2#q\3\2\2\2%t\3\2\2\2\'v\3\2\2\2)y\3\2\2\2")
        buf.write("+{\3\2\2\2-~\3\2\2\2/\u0080\3\2\2\2\61\u0082\3\2\2\2\63")
        buf.write("\u0087\3\2\2\2\65\u008d\3\2\2\2\67\u0092\3\2\2\29\u0099")
        buf.write("\3\2\2\2;\u00a3\3\2\2\2=\u00a8\3\2\2\2?\u00ae\3\2\2\2")
        buf.write("A\u00b0\3\2\2\2C\u00b3\3\2\2\2E\u00c9\3\2\2\2G\u00cb\3")
        buf.write("\2\2\2I\u00d2\3\2\2\2KL\7&\2\2L\4\3\2\2\2MN\7]\2\2N\6")
        buf.write("\3\2\2\2OP\7_\2\2P\b\3\2\2\2QR\7\60\2\2RS\7\60\2\2S\n")
        buf.write("\3\2\2\2TU\7\60\2\2U\f\3\2\2\2VW\7.\2\2W\16\3\2\2\2XY")
        buf.write("\7,\2\2Y\20\3\2\2\2Z[\7<\2\2[\22\3\2\2\2\\]\7A\2\2]\24")
        buf.write("\3\2\2\2^_\7*\2\2_\26\3\2\2\2`a\7+\2\2a\30\3\2\2\2bc\7")
        buf.write("c\2\2cd\7p\2\2de\7f\2\2e\32\3\2\2\2fg\7q\2\2gh\7t\2\2")
        buf.write("h\34\3\2\2\2ij\7p\2\2jk\7q\2\2kl\7v\2\2l\36\3\2\2\2mn")
        buf.write("\7B\2\2n \3\2\2\2op\7?\2\2p\"\3\2\2\2qr\7#\2\2rs\7?\2")
        buf.write("\2s$\3\2\2\2tu\7>\2\2u&\3\2\2\2vw\7>\2\2wx\7?\2\2x(\3")
        buf.write("\2\2\2yz\7@\2\2z*\3\2\2\2{|\7@\2\2|}\7?\2\2},\3\2\2\2")
        buf.write("~\177\7}\2\2\177.\3\2\2\2\u0080\u0081\7\177\2\2\u0081")
        buf.write("\60\3\2\2\2\u0082\u0083\7v\2\2\u0083\u0084\7t\2\2\u0084")
        buf.write("\u0085\7w\2\2\u0085\u0086\7g\2\2\u0086\62\3\2\2\2\u0087")
        buf.write("\u0088\7h\2\2\u0088\u0089\7c\2\2\u0089\u008a\7n\2\2\u008a")
        buf.write("\u008b\7u\2\2\u008b\u008c\7g\2\2\u008c\64\3\2\2\2\u008d")
        buf.write("\u008e\7p\2\2\u008e\u008f\7w\2\2\u008f\u0090\7n\2\2\u0090")
        buf.write("\u0091\7n\2\2\u0091\66\3\2\2\2\u0092\u0096\t\2\2\2\u0093")
        buf.write("\u0095\t\3\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u00978\3\2\2")
        buf.write("\2\u0098\u0096\3\2\2\2\u0099\u009e\7$\2\2\u009a\u009d")
        buf.write("\5;\36\2\u009b\u009d\5A!\2\u009c\u009a\3\2\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a1\u00a2\7$\2\2\u00a2:\3\2\2\2\u00a3\u00a6\7^\2\2")
        buf.write("\u00a4\u00a7\t\4\2\2\u00a5\u00a7\5=\37\2\u00a6\u00a4\3")
        buf.write("\2\2\2\u00a6\u00a5\3\2\2\2\u00a7<\3\2\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\5? \2\u00aa\u00ab\5? \2\u00ab\u00ac")
        buf.write("\5? \2\u00ac\u00ad\5? \2\u00ad>\3\2\2\2\u00ae\u00af\t")
        buf.write("\5\2\2\u00af@\3\2\2\2\u00b0\u00b1\n\6\2\2\u00b1B\3\2\2")
        buf.write("\2\u00b2\u00b4\7/\2\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00bc\5E#\2\u00b6\u00b8")
        buf.write("\7\60\2\2\u00b7\u00b9\t\7\2\2\u00b8\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bd\3\2\2\2\u00bc\u00b6\3\2\2\2\u00bc\u00bd\3")
        buf.write("\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00c0\5G$\2\u00bf\u00be")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0D\3\2\2\2\u00c1\u00ca")
        buf.write("\7\62\2\2\u00c2\u00c6\t\b\2\2\u00c3\u00c5\t\7\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c9\u00c1\3\2\2\2\u00c9\u00c2\3\2\2\2\u00caF")
        buf.write("\3\2\2\2\u00cb\u00cd\t\t\2\2\u00cc\u00ce\t\n\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\5E#\2\u00d0H\3\2\2\2\u00d1\u00d3\t\13\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7")
        buf.write("\b%\2\2\u00d7J\3\2\2\2\17\2\u0096\u009c\u009e\u00a6\u00b3")
        buf.write("\u00ba\u00bc\u00bf\u00c6\u00c9\u00cd\u00d4\3\b\2\2")
        return buf.getvalue()


class JSONPathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    ID = 27
    STRING = 28
    NUMBER = 29
    WS = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'$'", "'['", "']'", "'..'", "'.'", "','", "'*'", "':'", "'?'", 
            "'('", "')'", "'and'", "'or'", "'not'", "'@'", "'='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'{'", "'}'", "'true'", "'false'", 
            "'null'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "ID", "STRING", "ESC", "UNICODE", "HEX", "SAFECODEPOINT", 
                  "NUMBER", "INT", "EXP", "WS" ]

    grammarFileName = "JSONPath.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


