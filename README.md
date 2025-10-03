# Presentación 7 – Soluciones a Ejercicios 1, 2 y 3

Este repositorio contiene soluciones trabajadas **a partir del ejemplo de gramática** que aparece en la presentación (función `A()` y `emparejar(...)`), donde los *tokens* usados son `UNO`, `DOS`, `TRES`, `CUATRO` y se observa un descenso recursivo.

> **Gramática base:**
>
> A → B UNO | DOS  
> B → TRES | CUATRO

> si el *token* inicial es `TRES` o `CUATRO`, se llama `B()` y luego se empareja `UNO`; si el *token* inicial es `DOS`, se empareja `DOS`; en cualquier otro caso hay error de sintaxis. Eso corresponde exactamente a la gramática anterior.

Contenido:
- `solutions/ex1_first_follow.md`: **Ejercicio 1** – Cálculo detallado de conjuntos **FIRST** y **FOLLOW**.
- `solutions/ex2_parse_table.md`: **Ejercicio 2** – Tabla **LL(1)** y verificación de condiciones.
- `src/python/rdp.py`: **Ejercicio 3** – Parser por **descenso recursivo** en Python + pruebas.
- `src/java/RecursiveDescent.java`: Alternativa mínima en Java (sin dependencias externas).
- `scripts/first_follow_ll1.py`: Utilidad para recomputar FIRST/FOLLOW y tabla de predicción a partir de la gramática.

> Si el enunciado oficial de los ejercicios 1–3 difiere, puedes actualizar la gramática en `scripts/first_follow_ll1.py` (diccionario `GRAMMAR`) y volver a generar resultados.
