class InlineCalculator:
    def __init__(self):
        self.userInput = None
        self.stack = None
        self.operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "x": lambda x, y: x * y,
                          "*": lambda x, y: x * y, "/": lambda x, y: x / y, "^": lambda x, y: x ** y}
        self.run = False
        self.prefix = None
        self.postfix = None
        self.result = None

    def __putOnStack(self):
        print("Your formula:")
        self.userInput = input()
        self.stack = self.userInput.split(" ")
        if self.stack[-1] in self.operators.keys():
            self.postfix = self.stack[:]
            self.prefix = self.stack[::-1]
            self.run = 1
        elif self.stack[0] in self.operators.keys():
            self.postfix = self.stack[::-1]
            self.prefix = self.stack[:]
            self.stack.reverse()
            self.run = 1
        else:
            print("Wrong input")

    def getResult(self):
        result = []
        while len(self.stack) > 0:
            value = self.stack.pop(0)
            if value.isdigit():
                result.append(float(value))
            elif value in self.operators.keys():
                try:
                    result.append(self.operators[value](result.pop(-2), result.pop(-1)))
                except:
                    print("Invalid operation")
                    self.run = 0
                    return 0
            else:
                print(f"Insufficient input {value}")
                self.run = 0
                return 0
        self.result = result[0]

    def display(self):
        print(f"postfix: {' '.join(self.postfix)}")
        print(f"prefix: {' '.join(self.prefix)}")
        if self.result is not None:
            print(f"Result: {self.result}")

    def resetResult(self):
        self.prefix = None
        self.postfix = None
        self.result = None
        self.stack = None
        self.userInput = None

    def calculate(self):
        while True:
            self.__putOnStack()
            if not self.run:
                break
            self.getResult()
            if not self.run:
                break
            self.display()
            self.resetResult()


if __name__ == '__main__':
    calculator = InlineCalculator()
    calculator.calculate()
