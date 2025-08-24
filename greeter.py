from math_utils import add

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        total = add(len(self.name), 10)
        return f"Hello, {self.name}! Your magic number is {total}."
