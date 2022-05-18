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
        4,1,25,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,4,1,25,8,1,11,1,12,1,26,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,4,3,36,8,3,11,3,12,3,37,1,4,1,4,1,4,
        1,4,1,4,4,4,45,8,4,11,4,12,4,46,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,87,
        8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,104,8,5,10,5,12,5,107,9,5,1,6,5,6,110,8,6,10,6,12,6,113,9,6,
        1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,8,1,8,1,8,1,8,1,9,1,9,3,9,127,
        8,9,1,9,0,1,10,10,0,2,4,6,8,10,12,14,16,18,0,0,139,0,20,1,0,0,0,
        2,24,1,0,0,0,4,28,1,0,0,0,6,35,1,0,0,0,8,76,1,0,0,0,10,86,1,0,0,
        0,12,111,1,0,0,0,14,117,1,0,0,0,16,120,1,0,0,0,18,126,1,0,0,0,20,
        21,3,2,1,0,21,22,5,0,0,1,22,1,1,0,0,0,23,25,3,4,2,0,24,23,1,0,0,
        0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,29,5,
        16,0,0,29,30,3,12,6,0,30,31,5,1,0,0,31,32,3,6,3,0,32,33,5,2,0,0,
        33,5,1,0,0,0,34,36,3,8,4,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,
        0,0,37,38,1,0,0,0,38,7,1,0,0,0,39,40,5,15,0,0,40,41,5,3,0,0,41,77,
        3,10,5,0,42,44,5,4,0,0,43,45,3,18,9,0,44,43,1,0,0,0,45,46,1,0,0,
        0,46,44,1,0,0,0,46,47,1,0,0,0,47,77,1,0,0,0,48,49,5,5,0,0,49,77,
        5,15,0,0,50,51,5,6,0,0,51,77,3,10,5,0,52,53,5,7,0,0,53,54,3,16,8,
        0,54,55,5,1,0,0,55,56,3,6,3,0,56,57,5,2,0,0,57,58,5,8,0,0,58,59,
        5,1,0,0,59,60,3,6,3,0,60,61,5,2,0,0,61,77,1,0,0,0,62,63,5,7,0,0,
        63,64,3,16,8,0,64,65,5,1,0,0,65,66,3,6,3,0,66,67,5,2,0,0,67,77,1,
        0,0,0,68,69,5,9,0,0,69,70,3,16,8,0,70,71,5,1,0,0,71,72,3,6,3,0,72,
        73,5,2,0,0,73,77,1,0,0,0,74,75,5,16,0,0,75,77,3,14,7,0,76,39,1,0,
        0,0,76,42,1,0,0,0,76,48,1,0,0,0,76,50,1,0,0,0,76,52,1,0,0,0,76,62,
        1,0,0,0,76,68,1,0,0,0,76,74,1,0,0,0,77,9,1,0,0,0,78,79,6,5,-1,0,
        79,80,5,10,0,0,80,81,3,10,5,0,81,82,5,11,0,0,82,87,1,0,0,0,83,87,
        5,17,0,0,84,87,5,15,0,0,85,87,5,13,0,0,86,78,1,0,0,0,86,83,1,0,0,
        0,86,84,1,0,0,0,86,85,1,0,0,0,87,105,1,0,0,0,88,89,10,8,0,0,89,90,
        5,20,0,0,90,104,3,10,5,9,91,92,10,7,0,0,92,93,5,19,0,0,93,104,3,
        10,5,8,94,95,10,6,0,0,95,96,5,22,0,0,96,104,3,10,5,7,97,98,10,5,
        0,0,98,99,5,18,0,0,99,104,3,10,5,6,100,101,10,4,0,0,101,102,5,21,
        0,0,102,104,3,10,5,5,103,88,1,0,0,0,103,91,1,0,0,0,103,94,1,0,0,
        0,103,97,1,0,0,0,103,100,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,
        105,106,1,0,0,0,106,11,1,0,0,0,107,105,1,0,0,0,108,110,5,15,0,0,
        109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,
        112,13,1,0,0,0,113,111,1,0,0,0,114,116,3,10,5,0,115,114,1,0,0,0,
        116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,15,1,0,0,0,119,
        117,1,0,0,0,120,121,3,10,5,0,121,122,5,23,0,0,122,123,3,10,5,0,123,
        17,1,0,0,0,124,127,3,10,5,0,125,127,5,12,0,0,126,124,1,0,0,0,126,
        125,1,0,0,0,127,19,1,0,0,0,10,26,37,46,76,86,103,105,111,117,126
    ]

class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'<-'", "'<!>'", "'<?>'", 
                     "'<:>'", "'if'", "'else'", "'while'", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'*'", "'/'", "'-'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_printable = 9

    ruleNames =  [ "root", "functions", "func", "codeblock", "line", "expr", 
                   "fheader", "param", "cond", "printable" ]

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
    STR=12
    NOTE=13
    LN=14
    VAR=15
    FNME=16
    NUM=17
    ADD=18
    MULT=19
    DIV=20
    SUBS=21
    REM=22
    COMP=23
    WS=24
    COMMENT=25

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
            self.state = 20
            self.functions()
            self.state = 21
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
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.func()
                self.state = 26 
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
            self.state = 28
            self.match(jsbachParser.FNME)
            self.state = 29
            self.fheader()
            self.state = 30
            self.match(jsbachParser.T__0)
            self.state = 31
            self.codeblock()
            self.state = 32
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
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.line()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.T__3) | (1 << jsbachParser.T__4) | (1 << jsbachParser.T__5) | (1 << jsbachParser.T__6) | (1 << jsbachParser.T__8) | (1 << jsbachParser.VAR) | (1 << jsbachParser.FNME))) != 0)):
                    break

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


    class AssignContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


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
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = jsbachParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(jsbachParser.VAR)
                self.state = 40
                self.match(jsbachParser.T__2)
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = jsbachParser.WrtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(jsbachParser.T__3)
                self.state = 44 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 43
                        self.printable()

                    else:
                        raise NoViableAltException(self)
                    self.state = 46 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 3:
                localctx = jsbachParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(jsbachParser.T__4)
                self.state = 49
                self.match(jsbachParser.VAR)
                pass

            elif la_ == 4:
                localctx = jsbachParser.ReprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(jsbachParser.T__5)
                self.state = 51
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = jsbachParser.IfelseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(jsbachParser.T__6)
                self.state = 53
                self.cond()
                self.state = 54
                self.match(jsbachParser.T__0)
                self.state = 55
                self.codeblock()
                self.state = 56
                self.match(jsbachParser.T__1)
                self.state = 57
                self.match(jsbachParser.T__7)
                self.state = 58
                self.match(jsbachParser.T__0)
                self.state = 59
                self.codeblock()
                self.state = 60
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 6:
                localctx = jsbachParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 62
                self.match(jsbachParser.T__6)
                self.state = 63
                self.cond()
                self.state = 64
                self.match(jsbachParser.T__0)
                self.state = 65
                self.codeblock()
                self.state = 66
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 7:
                localctx = jsbachParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.match(jsbachParser.T__8)
                self.state = 69
                self.cond()
                self.state = 70
                self.match(jsbachParser.T__0)
                self.state = 71
                self.codeblock()
                self.state = 72
                self.match(jsbachParser.T__1)
                pass

            elif la_ == 8:
                localctx = jsbachParser.CallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 74
                self.match(jsbachParser.FNME)
                self.state = 75
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
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__9]:
                localctx = jsbachParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 79
                self.match(jsbachParser.T__9)
                self.state = 80
                self.expr(0)
                self.state = 81
                self.match(jsbachParser.T__10)
                pass
            elif token in [jsbachParser.NUM]:
                localctx = jsbachParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 83
                self.match(jsbachParser.NUM)
                pass
            elif token in [jsbachParser.VAR]:
                localctx = jsbachParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(jsbachParser.VAR)
                pass
            elif token in [jsbachParser.NOTE]:
                localctx = jsbachParser.NoteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(jsbachParser.NOTE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.DivContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 89
                        self.match(jsbachParser.DIV)
                        self.state = 90
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.MultContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 92
                        self.match(jsbachParser.MULT)
                        self.state = 93
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.RemContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 95
                        self.match(jsbachParser.REM)
                        self.state = 96
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = jsbachParser.AddContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 98
                        self.match(jsbachParser.ADD)
                        self.state = 99
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = jsbachParser.SubContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 101
                        self.match(jsbachParser.SUBS)
                        self.state = 102
                        self.expr(5)
                        pass

             
                self.state = 107
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
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.VAR:
                self.state = 108
                self.match(jsbachParser.VAR)
                self.state = 113
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
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 114
                    self.expr(0) 
                self.state = 119
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
            self.state = 120
            self.expr(0)
            self.state = 121
            self.match(jsbachParser.COMP)
            self.state = 122
            self.expr(0)
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
        self.enterRule(localctx, 18, self.RULE_printable)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.T__9, jsbachParser.NOTE, jsbachParser.VAR, jsbachParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.expr(0)
                pass
            elif token in [jsbachParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




