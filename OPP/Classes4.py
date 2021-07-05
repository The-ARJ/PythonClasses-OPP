"""Multiplication in class"""


class Multi:
    def __init__(self, a):
        self.a = a
        i = 1
        n = 10
        while i <= 10:
            total = a * i
            print(a, "x", i, "=", total)
            i = i + 1


m1 = Multi(int(input("Enter a number : ")))
