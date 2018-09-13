import token as Token

symbolsTable = {}
tokensTable = []

data_type = ['entero', 'logico', 'real']

def error(message, token, pos=None):
  if pos:
    return "Msg " + message + ", err[ Token-" + Token.string(token) + " ]"
  return "Msg " + message + ", err[ Token-" + Token.string(token) + " ]"

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
  
  principalPos, errPrincipal = validatePrincipal(tokens)
  if errPrincipal:
      return [], errPrincipal

  funcionesPos, errFunciones = validateFunciones(tokens)
  if errFunciones:
    return funcionesPos, errFunciones


  return symbolsTable, None
      

def validateFunciones(tokens) :
  count = 0
  tokenFunc = []
  for i in range(len(tokens)):
    token = tokens[i]
    if(token['val'] in data_type) :
      i += 1
      token = tokens[i]
      if(token['type'] is Token.IDENTIFIER) :
        i += 1
        token = tokens[i]
        if(token['val'] == '(') :
          i += 1
          token = tokens[i]
          ##print("type__", token['type'])
          if(token['type'] is Token.KEYWORD) :
            i += 1
            token = tokens[i]
            if(token['type'] is Token.IDENTIFIER) :
              symbolsTable[tokens[i]['val']] = {"type":Token.IDENTIFIER, "val":tokens[i]['val'], "line":tokens[i]['line'], 'char':tokens[i]['char']}
              i += 1
              token = tokens[i]
              hasMoreArguments = True
              while hasMoreArguments :
                token = tokens[i]
                #print("___val___", token['val'])
                if token['val'] == ',':
                  i +=1
                  token = tokens[i]
                  #print("___val2___", token['val'])
                  if token['val'] in data_type:
                    i +=1
                    token = tokens[i]
                    #print("___val3___", token['val'])
                    if token['type'] is Token.IDENTIFIER :
                      #print("___val4___", token['val'])
                      symbolsTable[tokens[i]['val']] = {"type":Token.IDENTIFIER, "val":tokens[i]['val'], "line":tokens[i]['line'], 'char':tokens[i]['char']}
                      i += 1
                      continue
                    else :
                      #print("_id2_")
                      return [], error("id esperado", token, i)
                  else :
                    return [], error("tipo de dato esperado", token, i)
                elif token['val'] == ')':
                  #print("__val5__", token['val'])
                  hasMoreArguments = False
                else :
                  return [], error(", esperado", token, i)
            if(token['val'] == ')'):
              #print("algo")
              i += 1
              continue
            else:
              return [], error(") faltante", token, i)
          else :
            if(token['val'] == ')'):
              continue
            return [], error(str(data_type) + " esperado", token, i)
        else :
          return [], error("( esperado", token, i)
      else :
        #print("_id1_")
        return [], error("id esperado", token, i)
    else :
      return [], error(str(data_type) + " esperado", token, i)
  return [], None

def validatePrincipal(tokens) :
  count = 0
  hasPrincipal = False
  for token in tokens:
    if(token['val'] == "principal"):
      if not hasPrincipal:
        hasPrincipal = True
      else:
        return count, error("Solo puede haber un principal", token)
    
    count += 1   

  return count, None
    


