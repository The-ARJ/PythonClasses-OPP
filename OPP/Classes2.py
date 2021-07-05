# creating class by using function(method)
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def myintro(self):  # This is method
        print("My name is ", self.name, "age", self.age,
              "and my height is ", self.height)


p1 = Person("Aayush Raj Joshi", 21, "5.4 inch")
p1.myintro()
