"""
Los operadores booleanos.
Hay un orden de operaciones para operadores booleanos:
not se evalúa primero
and se evalúa a continuación
or es evaluado por último.
https://docs.python.org/3/reference/expressions.html#operator-precedence
"""
name = "miguel"
age = 17

print(name == "miguel" or not age < 21)

print(name is "Ellis" or not (name is "miguel" and age == 17))

x = 1 + 2 ** 3 / 4 * 5
print(x)