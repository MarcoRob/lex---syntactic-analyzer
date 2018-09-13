# Lex and Syntactic Analyzer

Lexical and Syntactic analyzer for Compie Design Course

## Grammar (Backus Naur Form)

```
<fuente> ::= [<bloque_funciones>] <principal>

<bloque_funciones> ::= {<funcion>}

<principal> ::= principal '(' ')' [<declaraciones>]
                [<operaciones>] '}'

<funcion> ::= <tipo_dato> <id> '(' [<argumentos>] ')'
                '{' [<declaraciones>] [<operaciones>] <regresa> '}'

<tipo_dato> ::= 'entero'
            ::= 'logico'
            ::= 'real'

<argumentos> ::= { <argumento> [',' <argumento>]

<argumento> ::= <tipo_dato> <id>

<declaraciones> ::= { declaracion }

<declaracion> ::= <tipo_dato> <id> ';'

<regresa> ::= 'regresa' <id> ';'

<operaciones> ::= <sentencia_si>
              ::= <sentencia_mientras>
              ::= <expresiones>

<sentencia_si> ::= si '(' <id> ')' '{' [<expresiones>] '}'

<sentencia_mientras> ::= mientras '(' id ')' '{' [<expresiones>] '}'

<expresiones> ::= <asignacion>
              ::= <llamada_funcion> ';'

<asgnacion> ::= <id> '=' <expresion> ';'

<expresion> ::= <aritmetica> | <logica> | <relacional> | <id> | '!'<id>

<llamada_funcion> ::= <id> '(' [<argumentos>]')'

<aritmetica> ::= '(' <aritmetica> ')'
             ::= <valor_aritmetico>
             ::= <aritmetica> [<operador_aritmetico> <aritmetica>]

<valor_aritmetico> ::= <id> | <entero> | <real> | <llamada_funcion>

<entero> ::= // [0..9]

<real> ::= // {[0..9]} '.' {[0..9]}

<operador_aritmetico> ::= '+' | '-' | '*' | '/' | '^'

<logica> ::= '(' <logica> ')'
         ::= <valor_logico>
         ::= <logica> [<operador_logico> <logica>]

<valor_logico> ::= '&' | '|'

<relacional> ::= <valor_aritmetico> <operador_relacional> <valor_aritmetico>

<operador_relacional> ::= '<'| '>' | '=='

<id> ::= { <abc> }
         [ <num> ]
         [ <ABC>]
```

## Build and Run

In order to run the project, you will need to have install `python3` and the code file `txt` in the same root/folder

To run just set the following command:

```
python3 main.py
```
