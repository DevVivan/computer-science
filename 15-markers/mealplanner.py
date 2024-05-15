mealSchedule = [["" for i in range(3)]for y in range(3)]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
breakfast = ""  
lunch = ""
dinner = ""
row = 0
meals = ["Breakfast", "Lunch", "Dinner"]

while row < len(mealSchedule):
    col = 0
    while col < len(mealSchedule[row]):
        meal = input("Enter meal " + str(col + 1) + " for day " + str(row + 1) + ": ")
        mealSchedule[row][col] = meal
        col = col + 1
    row = row + 1

def display():
    row = 0
    while row < len(mealSchedule):
        col = 0
        print(days[row])
        while col < len(mealSchedule[row]):
            print(meals[col] + ": " + mealSchedule[row][col])
            col = col + 1
        row = row + 1

display()

mealSchedule[4][2] = "BBQ"

display()
