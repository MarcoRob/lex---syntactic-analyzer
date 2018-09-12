import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Lex {

    private ArrayList<String> reserved;
    private ArrayList<Token> tokens;

    private int linePos;
    private int charPos;

    public Lex() {

        this.reserved = new ArrayList<>();
        this.tokens = new ArrayList<>();

        reserved.add("principal");
        reserved.add("entero");
        reserved.add("real");
        reserved.add("logico");
        reserved.add("si");
        reserved.add("mientras");
        reserved.add("regresa");
        reserved.add("verdadero");
        reserved.add("falso");


    }

    private boolean isEspecialChar(char val) {

        switch (val) {
            case '\t':
                System.out.println("especial char -t");
            case '\n':
                System.out.println("especial char -n");
            case ' ':
                System.out.println("especial char - -");
                return true;
            default:
                return false;
        }

    }

    private boolean isReservedWord(String word) {
        return this.reserved.contains(word);
    }

    private void addReservedWord(String word) {
        this.addToken(Token.KEYWORD, word);
    }

    private boolean isOperatorsChar(Character val, String line, int pos) {
        switch (val) {
            case '+':
            case '-':
            case '*':
            case '/':
            case '^':
                this.addToken(Token.ARITMETHIC, val.toString());
                return true;
            case '<':
            case '>':
                this.addToken(Token.RELATIONAL, val.toString());
                return true;
            case '=':
                boolean isEqualOperator = this.validEqualOperator(Token.ASSIGMENT, pos, line);
                if(!isEqualOperator) {
                    this.addToken(Token.ASSIGMENT, val.toString());
                }
                return true;
            default:
                return false;

        }
    }

    private boolean validEqualOperator(int tokenType, int characterPos, String line) {
        int position = characterPos;
        if(Token.ASSIGMENT == tokenType) {
            String str = "";
            char character = line.charAt(position);
            str += character;
            position++;
            character = line.charAt(position);
            str += character;
            if(str.equals("==")) {
            this.addToken(Token.RELATIONAL, str);
                this.charPos++;
                characterPos++;
                return true;
            }
            return false;
        }
        return false;
    }

    private boolean isPunctuationChar(Character val) {
        switch (val) {
            case ',':
            case ';':
            case '(':
            case ')':
            case '{':
            case '}':
                return true;
            default:
                return false;
        }
    }

    private void addPunctuationChar(Character c) {
        this.addToken(Token.PUNCTUATION, c.toString());
    }

    private boolean isNumberChar(String val) {

        String str = "";
        int dots = 0;
        for(int i=0; i<val.length(); i++) {
            Character character = val.charAt(i);
            if(!Character.isLetter(character)) {
                if(Character.isDigit(character)) {
                    str += character;
                    continue;
                }
                if(this.validDot(character)) {
                    dots ++;
                    str += character;
                    if(dots > 1) {
                        this.addToken(Token.ERROR, str);
                        return false;
                    }
                    str += character;
                }
            } else {
                return false;
            }


        }
        if(!str.equals(" ")) {
            if(dots == 1){
                this.addToken(Token.REAL, str);
                return true;
            } else {
                this.addToken(Token.ENTERO, str);
                return true;
            }
        }
        return false;
    }


    private boolean validDot(char val) {
        return '.' == val;
    }

    private void addToken(int tokenType, String val) {
        if(!val.isEmpty()) {
            this.tokens.add(new Token(tokenType, val, this.linePos, this.charPos));
        }

    }

    private boolean isIdentifier(String val) {

        String id = "";
        for(int i=0; i<val.length(); i++) {
            Character character = val.charAt(i);
            if(Character.isLetter(character) && i==0) {
                id += character;
            } else if (i > 0) {
                id += character;
            } else {
                this.addToken(Token.ERROR, id);
                return false;
            }
        }
        this.addToken(Token.IDENTIFIER, id);
        return true;

    }


    private void states(String currentLine) {

        String str = "";
        for (int i = 0; i < currentLine.length(); i++) {
            char currentChar = currentLine.charAt(i);


            if(!this.isEspecialChar(currentChar)) {
                if(this.isPunctuationChar(currentChar)) {
                    str += currentChar;
                    this.charPos++;
                    continue;
                }  else {
                    str += currentChar;
                    if(this.isOperatorsChar(currentChar, currentLine, i)) {
                        str = "";
                        this.charPos++;
                        continue;
                    } else {
                        if(this.isReservedWord(str)) {
                            this.charPos++;
                            continue;
                        } else {
                            if(this.isNumberChar(str)) {
                                this.charPos++;
                                continue;
                            } else {
                                if (this.isIdentifier(str)) {
                                    this.charPos++;
                                    continue;
                                }
                            }
                        }
                    }
                }
            } else {
                str = "";
                this.charPos++;
            }
            System.out.println(str);
        }
    }

    public void analyze(String filename) {

        try {

            FileReader fr = new FileReader(filename);
            BufferedReader br = new BufferedReader(fr);

            String sCurrentLine;

            charPos = 0;
            linePos = 0;

            while ((sCurrentLine = br.readLine()) != null) {
                this.states(sCurrentLine);
                this.linePos++;
                //System.out.println(sCurrentLine);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("---- Tokens -----");
        for(int i=0; i<this.tokens.size(); i++) {
            System.out.println(this.tokens.get(i));
        }
    }
}
