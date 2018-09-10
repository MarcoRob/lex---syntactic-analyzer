# Lex and Syntactic Analyzer
Lexical and Syntactic analyzer for Compie Design Course

## Grammar (Backus Naur Form)
```
<fuente> ::= [<bloque_funcion>] <principal>

<bloque_funcion> ::= {<funcion>}

<principal> ::= principal '(' ')' [<declaraciones>] 
                [<operaciones>] '}'

<funcion> ::= <tipo_dato> <id> '(' [<argumentos>]')'
                '{' [<declaraciones>] [<operaciones>]   
                <regresa>'}'
                
<operaciones>
<expresiones> ::= <id> '=' <expresion> ';'
<expresion> ::= <aritmetica> | <logica> | <relacionales> | <asignacion> | !<id>

<id>
<argumentos>
<regresa>
<declaraciones>
```
