import lex as Lexical
import token as Token 
import syntactic as Syntactic

if __name__ == '__main__':
  filename = "Archivo_Fuente.txt"
  
  print (" //------------------------ Lexical Analysis ------------------------//")
  tokens, errors, symbols = Lexical.analyze(filename)
  for token in tokens:
    print(Token.string(token))

  print('||---------------------- Symbol Table --------------------||')
  for id in symbols:
    print(Token.string(symbols[id]))


  if (len(errors) > 0):
    print('||------------------------ Errors ------------------------||')
  for error in errors:
    print(Token.string(error))

  if (len(errors) == 0):
    print (" //------------------------ Syntactic Analysis ------------------------//")
    symbolTable, error = Syntactic.analyze(tokens, symbols)

    if error:
      print("Error-->",error)
    else:
      #print(symbolTable)
      for symbol in symbolTable:
        print(str(symbol) +  "--" + str(symbolTable[symbol]))
        