from antlr4 import *
from RationalLexer import RationalLexer
from RationalParser import RationalParser
from RationalVisitor import RationalVisitor

class MyFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        self.numerator = numerator
        self.denominator = denominator
    
    def add(self, other):
        if self.denominator == other.denominator:
            # denominadores iguales: sumar numeradores directamente
            return MyFraction(
                self.numerator + other.numerator,
                self.denominator
            )
        else:
            # denominadores diferentes: utilizar la formula estandar
            return MyFraction(
                self.numerator * other.denominator + self.denominator * other.numerator,
                self.denominator * other.denominator
            )
    
    def subtract(self, other):
        if self.denominator == other.denominator:
            # denominadores iguales: restar numeradores directamente
            return MyFraction(
                self.numerator - other.numerator,
                self.denominator
            )
        else:
            # denominadores diferentes: utilizar la formula estándar
            return MyFraction(
                self.numerator * other.denominator - self.denominator * other.numerator,
                self.denominator * other.denominator
            )
    
    def multiply(self, other):
        # a/b * c/d = (a*c) / (b*d)
        return MyFraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )
    
    def divide(self, other):
        # (a/b) / (c/d) = (a*d) / (b*c)
        if other.numerator == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return MyFraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# implementacion del Visitor
class EvalVisitor(RationalVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())
    
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        op = ctx.op.text
        if op == '+':
            return left.add(right)
        else:
            return left.subtract(right)
    
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        op = ctx.op.text
        if op == '*':
            return left.multiply(right)
        else:
            try:
                return left.divide(right)
            except ZeroDivisionError as e:
                print(f"Error: {e}")
                return None
    
    def visitFraction(self, ctx):
        frac_text = ctx.FRACTION().getText()
        numerator, denominator = map(int, frac_text.split('/'))
        try:
            return MyFraction(numerator, denominator)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None
    
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitToTerm(self, ctx):
        return self.visit(ctx.term())
    
    def visitToFactor(self, ctx):
        return self.visit(ctx.factor())

# funcion principal para ejecutar el evaluador
def main():
    print("Evaluador de Fracciones. Ingresa 'exit' para salir.")
    while True:
        try:
            expr = input('expr> ')
            if expr.strip().lower() == 'exit':
                break
            if not expr:
                continue
            input_stream = InputStream(expr)
            lexer = RationalLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = RationalParser(stream)
            tree = parser.prog()
            visitor = EvalVisitor()
            result = visitor.visit(tree)
            if result is not None:
                print(f'= {result}')
        except EOFError:
            break
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()
