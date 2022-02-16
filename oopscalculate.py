class Calculator:
    def __init__(self,number):
        self.number=number

    def square(self):
        print(f"The square of the number {self.number} is {self.number ** 2}")

    def squareroot(self):
        print(f"The squareroot of the number {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The cube of the number {self.number} is {self.number **3}")

c=Calculator(2)
c.square()
c.squareroot()
c.cube()
