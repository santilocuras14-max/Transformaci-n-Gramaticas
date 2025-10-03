// Parser por descenso recursivo equivalente (versión mínima en Java).
// Compilar: javac RecursiveDescent.java
// Ejecutar:  java RecursiveDescent "TRES UNO"
import java.util.*;

class ParserError extends RuntimeException {
    ParserError(String msg) { super(msg); }
}

class Lexer {
    private final List<String> tokens;
    private int pos = 0;

    Lexer(String source) {
        tokens = new ArrayList<>();
        for (String t : source.trim().split("\\s+")) {
            if (!t.isBlank()) tokens.add(t.toUpperCase());
        }
        tokens.add("$");
    }

    String peek() { return tokens.get(pos); }
    String next() { return tokens.get(pos++); }
}

public class RecursiveDescent {
    private final Lexer lex;
    private String token;

    public RecursiveDescent(Lexer lex) {
        this.lex = lex;
        this.token = lex.next();
    }

    private void match(String expected) {
        if (token.equals(expected)) {
            token = lex.next();
        } else {
            throw new ParserError("Se esperaba " + expected + ", se encontró " + token);
        }
    }

    // A → B UNO | DOS
    private void A() {
        if (token.equals("TRES") || token.equals("CUATRO")) {
            B();
            match("UNO");
        } else if (token.equals("DOS")) {
            match("DOS");
        } else {
            throw new ParserError("Error de sintaxis en A con token: " + token);
        }
    }

    // B → TRES | CUATRO
    private void B() {
        if (token.equals("TRES")) {
            match("TRES");
        } else if (token.equals("CUATRO")) {
            match("CUATRO");
        } else {
            throw new ParserError("Error de sintaxis en B con token: " + token);
        }
    }

    public boolean parse() {
        A();
        if (!token.equals("$")) {
            throw new ParserError("Fin de archivo esperado, encontrado: " + token);
        }
        return true;
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Uso: java RecursiveDescent \"TRES UNO\"");
            return;
        }
        try {
            boolean ok = new RecursiveDescent(new Lexer(args[0])).parse();
            System.out.println(ok ? "Aceptada" : "Rechazada");
        } catch (ParserError e) {
            System.out.println("Rechazada: " + e.getMessage());
        }
    }
}
