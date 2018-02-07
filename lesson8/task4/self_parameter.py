"""
self es el primer parámetro que se pasa a cualquier método de clase.
Python usará el parámetro self para referirse al objeto que se está creando.
"""
class Complex:

    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part
    return

class Calculator:
    current = 0

    def add(self, amount):
        current += amount

    def get_current(self):
        return current

# Para Complex cree el objeto y realize una llamada al metodo


# Para Calculator cree el objeto y realize llamadas a los metodos
# identifique y resuelva el problema