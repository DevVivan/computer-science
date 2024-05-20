Students = ["", "Alice", "Bob", "Charlie"]  
Scores = [[0, 0], [85, 90], [102, 95], [75, 105]]
index = 0

def procedure(id):
    while id < 1 or id > 300:
        print("The id is incorrectly entered, it has to be between 1 and 300. Please try again.")
        break
    index = id - 1
    print(Students[index])
    rows = 0
    if (Scores[index][0] >= 1 and Scores[index][0] <= 100) and (Scores[index][1] >= 1 and Scores[index][1] <= 100):
        print("All scores within range.")
    elif (Scores[index][0] >= 1 and Scores[index][0] <= 100) and not (Scores[index][1] >= 1 and Scores[index][1] <= 100):
        print("Science score out of range.")
    elif not (Scores[index][0] >= 1 and Scores[index][0] <= 100) and (Scores[index][1] >= 1 and Scores[index][1] <= 100):
        print("Math score out of range.")
    elif not (Scores[index][0] >= 1 and Scores[index][0] <= 100) and not (Scores[index][1] >= 1 and Scores[index][1] <= 100):
        print("Both scores out of range.")

procedure(1)
