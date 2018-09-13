import token as Token
tokens = []
errors = []
symbols = {}
keywords = ["entero", "real", "logico", "regresa", "si", "mientras", "principal", "verdadero", "falso"]
unique_tokens = ['+','-','*','^', '/', '<', '>', '!', '&', '|', ',', ';', '(', ')', '{', '}']

initLower = ord('a')
finalLower = ord('z')
minNum = ord('0')
maxNum = ord('9')
initUpper = ord('A')
finalUpper = ord('Z')

def validateToken(typeToken, valToken, line, char):
  isIdentifier = False
  if isSpecialChar(valToken):
    return -1
  if typeToken == Token.ERROR:
    errors.append(Token.build(typeToken, valToken, line, char))
    return -1
  if typeToken == Token.IDENTIFIER:
    isIdentifier = True
    if (valToken in keywords):
      print("val_k", valToken)
      typeToken = Token.KEYWORD
    #elif valToken not in symbols:
    #  print("val_sym", valToken)
    #  symbols[valToken] = Token.build(typeToken, valToken, line, char)
    else:
      print("val_else", valToken)
      temp = validate_types(valToken)
      print("type "+str(typeToken), valToken)
      print("type "+str(temp), valToken)
      if temp != -1:
        typeToken = temp
        isIdentifier = False
  if(isIdentifier) :
    addToken(typeToken, valToken, line, char)
  else :
    addToken(validate_types(valToken), valToken, line, char)
  
def addToken(tokenType, valToken, line, char):
  if(tokenType >= 0 and tokenType <= 9):
    tokens.append(Token.build(tokenType, valToken, line, char))

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def validate_types(val) :
  if (val == '+' or val == '-' or val == '*' or val == '/' or val == '^'):
    return Token.ARITMETHIC
  elif (val == '<' or val == '>'):
    return Token.RELATIONAL
  elif (val == ';' or val == ',' or val == '(' or val == ')' or val == '{' or val == '}'):
    return Token.PUNCTUATION
  elif (val == '!' or val == '&' or val == '|'):
    return Token.LOGICAL
  elif (val == '=') :
    return Token.ASSIGMENT
  elif (val == '==') :
    return Token.RELATIONAL
  else:
    return -1

def isSpecialChar(val) :
  if val == '\n':
    print("special_char /n", True)
    return True
  elif val == '\t': 
    print("special_char /t", True)
    return True
  elif val == '\r': 
    print("special_char /r", True)
    return True
  elif val == ' ':
    print("special_char /s", True)
    return True

  print("special_char", False)
  return False

def isUnaryChar(val) :
  unaryChars = {
    ';':True,
    ',':True,
    '(':True,
    ')':True,
    ')':True,
    '{':True,
    '}':True,
    '!':True,
    '&':True,
    '|':True,
    '<':True,
    '>':True,
    '+':True,
    '-':True,
    '*':True,
    '/':True,
    '^':True
  }
  return unaryChars.get(val, False)
    
def canBeLowerLetter(val) :
  initLimit = ord('a')
  finalLimit = ord('z')
  return (ord(val) >= initLimit and ord(val) <= finalLimit)

def canBeNumber(val) :
  numChar = ord(val)
  minNum = ord('0')
  maxNum = ord('9')
  isInRangeNumber = (minNum >= numChar and maxNum <= numChar)
  return isInRangeNumber

def canBeIdentifier(val) :
  numChar = ord(val)
  isInRangeLowerCase = (initLower <= numChar and finalLower >= numChar)
  isInRangeUpperCase = (initUpper <= numChar and finalUpper >= numChar)
  isInRangeNumber = (minNum <= numChar and maxNum >= numChar)

  return (isInRangeLowerCase or isInRangeUpperCase or isInRangeNumber)

def analyze(filename):
  with open(filename, 'r') as file:
    NO_TOKEN_TYPE = -1
    line = file.readline()
    linePos = 0
    charPos = 0
    tokenOption = NO_TOKEN_TYPE
    charInit = 0
    charVal = ''

    while line:
      charPos = 0
      while charPos < len(line):
        character = line[charPos]

        if isSpecialChar(character) :
          validateToken(tokenOption, charVal, linePos, charInit)
          tokenOption = NO_TOKEN_TYPE
          charPos += 1
          charVal = ""
          continue
        
        if isUnaryChar(character) :
          validateToken(tokenOption, charVal, linePos, charInit)
          validateToken(tokenOption, character, linePos, charPos)
          tokenOption = NO_TOKEN_TYPE
          charPos += 1
          charVal = ""
          continue

        if tokenOption == -1 and canBeLowerLetter(character) :
          charInit = charPos
          charVal += character
          charPos += 1
          tokenOption = Token.IDENTIFIER
          continue

        if tokenOption == Token.IDENTIFIER and canBeIdentifier(character) :
          charVal += character
          charPos += 1
          continue

        if tokenOption == -1 and canBeNumber(character) :
          charInit = charPos
          charVal += character
          charPos += 1
          tokenOption = Token.INTEGER
          continue

        if (tokenOption == Token.INTEGER or tokenOption == Token.REAL) and canBeNumber(character) :
          charVal += character
          charPos += 1
          continue

        if tokenOption == Token.INTEGER and character == '.' :
          charVal += character
          charPos += 1
          character = line[charPos]
          if canBeNumber :
            charVal += character
            charPos += 1
            tokenOption = Token.REAL
            continue
          else :
            charVal += character
            charPos += 1
            tokenOption = Token.ERROR
            continue

        if character == '=' :
          validateToken(tokenOption, charVal, linePos, charPos)   
          charVal = ""
          tokenOption = -1
          nextChar = line[charPos+1]
          if nextChar == '=' :
            validateToken(Token.RELATIONAL, '==', linePos, charPos)
            charPos += 2
            continue
          else :
            validateToken(Token.ASSIGMENT, '=', linePos, charPos)
            charPos += 1
            continue

        tokenOption = Token.ERROR
        charPos += 1
        charVal += character

        print("val", character)
        print("tokenOption", tokenOption)
      
      line = file.readline()
      linePos += 1
    validateToken(tokenOption, charVal, linePos-1, charInit)
    return tokens

        

      
