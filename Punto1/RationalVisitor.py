# Generated from Rational.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RationalParser import RationalParser
else:
    from RationalParser import RationalParser

# This class defines a complete generic visitor for a parse tree produced by RationalParser.

class RationalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RationalParser#prog.
    def visitProg(self, ctx:RationalParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#AddSub.
    def visitAddSub(self, ctx:RationalParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#ToTerm.
    def visitToTerm(self, ctx:RationalParser.ToTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#ToFactor.
    def visitToFactor(self, ctx:RationalParser.ToFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#MulDiv.
    def visitMulDiv(self, ctx:RationalParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#Fraction.
    def visitFraction(self, ctx:RationalParser.FractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalParser#Parens.
    def visitParens(self, ctx:RationalParser.ParensContext):
        return self.visitChildren(ctx)



del RationalParser