EmployeeName = ["John", "Jane", "Alice", "Bob", "Eve"] 
EmployeeScore = [[90, 85, 88],    
                [75, 70, 78],      
                [60, 65, 58],      
                [40, 45, 50],      
                [30, 35, 28]] 
DepartmentSize = 5
ProjectNo = 3
total = 0
average = 0
count = 0
goodEmployees = 0
excellentEmployees = 0
satifactoryEmployees = 0
improvementEmployees = 0

row = 0
while row < DepartmentSize:
    print(EmployeeName[row])
    col = 0
    while col < ProjectNo:
        total = total + EmployeeScore[row][col]
        col= col + 1
    average = total / ProjectNo
    print("The total is " + str(total))
    print("The average score is " + str(round(average)))
    if average >= 85:
        print("This employee's performance rating is excellent.")
        excellentEmployees = excellentEmployees + 1
    elif average >= 75 and average < 85:
        print("This employee's performance rating is good.")
        goodEmployees = goodEmployees + 1
    elif average >= 50 and average < 75:
        print("This employee's performance rating is satisfactory.")
        satifactoryEmployees = satifactoryEmployees + 1
    elif average < 50:
        print("This employee's performance rating needs improvement.")
        improvementEmployees = improvementEmployees + 1
    average = 0
    total = 0
    row = row + 1

print("There were " + str(excellentEmployees) + " employees whose performance rating was excellent.")
print("There were " + str(goodEmployees) + " employees whose performance rating was good.")
print("There were " + str(satifactoryEmployees) + " employees whose performance rating was satisfactory.")
print("There were " + str(improvementEmployees) + " employees whose performance rating needs improvement.")