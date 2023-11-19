userInt = 0
count = 1

def getNumber():
    global userInt
    userInt = int(input("Enter the number: "))

def calculateTable(n):
    global count
    while count < 11:
        print(str(n * count))
        count = count + 1

def output():
    getNumber()
    calculateTable(userInt)

output()
