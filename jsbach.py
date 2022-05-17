if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
    from .jsbachLexer import jsbachLexer
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
    from jsbachLexer import jsbachLexer

from antlr4 import *

class TreeVisitor(jsbachVisitor):
    def __init__(self):
        self.simbols = []
        self.functions = {}

    # variables work
    def getValueOfSimbol(self, name):
        if name in self.simbols[-1]:
            return self.simbols[-1][name]
        else:
            self.simbols[-1][name] = 0
            return self.simbols[-1][name]

    def setValueOfSimbol(self, name, val):
        self.simbols[-1][name] = val
        return self.simbols[-1][name]
    # end variables

    ##
    ## arithmetic expressions visitors
    ##

    # Visit a parse tree produced by jsbachParser#par.
    def visitPar(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])


    # Visit a parse tree produced by jsbachParser#div.
    def visitDiv(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1]) // self.visit(l[1])

    # Visit a parse tree produced by jsbachParser#add.
    def visitAdd(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])+self.visit(l[2])

    # Visit a parse tree produced by jsbachParser#sub.
    def visitSub(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1]) - self.visit(l[1])


    # Visit a parse tree produced by jsbachParser#mult.
    def visitMult(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1]) * self.visit(l[1])


    # Visit a parse tree produced by jsbachParser#var.
    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        return self.getValueOfSimbol(l[0].getText())


    # Visit a parse tree produced by jsbachParser#num.
    def visitNum(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())


    # Visit a parse tree produced by jsbachParser#rem.
    def visitRem(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1]) % self.visit(l[1])
    ##
    ## end arithmetic expressions visitors
    ##

    ##
    ## Visit line instructions
    ##

    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        val = self.visit(l[2])
        self.setValueOfSimbol(nom, val)


    # Visit a parse tree produced by jsbachParser#wrt.
    def visitWrt(self, ctx):
        l = list(ctx.getChildren())
        print(str(self.visit(l[1])))


    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx):
        l = list(ctx.getChildren())
        nom = l[1].getText()
        self.setValueOfSimbol(nom, int(input()))


    # Visit a parse tree produced by jsbachParser#repr.
    def visitRepr(self, ctx):
        # TODO
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ifelse.
    def visitIfelse(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3]) #TODO: this is for returns in functions, have to see
        else:
            return self.visit(l[7])


    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3]) #TODO: this is for returns in functions, have to see


    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            ret = self.visit(l[3])
            if ret != None: #TODO: this is for returns in functions, have to see
                return ret

    # Visit a parse tree produced by jsbachParser#call.
    def visitCall(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        param = self.visit(l[1])
        (codi, paramsNames) = self.functions[nom]

        self.simbols.append({})
        for (x,y) in zip(paramsNames, param):
            self.setValueOfSimbol(x,y) # todo: Arrays are passed by reference
        sol = self.visit(codi)
        self.simbols.pop()
        return sol

    ##
    ## End visit line instructions
    ##

    def visitCond(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '=':
            return self.visit(l[0]) == self.visit(l[2])
        elif l[1].getText() == '<':
            return self.visit(l[0]) < self.visit(l[2])
        elif l[1].getText() == '>':
            return self.visit(l[0]) > self.visit(l[2])
        elif l[1].getText() == '/=':
            return self.visit(l[0]) != self.visit(l[2])
        elif l[1].getText() == '>=':
            return self.visit(l[0]) >= self.visit(l[2])
        elif l[1].getText() == '<=':
            return self.visit(l[0]) <= self.visit(l[2])

    ##
    ## Function, header and parameters visitors
    ##
    def visitFunc(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()
        codi = l[3]
        params = self.visit(l[1])
        self.functions[nom] = (codi, params)

    def visitFheader(self, ctx):
        l = list(ctx.getChildren())
        param = []
        for x in l:
            param.append(x.getText())
        return param
    def visitParam(self, ctx):
        l = list(ctx.getChildren())
        param = []
        for x in l:
            param.append(self.visit(x))
        return param
    ##
    ## End function, header and parameters visitors
    ##

    # Only needed for returns:
    # def visitCodeblock(self, ctx): 
    #    l = list(ctx.getChildren())
    #    for lin in l:
    #        ret = self.visit(lin)
    #        if ret != None:
    #            return ret

    def run(self, funName):
        # TODO: run from not main with values
        self.simbols.append({})
        print(self.functions)
        (codi, paramsNames) = self.functions[funName]
        self.visit(codi)


def main():
    input_stream = StdinStream()

    lexer = jsbachLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = jsbachParser(token_stream)

    tree = parser.root()
    visitor = TreeVisitor()
    visitor.visit(tree)

    visitor.run("Main")

#visitor = TreeVisitor()
#visitor.visit(tree)

if __name__ == "__main__":
    main()
       


