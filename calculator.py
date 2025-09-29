def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
def main():
    print("simple calculator")
    
    
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    operation=input("Enter operation(+,-,*,/):")
    if operation=='+':
        print(add(num1,num2))
    elif operation=='-':
        print(subtract(num1,num2))
    elif operation=='*':
        print(multiply(num1,num2))
    elif operation=='/':
        print(divide(num1,num2))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
