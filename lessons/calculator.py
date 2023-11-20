num1 = 0
num2 = 0
choice = 1
answer = 0

def getNum1():
    global num1
    num1 = int(input("Enter number 1: "))

def getNum2():
    global num2
    num2 = int(input("Enter number 2: "))

def add(a, b):
    return a + b

def subtract(a, b):
    return b - a

def multiply(a, b):
    return a * b

def divide(a, b):
    return b / a

def menu():
    getNum1()
    getNum2()
    global choice
    global answer
    while choice != 5:
        print("Press 1 to add")
        print("Press 2 to subtract")
        print("Press 3 to divide")
        print("Press 4 to multiply")
        print("Press 5 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            answer = add(num1, num2)
            print("The answer is " + str(answer))
        elif choice == 2:
            answer = subtract(num1, num2)
            print("The answer is " + str(answer))
        elif choice == 3:
            answer = divide(num1, num2)
            print("The answer is " + str(answer))
        elif choice == 4:
            answer = multiply(num1, num2)
            print("The answer is " + str(answer))
        elif choice == 5:
            break
        else:
            print("Incorrect choice. Please try again.")
            choice = int(input("Enter your choice: "))
    
menu()