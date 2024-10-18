# Parcial 2 - Lenguajes de Programación

Explicación de las soluciones, e implementación de las mismas.

## Tabla de Contenidos

- [Requisitos](#Requisitos)
- [Punto 1](#Punto1)
- [Punto 2](#punto2)
- [Punto 3](#punto3)

## Requisitos

Tras haber clonado el repositorio, se debe crear y activar un entorno virtual de Python, así:

 ```bash
python3 -m venv venv
source ven/bin/activate
 ```

Luego, dpara replicar el proyecto de forma adecuada, se deben instalar los siguientes requisitos:

```bash
pip install antlr4-python3-runtime
pip install antlr4-python3-runtime sympy
pip install antlr4-python3-runtime numpy
```

En cada punto, para generar el lexer, parser y el visitor con Python, se debe ejecutar `antlr4 -Dlanguage=Python3 -visitor Rational.g4`.

## Punto 1

Al ejecutar `python visitor.py` se abre una terminal "interna" de la forma `expr>` en la cual se puede ejecutar operaciones entre racionales, a menos de que se ingrese `exit`
Debería verse de la siguiente forma:

```bash
expr> (1/3 + 2/3)
= 1
expr> (1/2 * 3/4)
= 3/8
expr> 4/5 - 2/5
= 2/5
expr> (1/3 + 2/3) * (3/3)
= 1
expr> 1/0 + 2/3
Error: División por cero en la fracción.
expr> 
```

## Punto 2

Al ejecutar `python main.py` se abre una terminal "interna" en la cual se pueden pasar distintas líneas de la forma FILTER(function, iterable) o MAP(function, iterable), separadas por punto y coma, al presionar `CTRL + D`, se mostrará línea a línea el resultado producido por cada linea ingresada.
Por defecto, la gramática acepta las siguientes funciones:

```bash
self.functions = {
        'abs': abs,
        'round': round,
        'int': int,
        'float': float,
        'str': str,
        'max': max,
        'min': min,
        'sum': sum,
        'len': len,
        'upper': str.upper,
        'lower': str.lower,
        'capitalize': str.capitalize,
        'strip': str.strip,
        'bool': bool,
        'all': all,
        'any': any,
        'sorted': sorted,
        'reversed': lambda x: list(reversed(x)),
    }
    import math
    self.math_functions = {
        'sqrt': math.sqrt,
        'ceil': math.ceil,
        'floor': math.floor,
        'sin': math.sin,
        'log': math.log,
    }
    self.conditional_functions = {
        'multiple': self.multiple,
        'es_par': self.es_par,
        'es_impar': self.es_impar,
        'es_positivo': self.es_positivo,
        'es_negativo': self.es_negativo,
        'mayor_que': self.mayor_que,
        'menor_que': self.menor_que,
        'entre': self.entre,
        'es_primo': self.es_primo,
        'divisible_por_ambos': self.divisible_por_ambos,
        'divisible_por_cualquiera': self.divisible_por_cualquiera,
        'empieza_con': self.empieza_con,
        'termina_con': self.termina_con,
        'contiene_subcadena': self.contiene_subcadena,
        'longitud_mayor_que': self.longitud_mayor_que,
    }
```

Por ejemplo, la entrada 

```bash
MAP(int, [1.1, 2.5, 3.9]);
FILTER(es_negativo, [-5, -3, 0, 2, 4]);
MAP(len, ['apple', 'banana', 'cherry']);
FILTER(empieza_con('b'), ['apple', 'banana', 'berry', 'cherry']);
MAP(reversed, [[1, 2], [3, 4], [5, 6]]);
FILTER(es_primo, [1, 2, 3, 4, 5, 6, 7]);
```

debería producir:

```bash
[1, 2, 3]
[-5, -3]
[5, 6, 6]
['banana', 'berry']
[[2, 1], [4, 3], [6, 5]]
[2, 3, 5, 7]
```

Tambien se aceptan MAP y FILTER anidados.

## Punto 3

Al ejecutar `python main.py` se abre una terminal "interna" en la cual se deben ingresar dos líneas de la forma:

```bash
function f(t) = 'Aqui se ingresa en forma de markdown la función a la cual se le desea calcular la transformada de Laplace';
Laplace f(t);
```

luego, al presionar `CTRL + D`, se mostrará la transformada de Laplace de la función ingresada.
Por ejemplo, la entrada

```bash
function f(t) = t^2 * exp(-3 * t) * sin(4 * t);
Laplace f(t);
```

produce:

```bash
La transformada de Laplace de f(t) es: (8*(s + 3) - 160)/((s + 3)**2 + 16)**3
```
