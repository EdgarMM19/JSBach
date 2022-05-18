# Generated from jsbach.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#functions.
    def visitFunctions(self, ctx:jsbachParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#func.
    def visitFunc(self, ctx:jsbachParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#codeblock.
    def visitCodeblock(self, ctx:jsbachParser.CodeblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx:jsbachParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#wrt.
    def visitWrt(self, ctx:jsbachParser.WrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx:jsbachParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#repr.
    def visitRepr(self, ctx:jsbachParser.ReprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listrepr.
    def visitListrepr(self, ctx:jsbachParser.ListreprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ifelse.
    def visitIfelse(self, ctx:jsbachParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx:jsbachParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx:jsbachParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#append.
    def visitAppend(self, ctx:jsbachParser.AppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#delete.
    def visitDelete(self, ctx:jsbachParser.DeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#call.
    def visitCall(self, ctx:jsbachParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#par.
    def visitPar(self, ctx:jsbachParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#div.
    def visitDiv(self, ctx:jsbachParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#add.
    def visitAdd(self, ctx:jsbachParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listlength.
    def visitListlength(self, ctx:jsbachParser.ListlengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#note.
    def visitNote(self, ctx:jsbachParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#sub.
    def visitSub(self, ctx:jsbachParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#mult.
    def visitMult(self, ctx:jsbachParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#var.
    def visitVar(self, ctx:jsbachParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#num.
    def visitNum(self, ctx:jsbachParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#rem.
    def visitRem(self, ctx:jsbachParser.RemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#listaccess.
    def visitListaccess(self, ctx:jsbachParser.ListaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#fheader.
    def visitFheader(self, ctx:jsbachParser.FheaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#param.
    def visitParam(self, ctx:jsbachParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#cond.
    def visitCond(self, ctx:jsbachParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assignable.
    def visitAssignable(self, ctx:jsbachParser.AssignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#printable.
    def visitPrintable(self, ctx:jsbachParser.PrintableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#list.
    def visitList(self, ctx:jsbachParser.ListContext):
        return self.visitChildren(ctx)



del jsbachParser