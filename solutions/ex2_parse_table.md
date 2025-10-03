# Ejercicio 2 – Tabla LL(1) y verificación

**Gramática**  
A → B UNO | DOS  
B → TRES | CUATRO

## Tabla de predicción M[NoTerminal, Terminal]
Usamos FIRST y, cuando procede, FOLLOW (no hay ε-producciones aquí).

- Para **A**:
  - A → B UNO se coloca en columnas de FIRST(B) = {TRES, CUATRO}:
    - M[A, TRES]   = A → B UNO
    - M[A, CUATRO] = A → B UNO
  - A → DOS se coloca en FIRST(DOS) = {DOS}:
    - M[A, DOS] = A → DOS

- Para **B**:
  - B → TRES  ⇒ M[B, TRES]  = B → TRES
  - B → CUATRO ⇒ M[B, CUATRO] = B → CUATRO

No hay entradas múltiples por celda ⇒ **La gramática es LL(1)**.

|     M     | TRES         | CUATRO       | DOS        | UNO |
|:---------:|:------------:|:------------:|:----------:|:---:|
| **A**     | A → B UNO    | A → B UNO    | A → DOS    |     |
| **B**     | B → TRES     | B → CUATRO   |            |     |

**Derivaciones de ejemplo**  
- Entrada `TRES UNO`:
  - A ⇒ B UNO ⇒ TRES UNO ✓
- Entrada `CUATRO UNO`:
  - A ⇒ B UNO ⇒ CUATRO UNO ✓
- Entrada `DOS`:
  - A ⇒ DOS ✓
