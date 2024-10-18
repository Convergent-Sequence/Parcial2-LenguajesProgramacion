grammar Rational;

options { 
    language=Python3; 
    visitor=true; 
}

// Punto de entrada de la gramática
prog: expr EOF;

// Definición de expresiones con precedencia
expr: expr op=('+' | '-') term   # AddSub
    | term                       # ToTerm
    ;

term: term op=('*' | '/') factor # MulDiv
    | factor                     # ToFactor
    ;

factor: FRACTION                 # Fraction
      | '(' expr ')'             # Parens
      ;

// Definición de un número fraccionario (e.g., 1/3)
FRACTION: INT '/' INT;

// Definición de enteros
INT: [0-9]+;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip;

