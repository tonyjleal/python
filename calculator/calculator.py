import sys

class Calculator:

    def __init__(self):
        self.value = 0

    def add(self, x, y):
        self.value = x + y

    def substract(self, x, y):
        self.value = x - y

    def multiply(self, x, y):
        self.value = x * y

    def divide(self, x, y):
        try:
            self.value = x / y
        except ZeroDivisionError:
            print("You can't divide by zero!")
