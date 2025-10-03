"""
Parser por descenso recursivo para la gramática:

A → B UNO | DOS
B → TRES | CUATRO

Se asume que la entrada ya es una secuencia de *tokens* en mayúscula: "TRES", "CUATRO", "UNO", "DOS".
"""

from typing import List

class ParserError(Exception):
    pass

class Lexer:
    """
    Lexer mínimo que acepta una cadena con tokens separados por espacios.
    Ej: "TRES UNO", "DOS", "CUATRO UNO".
    También admite una lista de cadenas ya tokenizadas.
    """
    def __init__(self, source):
        if isinstance(source, str):
            self.tokens = [t.strip().upper() for t in source.split() if t.strip()]
        else:
            self.tokens = [str(t).upper() for t in source]
        self.tokens.append("$")  # Fin de entrada
        self.pos = 0

    def peek(self) -> str:
        return self.tokens[self.pos]

    def next(self) -> str:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

class RecursiveDescentParser:
    def __init__(self, lexer: Lexer):
        self.lex = lexer
        self.token = self.lex.next()

    def match(self, expected: str):
        if self.token == expected:
            self.token = self.lex.next()
        else:
            raise ParserError(f"Se esperaba {expected}, se encontró {self.token}")

    # A → B UNO | DOS
    def A(self):
        if self.token in ("TRES", "CUATRO"):
            self.B()
            self.match("UNO")
        elif self.token == "DOS":
            self.match("DOS")
        else:
            raise ParserError(f"Error de sintaxis en A. Token inesperado: {self.token}")

    # B → TRES | CUATRO
    def B(self):
        if self.token == "TRES":
            self.match("TRES")
        elif self.token == "CUATRO":
            self.match("CUATRO")
        else:
            raise ParserError(f"Error de sintaxis en B. Token inesperado: {self.token}")

    def parse(self) -> bool:
        self.A()  # símbolo inicial
        if self.token != "$":
            raise ParserError(f"Fin de archivo esperado, encontrado: {self.token}")
        return True

def parse_input(s: str) -> bool:
    p = RecursiveDescentParser(Lexer(s))
    return p.parse()

if __name__ == "__main__":
    tests = [
        ("TRES UNO", True),
        ("CUATRO UNO", True),
        ("DOS", True),
        ("TRES DOS", False),
        ("UNO", False),
        ("CUATRO", False),
        ("TRES UNO $", False),  # '$' no debe venir en la entrada del usuario
    ]
    for src, ok in tests:
        try:
            res = parse_input(src)
            print(f"[OK] {src!r} ⇒ aceptada")
        except ParserError as e:
            if ok:
                print(f"[FALLO] {src!r}: {e}")
            else:
                print(f"[OK] {src!r} ⇒ rechazada ({e})")
