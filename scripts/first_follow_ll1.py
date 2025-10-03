"""
Herramienta para recomputar FIRST, FOLLOW y tabla LL(1) para una gramática dada.
Modifica GRAMMAR según necesites y ejecuta: `python first_follow_ll1.py`
"""
from collections import defaultdict, deque

# Gramática base (no hay ε-producciones aquí).
# Usa una lista por alternativa; cada alternativa es lista de símbolos (str).
GRAMMAR = {
    "A": [["B", "UNO"], ["DOS"]],
    "B": [["TRES"], ["CUATRO"]],
}
START = "A"
TERMINALS = {"UNO", "DOS", "TRES", "CUATRO"}

def compute_first(grammar, terminals):
    first = {nt: set() for nt in grammar}
    for t in terminals:
        first[t] = {t}
    changed = True
    while changed:
        changed = False
        for A, prods in grammar.items():
            for alpha in prods:
                # Avanza por la producción hasta que no haya ε (aquí no usamos ε explícito)
                X = alpha[0]
                before = len(first[A])
                first[A] |= first.get(X, set())
                changed |= (len(first[A]) != before)
    return first

def compute_follow(grammar, start, first, terminals):
    follow = {nt: set() for nt in grammar}
    follow[start].add("$")
    changed = True
    while changed:
        changed = False
        for A, prods in grammar.items():
            for alpha in prods:
                for i, B in enumerate(alpha):
                    if B in grammar:  # B es no terminal
                        if i+1 < len(alpha):
                            beta = alpha[i+1]
                            before = len(follow[B])
                            # FIRST(beta) sin ε; aquí beta es un único símbolo (no ε)
                            follow[B] |= (first.get(beta, set()) - {"ε"})
                            changed |= (len(follow[B]) != before)
                        else:
                            before = len(follow[B])
                            follow[B] |= follow[A]
                            changed |= (len(follow[B]) != before)
    return follow

def build_table(grammar, first, follow, terminals):
    table = defaultdict(dict)
    for A, prods in grammar.items():
        for alpha in prods:
            a = alpha[0]
            for a_sym in first.get(a, set()):
                if a_sym in terminals:
                    table[A][a_sym] = alpha
            if "ε" in first.get(a, set()):
                for b in follow[A]:
                    table[A][b] = alpha
    return table

def main():
    first = compute_first(GRAMMAR, TERMINALS)
    follow = compute_follow(GRAMMAR, START, first, TERMINALS)
    table = build_table(GRAMMAR, first, follow, TERMINALS)

    print("FIRST:")
    for k, v in first.items():
        if k in GRAMMAR:
            print(f"  FIRST({k}) = {sorted(v)}")
    print("\nFOLLOW:")
    for k, v in follow.items():
        print(f"  FOLLOW({k}) = {sorted(v)}")

    print("\nTabla LL(1):")
    for A, row in table.items():
        for a, prod in row.items():
            print(f"  M[{A}, {a}] = {A} → {' '.join(prod)}")

if __name__ == "__main__":
    main()
