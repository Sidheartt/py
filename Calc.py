#from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calc():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    conti = True

    while conti:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: ") == 'yes':
            num1 = answer
        else:
            conti = False
            clear()
            calc()


calc()
