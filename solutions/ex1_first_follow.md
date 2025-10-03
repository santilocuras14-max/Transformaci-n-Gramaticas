# Ejercicio 1 – FIRST y FOLLOW (paso a paso)

**Gramática**  
A → B UNO | DOS  
B → TRES | CUATRO

## FIRST
- FIRST(TRES)=\{TRES\}  (terminal)
- FIRST(CUATRO)=\{CUATRO\}
- FIRST(UNO)=\{UNO\}, FIRST(DOS)=\{DOS\}

- FIRST(B):
  - B → TRES ⇒ aporta {TRES}
  - B → CUATRO ⇒ aporta {CUATRO}
  ⇒ **FIRST(B) = {TRES, CUATRO}**

- FIRST(A):
  - A → B UNO ⇒ aporta FIRST(B) = {TRES, CUATRO}
  - A → DOS   ⇒ aporta {DOS}
  ⇒ **FIRST(A) = {TRES, CUATRO, DOS}**

## FOLLOW
Colocamos `$` en FOLLOW(A) por ser el símbolo inicial.

- De A → B UNO, **UNO** sigue a **B** ⇒ UNO ∈ FOLLOW(B).
  *Como UNO es terminal, no añade más propagación.*
- No hay producciones con B al final que arrastren FOLLOW(A) hacia FOLLOW(B).

Por tanto:
- **FOLLOW(A) = { $ }**
- **FOLLOW(B) = { UNO }**
