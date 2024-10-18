# Generated from Rational.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RationalParser import RationalParser
else:
    from RationalParser import RationalParser

# This class defines a complete listener for a parse tree produced by RationalParser.
class RationalListener(ParseTreeListener):

    # Enter a parse tree produced by RationalParser#prog.
    def enterProg(self, ctx:RationalParser.ProgContext):
        pass

    # Exit a parse tree produced by RationalParser#prog.
    def exitProg(self, ctx:RationalParser.ProgContext):
        pass


    # Enter a parse tree produced by RationalParser#AddSub.
    def enterAddSub(self, ctx:RationalParser.AddSubContext):
        pass

    # Exit a parse tree produced by RationalParser#AddSub.
    def exitAddSub(self, ctx:RationalParser.AddSubContext):
        pass


    # Enter a parse tree produced by RationalParser#ToTerm.
    def enterToTerm(self, ctx:RationalParser.ToTermContext):
        pass

    # Exit a parse tree produced by RationalParser#ToTerm.
    def exitToTerm(self, ctx:RationalParser.ToTermContext):
        pass


    # Enter a parse tree produced by RationalParser#ToFactor.
    def enterToFactor(self, ctx:RationalParser.ToFactorContext):
        pass

    # Exit a parse tree produced by RationalParser#ToFactor.
    def exitToFactor(self, ctx:RationalParser.ToFactorContext):
        pass


    # Enter a parse tree produced by RationalParser#MulDiv.
    def enterMulDiv(self, ctx:RationalParser.MulDivContext):
        pass

    # Exit a parse tree produced by RationalParser#MulDiv.
    def exitMulDiv(self, ctx:RationalParser.MulDivContext):
        pass


    # Enter a parse tree produced by RationalParser#Fraction.
    def enterFraction(self, ctx:RationalParser.FractionContext):
        pass

    # Exit a parse tree produced by RationalParser#Fraction.
    def exitFraction(self, ctx:RationalParser.FractionContext):
        pass


    # Enter a parse tree produced by RationalParser#Parens.
    def enterParens(self, ctx:RationalParser.ParensContext):
        pass

    # Exit a parse tree produced by RationalParser#Parens.
    def exitParens(self, ctx:RationalParser.ParensContext):
        pass



del RationalParser