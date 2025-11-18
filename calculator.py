def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    if b==0:
        return "error:division by zero is not allowed."
    return a/b

def multiply(a,b):
    return a*b


def main():
    print("simple calculator")
    while True:
        operator=input("Enter operator")
        if operator.lower()=="exit":
            print("exiting calculator.goodbye")
            break

        try:
            num1=int(input("Enter first number:"))
            num2=int(input("Enter second number:"))
        except valueError:
            print("invalid input:please enter numeric values.")
            continue
        if operator=="+":
                print(add(num1,num2))
        elif operator=="-":
                print(subtract(num1,num2))
        elif operator=="*":
                print(multiply(num1,num2))
        elif operator=="/":
                print(divide(num1,num2))
        else:
                print("invalid operator")

if __name__=="__main__":
    main()
