"""Creating Class Normally"""


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


p1 = Person("Aayush Raj Joshi", 21, "5.4 inch")
print(p1.name)
print(p1.age)
print(p1.height)
