from email.policy import default
from art import logo
import os



# def addition(first,next):
#     total = first + next
#     return total

# def subtraction(first,next):
#     total = first - next
#     return f"{first} - {next} = {total}"

# def multiplication(first,next):
#     total = first * next
#     return f"{first} * {next} = {total}"

# def division(first,next):
#     total = first / next
#     return f"{first} / {next} = {total}"

# def getting_inputs():
#     first_number = int(input("What is your first number?: "))
#     print("+")
#     print("-")
#     print("*")
#     print("/")
#     return first_number
    

# first_number = getting_inputs()
# should_continue = True
# result = first_number

# while should_continue:
#     operation = input("Pick an operation: ")
#     next_number = int(input("What is the next number?: "))
#     first_number = result
#     if operation == "+":
#         result = addition(first_number,next_number)
#     elif operation == "-":    
#         result = subtraction(first_number,next_number)
#     elif operation == "*":
#         result = multiplication(first_number,next_number)
#     elif operation == "/":
#         result = division(first_number,next_number)
#     else:
#         print(f"Invalid operation.")
    
#     print(f"{first_number} {operation} {next_number} = {result}") 
#     continue_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
#     if continue_again == "n":
#         should_continue = False
#         os.system('clear')
#         getting_inputs()


def addition(first,next):
    return first + next

def subtraction(first,next):
    return first - next
 
def multiplication(first,next):
    return first * next

def division(first,next):
    return first / next

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

# ask_first_number = True:
def calculator():
    print(logo)
    first_number = float(input("What is your first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What is the next number?: "))

        calculation = operations[operation_symbol]
        
        result = calculation(first_number,next_number)
        print(f"{first_number} {operation_symbol} {next_number} = {result}")
        continue_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ").lower()
        if continue_again == "n":
            should_continue = False
            os.system('clear')
            calculator()
        elif continue_again == "y":
            first_number = result   
        else:
            print(f"Good bye!!")
            should_continue = False
            exit 
        
calculator()
    