"""Addition in Class"""


class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b


s1 = Sum(int(input("enter value for a: ")), int(input("enter value for b: ")))

print("The sum is ", s1.a + s1.b)
