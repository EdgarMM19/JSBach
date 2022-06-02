# Generated from jsbach.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,172,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,4,
        1,29,8,1,11,1,12,1,30,1,2,1,2,1,2,1,2,1,2,1,2,1,3,5,3,40,8,3,10,
        3,12,3,43,9,3,1,4,1,4,1,4,1,4,1,4,4,4,50,8,4,11,4,12,4,51,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,95,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,116,8,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,
        133,8,5,10,5,12,5,136,9,5,1,6,5,6,139,8,6,10,6,12,6,142,9,6,1,7,
        5,7,145,8,7,10,7,12,7,148,9,7,1,8,1,8,1,8,1,8,1,9,1,9,3,9,156,8,
        9,1,10,1,10,1,10,3,10,161,8,10,1,11,1,11,5,11,165,8,11,10,11,12,
        11,168,9,11,1,11,1,11,1,11,0,1,10,12,0,2,4,6,8,10,12,14,16,18,20,
        22,0,0,191,0,24,1,0,0,0,2,28,1,0,0,0,4,32,1,0,0,0,6,41,1,0,0,0,8,
        94,1,0,0,0,10,115,1,0,0,0,12,140,1,0,0,0,14,146,1,0,0,0,16,149,1,
        0,0,0,18,155,1,0,0,0,20,160,1,0,0,0,22,162,1,0,0,0,24,25,3,2,1,0,
        25,26,5,0,0,1,26,1,1,0,0,0,27,29,3,4,2,0,28,27,1,0,0,0,29,30,1,0,
        0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,3,1,0,0,0,32,33,5,24,0,0,33,34,
        3,12,6,0,34,35,5,1,0,0,35,36,3,6,3,0,36,37,5,2,0,0,37,5,1,0,0,0,
        38,40,3,8,4,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,
        0,0,0,42,7,1,0,0,0,43,41,1,0,0,0,44,45,5,23,0,0,45,46,5,3,0,0,46,
        95,3,18,9,0,47,49,5,4,0,0,48,50,3,20,10,0,49,48,1,0,0,0,50,51,1,
        0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,95,1,0,0,0,53,54,5,5,0,0,54,
        95,5,23,0,0,55,56,5,6,0,0,56,95,3,10,5,0,57,58,5,6,0,0,58,95,3,22,
        11,0,59,60,5,7,0,0,60,61,3,16,8,0,61,62,5,1,0,0,62,63,3,6,3,0,63,
        64,5,2,0,0,64,65,5,8,0,0,65,66,5,1,0,0,66,67,3,6,3,0,67,68,5,2,0,
        0,68,95,1,0,0,0,69,70,5,7,0,0,70,71,3,16,8,0,71,72,5,1,0,0,72,73,
        3,6,3,0,73,74,5,2,0,0,74,95,1,0,0,0,75,76,5,9,0,0,76,77,3,16,8,0,
        77,78,5,1,0,0,78,79,3,6,3,0,79,80,5,2,0,0,80,95,1,0,0,0,81,82,5,
        23,0,0,82,83,5,10,0,0,83,95,3,10,5,0,84,85,5,11,0,0,85,86,5,23,0,
        0,86,87,5,12,0,0,87,88,3,10,5,0,88,89,5,13,0,0,89,95,1,0,0,0,90,
        91,5,14,0,0,91,95,3,10,5,0,92,93,5,24,0,0,93,95,3,14,7,0,94,44,1,
        0,0,0,94,47,1,0,0,0,94,53,1,0,0,0,94,55,1,0,0,0,94,57,1,0,0,0,94,
        59,1,0,0,0,94,69,1,0,0,0,94,75,1,0,0,0,94,81,1,0,0,0,94,84,1,0,0,
        0,94,90,1,0,0,0,94,92,1,0,0,0,95,9,1,0,0,0,96,97,6,5,-1,0,97,98,
        5,15,0,0,98,99,3,10,5,0,99,100,5,16,0,0,100,116,1,0,0,0,101,102,
        5,17,0,0,102,116,5,23,0,0,103,104,5,23,0,0,104,105,5,12,0,0,105,
        106,3,10,5,0,106,107,5,13,0,0,107,116,1,0,0,0,108,109,5,29,0,0,109,
        116,3,10,5,5,110,116,5,25,0,0,111,116,5,23,0,0,112,116,5,21,0,0,
        113,114,5,24,0,0,114,116,3,14,7,0,115,96,1,0,0,0,115,101,1,0,0,0,
        115,103,1,0,0,0,115,108,1,0,0,0,115,110,1,0,0,0,115,111,1,0,0,0,
        115,112,1,0,0,0,115,113,1,0,0,0,116,134,1,0,0,0,117,118,10,10,0,
        0,118,119,5,28,0,0,119,133,3,10,5,11,120,121,10,9,0,0,121,122,5,
        27,0,0,122,133,3,10,5,10,123,124,10,8,0,0,124,125,5,30,0,0,125,133,
        3,10,5,9,126,127,10,7,0,0,127,128,5,26,0,0,128,133,3,10,5,8,129,
        130,10,6,0,0,130,131,5,29,0,0,131,133,3,10,5,7,132,117,1,0,0,0,132,
        120,1,0,0,0,132,123,1,0,0,0,132,126,1,0,0,0,132,129,1,0,0,0,133,
        136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,11,1,0,0,0,136,134,
        1,0,0,0,137,139,5,23,0,0,138,137,1,0,0,0,139,142,1,0,0,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,13,1,0,0,0,142,140,1,0,0,0,143,145,3,
        10,5,0,144,143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,
        0,0,0,147,15,1,0,0,0,148,146,1,0,0,0,149,150,3,10,5,0,150,151,5,
        31,0,0,151,152,3,10,5,0,152,17,1,0,0,0,153,156,3,10,5,0,154,156,
        3,22,11,0,155,153,1,0,0,0,155,154,1,0,0,0,156,19,1,0,0,0,157,161,
        3,10,5,0,158,161,3,22,11,0,159,161,5,20,0,0,160,157,1,0,0,0,160,
        158,1,0,0,0,160,159,1,0,0,0,161,21,1,0,0,0,162,166,5,18,0,0,163,
        165,3,10,5,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,169,1,0,0,0,168,166,1,0,0,0,169,170,5,19,0,0,170,
        23,1,0,0,0,12,30,41,51,94,115,132,134,140,146,155,160,166
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'<-'", "'<!>'", "'<?>'", 
                     "'<:>'", "'if'", "'else'", "'while'", "'<<'", "'8<'", 
                     "'['", "']'", "'r\\u00FCck'", "'('", "')'", "'#'", 
                     "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'/'", "'-'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STR", "NOTE", "LN", "VAR", "FNME", "NUM", "ADD", 
                      "MULT", "DIV", "SUBS", "REM", "COMP", "WS", "COMMENT" ]

    RULE_root = 0
    RULE_functions = 1
    RULE_func = 2
    RULE_codeblock = 3
    RULE_line = 4
    RULE_expr = 5
    RULE_fheader = 6
    RULE_param = 7
    RULE_cond = 8
    RULE_assignable = 9
    RULE_printable = 10
    RULE_list = 11

    ruleNames =  [ "root", "functions", "func", "codeblock", "line", "expr", 
                   "fheader", "param", "cond", "assignable", "printable", 
                   "list" ]

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
    STR=20
    NOTE=21
    LN=22
    VAR=23
    FNME=24
    NUM=25
    ADD=26
    MULT=27
    DIV=28
    SUBS=29
    REM=30
    COMP=31
    WS=32
    COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functions(self):
            return self.getTypedRuleContext(jsbachParser.FunctionsContext,0)


        def EOF(self):
            return self.getToken(jsbachParser.EOF, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = jsbachParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.functions()
            self.state = 25
            self.match(jsbachParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.FuncContext)
            else:
                return self.getTypedRuleContext(jsbachParser.FuncContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_functions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = jsbachParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.func()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==jsbachParser.FNME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FNME(self):
            return self.getToken(jsbachParser.FNME, 0)

        def fheader(self):
            return self.getTypedRuleContext(jsbachParser.FheaderContext,0)


        def codeblock(self):
            return self.getTypedRuleContext(jsbachParser.CodeblockContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = jsbachParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(jsbachParser.FNME)
            self.state = 33
            self.fheader()
            self.state = 34
            self.match(jsbachParser.T__0)
            self.state = 35
            self.codeblock()
            self.state = 36
            self.match(jsbachParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.LineContext)
            else:
                return self.getTypedRuleContext(jsbachParser.LineContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_codeblock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodeblock" ):
                return visitor.visitCodeblock(self)
            else:
                return visitor.visitChildren(self)




    def codeblock(self):

        localctx = jsbachParser.CodeblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_codeblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__3) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__5) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__8) | (1 << jsbachParser.T__10) | (1 << jsbachParser.T__13) | (1 << jsbachParser.VAR) | (1 << jsbachParser.FNME))) != 0):
                self.state = 38
                self.line()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsbachParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReprContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepr" ):
                return visitor.visitRepr(self)
            else:
                return visitor.visitChildren(self)


    class RetContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)


    class CallContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FNME(self):
            return self.getToken(jsbachParser.FNME, 0)
        def param(self):
            return self.getTypedRuleContext(jsbachParser.ParamContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class ListreprContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(jsbachParser.ListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListrepr" ):
                return visitor.visitListrepr(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class WrtContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.PrintableContext)
            else:
                return self.getTypedRuleContext(jsbachParser.PrintableContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrt" ):
                return visitor.visitWrt(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(jsbachParser.CondContext,0)

        def codeblock(self):
            return self.getTypedRuleContext(jsbachParser.CodeblockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(jsbachParser.CondContext,0)

        def codeblock(self):
            return self.getTypedRuleContext(jsbachParser.CodeblockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class DeleteContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete" ):
                return visitor.visitDelete(self)
            else:
                return visitor.visitChildren(self)


    class AppendContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppend" ):
                return visitor.visitAppend(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)
        def assignable(self):
            return self.getTypedRuleContext(jsbachParser.AssignableContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(jsbachParser.CondContext,0)

        def codeblock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.CodeblockContext)
            else:
                return self.getTypedRuleContext(jsbachParser.CodeblockContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = jsbachParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_line)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = jsbachParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(jsbachParser.VAR)
                self.state = 45
                self.match(jsbachParser.T__2)
                self.state = 46
                self.assignable()
                pass

            elif la_ == 2:
                localctx = jsbachParser.WrtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(jsbachParser.T__3)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 48
                        self.printable()

                    else:
                        raise NoViableAltException(self)
                    self.state = 51 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 3:
                localctx = jsbachParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(jsbachParser.T__4)
                self.state = 54
                self.match(jsbachParser.VAR)
                pass

            elif la_ == 4:
                localctx = jsbachParser.ReprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(jsbachParser.T__5)
                self.state = 56
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = jsbachParser.ListreprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(jsbachParser.T__5)
                self.state = 58
                self.list_()
                pass

            elif la_ == 6:
                localctx = jsbachParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.match(jsbachParser.T__6)
                self.state = 60
                self.cond()
                self.state = 61
                self.match(jsbachParser.T__0)
                self.state = 62
                self.codeblock()
                self.state = 63
                self.match(jsbachParser.T__1)
                self.state = 64
                self.match(jsbachParser.T__7)
                self.state = 65
                self.match(jsbachParser.T__0)
                self.state = 66
                self.codeblock()
                self.state = 67
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 7:
                localctx = jsbachParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.match(jsbachParser.T__6)
                self.state = 70
                self.cond()
                self.state = 71
                self.match(jsbachParser.T__0)
                self.state = 72
                self.codeblock()
                self.state = 73
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 8:
                localctx = jsbachParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.match(jsbachParser.T__8)
                self.state = 76
                self.cond()
                self.state = 77
                self.match(jsbachParser.T__0)
                self.state = 78
                self.codeblock()
                self.state = 79
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 9:
                localctx = jsbachParser.AppendContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.match(jsbachParser.VAR)
                self.state = 82
                self.match(jsbachParser.T__9)
                self.state = 83
                self.expr(0)
                pass

            elif la_ == 10:
                localctx = jsbachParser.DeleteContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 84
                self.match(jsbachParser.T__10)
                self.state = 85
                self.match(jsbachParser.VAR)
                self.state = 86
                self.match(jsbachParser.T__11)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(jsbachParser.T__12)
                pass

            elif la_ == 11:
                localctx = jsbachParser.RetContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 90
                self.match(jsbachParser.T__13)
                self.state = 91
                self.expr(0)
                pass

            elif la_ == 12:
                localctx = jsbachParser.CallContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 92
                self.match(jsbachParser.FNME)
                self.state = 93
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsbachParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def ADD(self):
            return self.getToken(jsbachParser.ADD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class NoteContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTE(self):
            return self.getToken(jsbachParser.NOTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNote" ):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def SUBS(self):
            return self.getToken(jsbachParser.SUBS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def MULT(self):
            return self.getToken(jsbachParser.MULT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(jsbachParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class ListaccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaccess" ):
                return visitor.visitListaccess(self)
            else:
                return visitor.visitChildren(self)


    class UnarysubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUBS(self):
            return self.getToken(jsbachParser.SUBS, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnarysub" ):
                return visitor.visitUnarysub(self)
            else:
                return visitor.visitChildren(self)


    class CallInExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FNME(self):
            return self.getToken(jsbachParser.FNME, 0)
        def param(self):
            return self.getTypedRuleContext(jsbachParser.ParamContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallInExpr" ):
                return visitor.visitCallInExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def DIV(self):
            return self.getToken(jsbachParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class ListlengthContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListlength" ):
                return visitor.visitListlength(self)
            else:
                return visitor.visitChildren(self)


    class RemContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def REM(self):
            return self.getToken(jsbachParser.REM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRem" ):
                return visitor.visitRem(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = jsbachParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = jsbachParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 97
                self.match(jsbachParser.T__14)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(jsbachParser.T__15)
                pass

            elif la_ == 2:
                localctx = jsbachParser.ListlengthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(jsbachParser.T__16)
                self.state = 102
                self.match(jsbachParser.VAR)
                pass

            elif la_ == 3:
                localctx = jsbachParser.ListaccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(jsbachParser.VAR)
                self.state = 104
                self.match(jsbachParser.T__11)
                self.state = 105
                self.expr(0)
                self.state = 106
                self.match(jsbachParser.T__12)
                pass

            elif la_ == 4:
                localctx = jsbachParser.UnarysubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(jsbachParser.SUBS)
                self.state = 109
                self.expr(5)
                pass

            elif la_ == 5:
                localctx = jsbachParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(jsbachParser.NUM)
                pass

            elif la_ == 6:
                localctx = jsbachParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(jsbachParser.VAR)
                pass

            elif la_ == 7:
                localctx = jsbachParser.NoteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(jsbachParser.NOTE)
                pass

            elif la_ == 8:
                localctx = jsbachParser.CallInExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(jsbachParser.FNME)
                self.state = 114
                self.param()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 132
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.DivContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 117
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 118
                        self.match(jsbachParser.DIV)
                        self.state = 119
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.MultContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 120
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 121
                        self.match(jsbachParser.MULT)
                        self.state = 122
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.RemContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 124
                        self.match(jsbachParser.REM)
                        self.state = 125
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = jsbachParser.AddContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 127
                        self.match(jsbachParser.ADD)
                        self.state = 128
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = jsbachParser.SubContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 130
                        self.match(jsbachParser.SUBS)
                        self.state = 131
                        self.expr(7)
                        pass

             
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FheaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.VAR)
            else:
                return self.getToken(jsbachParser.VAR, i)

        def getRuleIndex(self):
            return jsbachParser.RULE_fheader

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFheader" ):
                return visitor.visitFheader(self)
            else:
                return visitor.visitChildren(self)




    def fheader(self):

        localctx = jsbachParser.FheaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fheader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VAR:
                self.state = 137
                self.match(jsbachParser.VAR)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = jsbachParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.expr(0) 
                self.state = 148
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def COMP(self):
            return self.getToken(jsbachParser.COMP, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = jsbachParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.expr(0)
            self.state = 150
            self.match(jsbachParser.COMP)
            self.state = 151
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def list_(self):
            return self.getTypedRuleContext(jsbachParser.ListContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_assignable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignable" ):
                return visitor.visitAssignable(self)
            else:
                return visitor.visitChildren(self)




    def assignable(self):

        localctx = jsbachParser.AssignableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignable)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__14, jsbachParser.T__16, jsbachParser.NOTE, jsbachParser.VAR, jsbachParser.FNME, jsbachParser.NUM, jsbachParser.SUBS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.expr(0)
                pass
            elif token in [jsbachParser.T__17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.list_()
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


    class PrintableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def list_(self):
            return self.getTypedRuleContext(jsbachParser.ListContext,0)


        def STR(self):
            return self.getToken(jsbachParser.STR, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_printable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintable" ):
                return visitor.visitPrintable(self)
            else:
                return visitor.visitChildren(self)




    def printable(self):

        localctx = jsbachParser.PrintableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_printable)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__14, jsbachParser.T__16, jsbachParser.NOTE, jsbachParser.VAR, jsbachParser.FNME, jsbachParser.NUM, jsbachParser.SUBS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.expr(0)
                pass
            elif token in [jsbachParser.T__17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.list_()
                pass
            elif token in [jsbachParser.STR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(jsbachParser.STR)
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = jsbachParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(jsbachParser.T__17)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__14) | (1 << jsbachParser.T__16) | (1 << jsbachParser.NOTE) | (1 << jsbachParser.VAR) | (1 << jsbachParser.FNME) | (1 << jsbachParser.NUM) | (1 << jsbachParser.SUBS))) != 0):
                self.state = 163
                self.expr(0)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(jsbachParser.T__18)
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
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




