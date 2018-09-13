import token as Token

symbolsTable = {}
tokensTable = []

def error(message, token):
  return message + Token.sring(token)

'''  
def validateToken(token_key, token_val, line, charPos, ) :
  if tokensTable[charPos].get(key) == token_val :
    if token_val == Token.IDENTIFIER:
      tokenType = tokensTable[charPos]
'''

# Analyze the tokens and return Symbol Table and Errors (if their exit)
def analyze(tokens, symbols) :
  tokensTable = tokens
  symbolsTable = {}
  initialPos = 0;
  initialLine = 0
  
  principalPos, errPrincipal = validatePrincipal()
  if errPrincipal:
    return None, errPrincipal

  for token in tokens:
    if(token["type"] == Token.IDENTIFIER):


def validatePrincipal() :
  count = 0
  hasPrincipal = False
  for token in tokens:
    if(token[token]["value"] == "principal"):
      if not hasPrincipal:
        count = token
        hasPrincipal = True
      else:
        return count, error("Solo puede haber un principal")
  return count, None
    


