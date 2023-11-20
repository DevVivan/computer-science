choice = 0
squareLength = 0
rectangleHeight = 0
rectangleWidth = 0
circleRadius = 0
area = 0
pi = 3.14

def areaSquare(n):
    return n * n

def areaRectangle(a, b):
    return a * b

def areaCircle(x):
    return x * x * pi

def menu():
    global choice, squareLength, rectangleHeight, rectangleWidth, circleRadius, area
    while choice != 4:
        print("Press 1 for calculating area of a square")
        print("Press 2 for calculating area of a rectangle")
        print("Press 3 for calculating area of a circle")
        print("Press 4 to exit the program")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            squareLength = int(input("Enter the side length of the square: "))
            area = areaSquare(squareLength)
            print("The area of the square is " + area)
        elif choice == 2:
            rectangleHeight = int(input("Enter the height of the rectangle: "))
            rectangleWidth = int(input("Enter the width of the rectangle: "))
            area = areaRectangle(rectangleWidth, rectangleHeight)
            print("The area of the rectangle is " + area)
        elif choice == 3:
            circleRadius = int(input("Enter the radius of the circle: "))
            area = areaCircle(circleRadius)
            print("The area of the circle is " + area)
        elif choice == 4:
            break
        else: 
            print("Invalid choice. Please try again.")
            choice = int(input("Enter your choice: "))

menu()