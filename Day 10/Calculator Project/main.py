from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Divide by Zero error"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

keep_result = "n"
result = 0
calculating = True
while calculating:
    if keep_result == "y":
        user_input_1 = result
    else:
        user_input_1 = float(input("Please enter the first number: "))

    user_input_2 = float(input("Please enter the second number: "))
    for symbol in operations:
        print(symbol)
    user_operator = input("Please select enter an operator: ")

    result = operations[user_operator](user_input_1, user_input_2)
    print(f"{user_input_1} {user_operator} {user_input_2} = {result}")

    keep_result = input(f"\nType 'y' to continue with previous result {result}. Type 'n' to start over: ").lower()

