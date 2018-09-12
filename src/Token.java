import java.util.ArrayList;

public class Token {


    public static final int ERROR = 0;
    public static final int IDENTIFIER = 1; // id
    public static final int ARITMETHIC = 2; // +, -, *, /, ^
    public static final int RELATIONAL = 3; // >, <, ==
    public static final int LOGICAL = 4; // &, |, !
    public static final int ASSIGMENT = 5; // =
    public static final int PUNCTUATION = 6; // =
    public static final int LOGICO = 7;
    public static final int KEYWORD = 8;
    public static final int ENTERO = 9;
    public static final int REAL = 10;

    private int tokenType;
    private String tokenValue;
    private int line;
    private int character;

    public Token(int tokenType, String tokenValue, int line, int character) {
        this.tokenType = tokenType;
        this.tokenValue = tokenValue;
        this.line = line;
        this.character = character;
        //System.out.println(this.toString());

    }

    public String toString() {
        return "Type: " + this.tokeTypeStr() + " Val: " + this.tokenValue + " Line: " + this.line + " Character Pos: " + this.character;
    }

    private String tokeTypeStr() {
        String type;
        switch (this.tokenType) {
            case ERROR:
                type = "ERROR";
                break;
            case IDENTIFIER:
                type = "IDENTIFIER";
                break;
            case ARITMETHIC:
                type = "ARITMETHIC";
                break;
            case RELATIONAL:
                type = "RELACIONAL";
                break;
            case LOGICAL:
                type = "LOGICAL";
                break;
            case PUNCTUATION:
                type = "PUNCTUATION";
                break;
            case KEYWORD:
                type = "KEYWORD";
                break;
            case LOGICO:
                type = "LOGICO";
                break;
            case REAL:
                type = "REAL";
                break;
            case ENTERO:
                type = "ENTERO";
                break;
            default:
                type = "ERROR";
                break;
        }
        return type;
    }

}
