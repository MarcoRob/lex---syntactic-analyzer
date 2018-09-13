import lex as Lexical
import token as Token 

if __name__ == '__main__':
  filename = "Archivo_Fuente.txt"
  print(Lexical.validate_types('+'))
  tokens = Lexical.analyze(filename)
  for token in tokens:
    print(Token.string(token))
