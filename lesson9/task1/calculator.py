class Calculator:
    def __init__(self):
        self.current = 0


    def add(self , amount):
        self.current += amount

    def get_curret(self):
        return self.current
