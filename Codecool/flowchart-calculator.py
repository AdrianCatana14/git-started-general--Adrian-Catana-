print("Start")

def addition(first_number, second_number):
    return first_number + second_number
def subtraction(first_number, second_number):
    return first_number - second_number
def multiplication(first_number, second_number):
    return first_number * second_number
def division(first_number, second_number):
    return first_number / second_number

while True:
    get_first_number = input("Enter first number: ")
    try:
        first_number = float(get_first_number)
        break
    except ValueError:
        print("Invalid input, try again")
        continue


valid_operators = ['+', '-', '*', '/']
while True:
    operation = input("Select operator: ")
    if operation in valid_operators:
        break
    else:
        print("Invalid input, try again")
        continue

while True:
    get_second_number = input("Enter second number: ")
    try:
        second_number = float(get_second_number)
        break
    except ValueError:
        print("Invalid input, try again")
        continue

if operation == '+':
    print(first_number, '+', second_number, '=', addition(first_number, second_number))
elif operation == '-':
    print(first_number, '-', second_number, '=', subtraction(first_number, second_number))
elif operation == '*':
    print(first_number, '*', second_number, '=', multiplication(first_number, second_number))
elif operation == '/':
    print(first_number, '/', second_number, '=', division(first_number, second_number))
elif operation == '/' and second_number == 0:
    print('Division by zero is not allowed')