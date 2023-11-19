initialValue = 0
initialUnit = ""
finalValue = 0
finalUnit = ""

def getInitial():
    global initialValue
    global initialUnit
    global finalUnit
    initialValue = int(input("Enter your initial temperature value: "))
    initialUnit = input("Enter your initial unit (c for Celsius, f for Fahrenheit): ")
    finalUnit = input("Enter your desired final unit (c for Celsius, f for Fahrenheit): ")

def calculateFinal(i, f, n):
    if i.lower() == "c" and f.lower() == "f":
        return str(n * 9/5 + 32) + " Fahrenheit"
    elif i.lower() == "f" and f.lower() == "c":
        return str((n - 32) * 5/9) + " Celsius"
    
def output():
    getInitial()
    print("The converted value is " + calculateFinal(initialUnit, finalUnit, initialValue))

output()

