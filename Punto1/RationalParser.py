# Generated from Rational.g4 by ANTLR 4.13.2
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
        4,1,9,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,0,
        2,2,4,4,0,2,4,6,0,2,1,0,1,2,1,0,3,4,39,0,8,1,0,0,0,2,11,1,0,0,0,
        4,22,1,0,0,0,6,38,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,
        11,12,6,1,-1,0,12,13,3,4,2,0,13,19,1,0,0,0,14,15,10,2,0,0,15,16,
        7,0,0,0,16,18,3,4,2,0,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,
        19,20,1,0,0,0,20,3,1,0,0,0,21,19,1,0,0,0,22,23,6,2,-1,0,23,24,3,
        6,3,0,24,30,1,0,0,0,25,26,10,2,0,0,26,27,7,1,0,0,27,29,3,6,3,0,28,
        25,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,5,1,0,0,
        0,32,30,1,0,0,0,33,39,5,7,0,0,34,35,5,5,0,0,35,36,3,2,1,0,36,37,
        5,6,0,0,37,39,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,39,7,1,0,0,0,3,
        19,30,38
    ]

class RationalParser ( Parser ):

    grammarFileName = "Rational.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FRACTION", 
                      "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "prog", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    FRACTION=7
    INT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(RationalParser.ExprContext,0)


        def EOF(self):
            return self.getToken(RationalParser.EOF, 0)

        def getRuleIndex(self):
            return RationalParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RationalParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(RationalParser.EOF)
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
            return RationalParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RationalParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(RationalParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ToTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RationalParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToTerm" ):
                listener.enterToTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToTerm" ):
                listener.exitToTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTerm" ):
                return visitor.visitToTerm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RationalParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RationalParser.ToTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RationalParser.AddSubContext(self, RationalParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 14
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 15
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 16
                    self.term(0) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RationalParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToFactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(RationalParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToFactor" ):
                listener.enterToFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToFactor" ):
                listener.exitToFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToFactor" ):
                return visitor.visitToFactor(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalParser.TermContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(RationalParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(RationalParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RationalParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = RationalParser.ToFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 23
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = RationalParser.MulDivContext(self, RationalParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 25
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 26
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 27
                    self.factor() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RationalParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RationalParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class FractionContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RationalParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FRACTION(self):
            return self.getToken(RationalParser.FRACTION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFraction" ):
                listener.enterFraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFraction" ):
                listener.exitFraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFraction" ):
                return visitor.visitFraction(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = RationalParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = RationalParser.FractionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(RationalParser.FRACTION)
                pass
            elif token in [5]:
                localctx = RationalParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(RationalParser.T__4)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(RationalParser.T__5)
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
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




