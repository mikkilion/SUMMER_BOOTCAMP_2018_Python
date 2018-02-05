"""
La función len() se usa para contar cuántos caracteres contiene una cadena.
obtener la primera mitad de la frase
"""
phrase = """
pepito esta tomando cursos
de ciberseguridad, forence

"""
first_half = phrase[:int(len(phrase)/5)]
print(first_half)