"""
La palabra clave "in" se usa para verificar si una lista o un diccionario
contiene un elemento específico.
Se puede aplicar a listas o diccionarios
de la misma manera que se hizo con las cadenas.
"""
grocery_list = ["fish", "tomato", 'apples']

print("banana" in grocery_list)

grocery_dict = {"fish": 10, "tomato": 6, 'apples': 3}

print('fish' in grocery_dict)

print('fish:10' in grocery_dict )