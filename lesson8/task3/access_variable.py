class Car:
    color = ""
    def description(self):
        description_string = "This is a %s car." % self.color
        return description_string

car1 = Car()
car2 = Car()

car1.color = "yellow"
car2.color = "black"

print(car1.description())
print(car2.description())