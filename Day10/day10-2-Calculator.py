from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

def calculator():
    print(logo)

    
    should_continue = True
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
            print(symbol)

    while should_continue:
        
        operation_symbol = input("Pick an operation from the line aboive: ")
        num2 = int(input("What's the first number?: "))

        ope = operations[operation_symbol]
        answer = ope(num1, num2) #값에 따라 함수가 change

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
