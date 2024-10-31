class Calculator:
    def __init__(self, n):
        square = n*n
        cube = square*n
        squareRoot = n/2

        print(f"Square is {square}, cube is {cube}, Square root is {squareRoot}")


a = Calculator(1000000000000000)