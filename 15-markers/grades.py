StudentName = ["Ben","Grace", "Holly","Bob"]
SubjectMark = [[34,12,56,78],[55,87,88,91],[23,23,23,23], [40,45,50,55]]
ClassSize = len(StudentName)
SubjectNo = len(SubjectMark[0])
totalMarks = 0
markAverage = 0
index = 0

def outputName():
    global index
    print(StudentName[index])

def handleProgram():
    global index, totalDistinctions, totalMerits, totalPasses, totalFails
    index2 = 0
    while index < ClassSize:
        print("-" * 50)
        outputName()
        totalMarks = 0
        index2 = 0
        while index2 < SubjectNo:
            totalMarks = totalMarks + SubjectMark[index][index2]
            index2 = index2 + 1
        print("The total mark for this student is " + str(totalMarks))
        print("The average mark for this student is " + str(round(totalMarks/SubjectNo)))
        if (totalMarks/SubjectNo) >= 70:
            print("This student got a distinction.")
            totalDistinctions = totalDistinctions + 1
        elif (totalMarks/SubjectNo) >= 55 and (totalMarks/SubjectNo) < 70:
            print("This student got a merit.")
            totalMerits = totalMerits + 1
        elif (totalMarks/SubjectNo) >= 40 and (totalMarks/SubjectNo) < 55:
            print("This student got a pass.")
            totalPasses = totalPasses + 1
        elif (totalMarks/SubjectNo) < 40:
            print("This student got a fail.")
            totalFails = totalFails + 1
        index = index + 1   

handleProgram()
    