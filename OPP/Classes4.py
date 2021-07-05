"""Multiplication in class by method"""


class Multi:
    def __init__(self, a):
        self.a = a

    def mul(self):
        i = 1
        while i <= 10:
            total = self.a * i
            print(self.a, "x", i, "=", total)
            i = i + 1


m1 = Multi(int(input("Enter a number : ")))

m1.mul()
