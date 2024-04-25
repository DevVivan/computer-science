students = []
index = 0
max = 5

def addName():
    global index, name
    index = 0
    while index < 5:
        name = input("Enter the name of the student: ")
        students[index] = name
        index = index + 1
    print("The class is full.")

addName()

def search():
    

# def menu():
#     print("MENU")
#     print("1. Add Student.")
#     print("2. Search for Student.")
#     print("3. Sort Names.")
#     print("4. Close Program.")

# menu()
# option = int(input("Enter the menu option: "))

# while option != 0:
#     if option == 1: