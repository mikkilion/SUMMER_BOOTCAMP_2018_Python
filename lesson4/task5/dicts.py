"""
Un diccionario es similar a una lista, excepto que
tiene acceso a sus valores buscando una clave en lugar de un índice
"""

phone_book = {"John": 2424, "Jane": 2348, "Jerard": 3000}
print(phone_book)


phone_book["Jill"] = 3450
print(phone_book)


phone_book.pop("Jane")

print(phone_book["Jerard"])
print(phone_book["John"])
print(phone_book["Jerard"])