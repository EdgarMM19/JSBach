if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
    from .jsbachLexer import jsbachLexer
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
    from jsbachLexer import jsbachLexer

from antlr4 import *
import sys
import os
from subprocess import DEVNULL, STDOUT, check_call


class TreeVisitor(jsbachVisitor):
    def __init__(self):
        self.simbols = []
        self.functions = {}
        self.notes = []

    # Variables management
    def getValueOfSimbol(self, name):
        if name in self.simbols[-1]:
            return self.simbols[-1][name]
        else:
            self.simbols[-1][name] = 0
            return self.simbols[-1][name]

    def setValueOfSimbol(self, name, val):
        # correct and assign and pass by reference in list handling
        # can not break the pointers
        if isinstance(val, list) and (name in self.simbols[-1]):
            while len(self.simbols[-1][name]) != 0:
                self.simbols[-1][name].pop()
            for x in val:
                self.simbols[-1][name].append(x)
        else:
            self.simbols[-1][name] = val
        return self.simbols[-1][name]

    def noteToInt(self, note):
        if len(note) == 1:
            note = note + "4"
        val = ord(note[0])-ord('A')
        if val > 1:
            val -= 7
        val += 7*(ord(note[1])-ord('0'))
        return val
    # End variables management

    # Used in visitCall and visitCallInExpr and run for good handling of return statements

    def genericFunctionCall(self, funName, params):
        self.simbols.append({})
        if not funName in self.functions:
            raise Exception("Function " + funName + " doesn't exists.")
        (codi, paramsNames) = self.functions[funName]
        if len(paramsNames) != len(params):
            raise Exception("Function " + funName + " has " + str(len(paramsNames)) +
                            " parameters but " + str(len(params)) + " were provided.")
        for (x, y) in zip(paramsNames, params):
            self.setValueOfSimbol(x, y)
        sol = self.visit(codi)
        self.simbols.pop()
        return sol

    ##
    # arithmetic expressions visitors
    ##

    # Visit a parse tree produced by jsbachParser#par.
    def visitPar(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    # Visit a parse tree produced by jsbachParser#div.

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())
        a = self.visit(l[0])
        b = self.visit(l[2])
        if b == 0:
            raise Exception("Division by zero")
        return a // b

    # Visit a parse tree produced by jsbachParser#add.
    def visitAdd(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])+self.visit(l[2])

    # Visit a parse tree produced by jsbachParser#sub.
    def visitSub(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])

    # Visit a parse tree produced by jsbachParser#unarysub.
    def visitUnarysub(self, ctx):
        l = list(ctx.getChildren())
        return - self.visit(l[1])

    # Visit a parse tree produced by jsbachParser#mult.
    def visitMult(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) * self.visit(l[2])

    # Visit a parse tree produced by jsbachParser#rem.
    def visitRem(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) % self.visit(l[2])

    # Visit a parse tree produced by jsbachParser#var.
    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        return self.getValueOfSimbol(l[0].getText())

    def visitListlength(self, ctx):
        l = list(ctx.getChildren())
        a = self.getValueOfSimbol(l[1].getText())
        if not isinstance(a, list):
            raise Exception(
                "Can not get length of a non-list object " + l[0].getText())
        return len(a)

    # Visit a parse tree produced by jsbachParser#listaccess.
    def visitListaccess(self, ctx: jsbachParser.ListaccessContext):
        l = list(ctx.getChildren())
        a = self.getValueOfSimbol(l[0].getText())
        index = self.visit(l[2])-1
        if not isinstance(a, list):
            raise Exception(
                "Can not access a non-list object " + l[0].getText())
        if index < 0 or index >= len(a):
            raise Exception("Trying to acces element not in array bounds.")
        return a[index]

    # Visit a parse tree produced by jsbachParser#num.
    def visitNum(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    # Visit a parse tree produced by jsbachParser#note.
    def visitNote(self, ctx):
        l = list(ctx.getChildren())
        return self.noteToInt(l[0].getText())

    def visitCallInExpr(self, ctx):
        l = list(ctx.getChildren())
        funName = l[0].getText()
        params = self.visit(l[1])
        return self.genericFunctionCall(funName, params)

    ##
    # end arithmetic expressions visitors
    ##

    ##
    # Visit line instructions
    ##

    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx):
        l = list(ctx.getChildren())
        name = l[0].getText()
        val = self.visit(l[2])
        # list assignation is by copy
        if isinstance(val, list):
            val = list(val)
        self.setValueOfSimbol(name, val)

    # Visit a parse tree produced by jsbachParser#assignVectorPos.
    def visitAssignVectorPos(self, ctx):
        l = list(ctx.getChildren())
        name = l[0].getText()
        index = self.visit(l[2])-1
        val = self.visit(l[5])
        if isinstance(val, list):
            raise Exception("Lists can not be members of lists.")
        v = self.getValueOfSimbol(name)
        if not isinstance(v, list):
            raise Exception("Can not acces a position of non-list object.")
        if index < 0 or index >= len(v):
            raise Exception("Trying to set an element not in array bounds.")
        v[index] = val

    # Visit a parse tree produced by jsbachParser#wrt.
    def visitWrt(self, ctx):
        l = list(ctx.getChildren())
        out = ""
        for pr in l[1:]:
            partial = self.visit(pr)
            # the only parameters of write are text, lists and integers
            if partial == None:
                partial = pr.getText().replace("\"", "")
            elif isinstance(partial, list):
                partial = [str(x) for x in partial]
                partial = "{" + " ".join(partial) + "}"
            else:
                partial = str(partial)
            if len(out) != 0:
                out = out + " "
            out = out + partial
        print(out)

    # Visit a parse tree produced by jsbachParser#read.

    def visitRead(self, ctx):
        l = list(ctx.getChildren())
        nom = l[1].getText()
        self.setValueOfSimbol(nom, int(input()))

    # Visit a parse tree produced by jsbachParser#repr.

    def visitRepr(self, ctx):
        l = list(ctx.getChildren())
        note = self.visit(l[1])
        self.notes.append(note)

    # Visit a parse tree produced by jsbachParser#listrepr.
    def visitListrepr(self, ctx):
        l = list(ctx.getChildren())
        a = self.visit(l[1])
        for note in a:
            self.notes.append(note)

    # Visit a parse tree produced by jsbachParser#ifelse.
    def visitIfelse(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3])
        else:
            return self.visit(l[7])

    # Visit a parse tree produced by jsbachParser#if.
    def visitIf(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            return self.visit(l[3])

    # Visit a parse tree produced by jsbachParser#while.
    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            ret = self.visit(l[3])
            if ret != None:
                return ret

    def visitAppend(self, ctx):
        l = list(ctx.getChildren())
        a = self.getValueOfSimbol(l[0].getText())
        if not isinstance(a, list):
            raise Exception(
                "Can not get append to a non-list object " + l[0].getText())
        a.append(self.visit(l[2]))

    # Visit a parse tree produced by jsbachParser#delete.
    def visitDelete(self, ctx):
        l = list(ctx.getChildren())
        a = self.getValueOfSimbol(l[1].getText())
        if not isinstance(a, list):
            raise Exception(
                "Can not get delete an element of a non-list object " + l[0].getText())
        index = self.visit(l[3])-1
        if index < 0 or index >= len(a):
            raise Exception("Trying to delete element not in array bounds.")
        a.pop(index)

    # Visit a parse tree produced by jsbachParser#call.
    def visitCall(self, ctx):
        l = list(ctx.getChildren())
        funName = l[0].getText()
        params = self.visit(l[1])
        self.genericFunctionCall(funName, params)

    # Visit a parse tree produced by jsbachParser#ret.
    def visitRet(self, ctx: jsbachParser.RetContext):
        l = list(ctx.getChildren())
        return self.visit(l[1])

    ##
    # End visit line instructions
    ##

    # Visit a parse tree produced by jsbachParser#list.
    def visitList(self, ctx):
        a = []
        l = list(ctx.getChildren())
        for elem in l[1:-1]:
            el = self.visit(elem)
            if isinstance(el, list):
                raise Exception("Lists can not be members of lists.")
            a.append(el)
        return a

    def visitComparate(self, ctx: jsbachParser.ComparateContext):
        l = list(ctx.getChildren())
        if l[1].getText() == '=':
            return int(self.visit(l[0]) == self.visit(l[2]))
        elif l[1].getText() == '<':
            return int(self.visit(l[0]) < self.visit(l[2]))
        elif l[1].getText() == '>':
            return int(self.visit(l[0]) > self.visit(l[2]))
        elif l[1].getText() == '/=':
            return int(self.visit(l[0]) != self.visit(l[2]))
        elif l[1].getText() == '>=':
            return int(self.visit(l[0]) >= self.visit(l[2]))
        elif l[1].getText() == '<=':
            return int(self.visit(l[0]) <= self.visit(l[2]))

    ##
    # Function, header and parameters visitors
    ##
    def visitFunc(self, ctx):
        l = list(ctx.getChildren())
        name = l[0].getText()
        code = l[3]
        params = self.visit(l[1])
        if name in self.functions:
            raise Exception("Function " + name + " is declared twice.")
        self.functions[name] = (code, params)

    def visitFheader(self, ctx):
        l = list(ctx.getChildren())
        param = []
        for x in l:
            if x.getText() in param:
                raise Exception("Parameter " + x.getText() +
                                " appears twice in function definition.")
            param.append(x.getText())
        return param

    def visitParam(self, ctx):
        l = list(ctx.getChildren())
        param = []
        for x in l:
            param.append(self.visit(x))
        return param
    ##
    # End function, header and parameters visitors
    ##

    def visitCodeblock(self, ctx):
        l = list(ctx.getChildren())
        for lin in l:
            ret = self.visit(lin)
            if ret != None:
                return ret

    def run(self, funName, params):
        self.genericFunctionCall(funName, params)

    def getNotes(self):
        return self.notes


def intToNote(id):
    letter = chr(ord("a") + id % 7)

    number = (id + 5) // 7
    scale = ""
    if number > 3:
        scale = "'"*(number-3)
    elif number < 3:
        scale = ","*(3-number)
    return letter + scale + "4"


def generateLily(fileName, notes):
    f = open(fileName + ".lily", "w")
    f.write("\\version \"2.22.1\"\n")
    f.write("\\score {\n")
    f.write("\\absolute {\n")
    f.write("\\tempo 4 = 120\n")

    notes2 = [intToNote(note) for note in notes]
    outNotes = ' '.join(notes2)
    f.write(outNotes)

    f.write("}\n")
    f.write("\\layout { }\n")
    f.write("\\midi { }\n")
    f.write("}\n")
    f.close()


def generateMusic(notes, name, reproduce):
    # if no notes generated don't try to play music
    if len(notes) > 0:
        generateLily(name, notes)

        check_call(['lilypond', name + ".lily"],
                   stdout=DEVNULL, stderr=STDOUT)
        check_call(['timidity', '-Ow', '-o', name + ".wav",
                   name + ".midi"], stdout=DEVNULL, stderr=STDOUT)

        if os.path.exists(name + ".mp3"):
            os.remove(name + ".mp3")
        os.system(' '.join(['ffmpeg', '-i', name + ".wav", '-codec:a',
                  'libmp3lame', '-qscale:a', '2', name + ".mp3", "2>/dev/null"]))
        if reproduce:
            check_call(['afplay', name + ".mp3"],
                       stdout=DEVNULL, stderr=STDOUT)


def main():
    if len(sys.argv) == 1:
        print("Use:\npython3 jsbach.py programname.jsb [StartFunction] [Parameters of Start function] [-NP]\
            \nIf the start functions has only integers input you can specify them next to the function name. If it has list arguments then you shouldn't start there:)\
            \nUse -NP option if you dont want to reproduce the output at the end")
        return

    reproduce = True
    for arg in sys.argv:
        if arg == "-NP":
            reproduce = False
    programName = sys.argv[1].replace(".jsb", "")
    input_stream = FileStream(programName + ".jsb", encoding='utf-8')

    beginAt = "Main"
    args = []
    if len(sys.argv) > 2:
        if sys.argv[2] != "-NP":
            beginAt = sys.argv[2]
            for arg in sys.argv[3:]:
                if arg != "-NP":
                    args.append(int(arg))

    lexer = jsbachLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = jsbachParser(token_stream)

    tree = parser.root()
    visitor = TreeVisitor()
    try:
        visitor.visit(tree)
    except Exception as err:
        # errors while parsing the program
        print("Bad program format: {0}".format(err))
        return

    try:
        visitor.run(beginAt, args)
    except Exception as err:
        print("Execution error: {0}".format(err))
        return

    notes = visitor.getNotes()
    generateMusic(notes, programName, reproduce)


if __name__ == "__main__":
    main()
