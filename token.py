ERROR = 0
KEYWORD = 1
IDENTIFIER = 2
LOGICAL = 3
RELATIONAL = 4
ARITMETHIC = 5
PUNCTUATION = 6
INTEGER = 7
REAL = 8
ASSIGMENT = 9


def build(type, val, line, charPos) :
  return {"type":type, "val":val, "line":line, "char":charPos}

def string(token) :
  tokenDic = {
    0:'ERROR',
    1:'KEYWORD',
    2:'IDENTIFIER',
    3:'LOGICAL',
    4:'RELATIONAL',
    5:'ARITMETHIC',
    6:'PUNCTUATION',
    7:'INTEGER',
    8:'REAL',
    9:'ASSIGMENT'
  }
  return ("Type " + str(tokenDic.get(token.get("type"))) + " Val '" + str(token.get("val")) + 
          "' Line " + str(token.get("line")) + " Char Pos " + str(token.get("char")))