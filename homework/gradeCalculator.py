mark = 0
grade = ""

def getMark():
    global mark
    global grade
    mark = int(input("Enter your mark: "))

def calculateGrade(m):
    if m >= 90 and m <= 100:
        return "A"
    elif m >= 80 and m < 90:
        return "B"
    elif m >= 70 and m < 80:
        return "C"
    elif m >= 60 and m < 70:
        return "D"
    else:
        return "F"
    
def output():
    getMark()
    grade = calculateGrade(mark)
    print("The equivalent grade is " + grade)

output()