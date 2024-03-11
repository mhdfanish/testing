def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

num1 = int(input("Enter The First Number: "))
num2 = int(input("Enter The Second Number: "))

print("Which operation would you like to perform?")
operator = input("Enter any these operator +,-,*,/ : ")

result = 0
if operator == '+':
    operation = 'Addition'
    print(f"The {operation} of {num1} and {num2} is {add(num1, num2)}.")
elif operator == '-':
    operation = 'Subtraction'
    print(f"The {operation} of {num1} and {num2} is {subtract(num1, num2)}.")
elif operator == '*':
    operation = 'Multiplication'
    print(f"The {operation} of {num1} and {num2} is {mult(num1, num2)}.")
elif operator == '/':
    operation = 'Division'
    print(f"The {operation} of {num1} and {num2} is {div(num1, num2)}.")
else:
    print("Invalid input operator character!")
