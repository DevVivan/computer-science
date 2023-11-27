import random 

name = "" 
mode = 0 
table = 0 
score = 0 
count = 1 
times = 0 
userAnswer = 0 

def getName(): 
    global name 
    name = input("Enter your name: ") 

def testing(x): 
    global score, count, times, userAnswer 
    while count <= 5: 
        times = random.randint(1, 12) 
        print("Question " + str(count)) 
        userAnswer = int(input(str(x) + " x " + str(times) + " = "))
        if userAnswer == x * times: 
            score = score + 1			 
        count = count + 1 
    print(str(name) + ", your score is " + str(score))
    if score == 5: 
        print("Well done, you got full marks.") 
    elif score == 4: 
        print("Good, you almost got full marks.") 
    elif score == 3: 
        print("You did alright, practice more.")	 
    elif score <= 2: 
        print("You didn't do very well. Practice is needed.")	 

def learning(y): 
    global count
    while count <= 5: 
        times = random.randint(1, 12) 
        print("Question " + str(count)) 
        userAnswer = int(input(str(y) + " x " + str(times) + " = "))
        if userAnswer == y * times: 
            print(str(name) + ", your answer is correct!")		
        if userAnswer != y * times:
            if userAnswer > y * times:
                print("This is incorrect, " + str(name) + ". Your answer is too large.") 
            elif userAnswer > y * times:
                print("This is incorrect, " + str(name) + ". Your answer is too small.") 
            else:
                print("This is not a valid answer. Try again.")
    count = count + 1 

def runProgram(): 
    global mode, table 
    getName()
    while True: 
        print("*" * 100)
        print("[1] Testing") 
        print("[2] Learning") 
        print("[3] Exit")
        print("*" * 100)
        mode = int(input("Enter your mode (1 for testing, 2 for learning, 3 to exit): ")) 
        table = int(input("Enter the times table you want to practice (Between 2 & 12): ")) 
        if mode == 1: 
            if table < 2 or table > 12:
                print("Invalid times table. It needs to be between 2 & 12. Try again.")
            else:
                testing(table) 
        elif mode == 2: 
            if table < 2 and table > 12:
                print("Invalid times table. It needs to be between 2 & 12. Try again.")
            else:
                learning(table) 
        elif mode == 3:
            break
        else: 
            print("Not a valid mode. Please try again.") 
        
runProgram()