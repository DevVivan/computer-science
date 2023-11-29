import random 

name = "" 
mode = 0 
table = 0 
score = 0 
count = 1 
times = 0 
userAnswer = 0 
attempts = 0

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
    print(str(name) + ", your score is " + str(score) + " .")
    if score == 5: 
        print("Well done, you got full marks.") 
    elif score == 4: 
        print("Good, you almost got full marks.") 
    elif score == 3: 
        print("You did alright, practice more.")	 
    elif score <= 2: 
        print("You didn't do very well. Practice is needed.")	 

def learning(y): 
    global userAnswer, score, count, times, userAnswer, attempts
    while count <= 5:
        times = random.randint(1, 12) 
        while attempts <= 3 and userAnswer != y * times:
            print("Question " + str(count)) 
            userAnswer = int(input(str(y) + " x " + str(times) + " = "))
            count = count + 1
            if userAnswer == y * times:
                print("Well done, your answer is correct, " + name)
            elif userAnswer > y * times:
                print("Your answer is too big, " + name + " . Please try again")
            elif userAnswer < y * times:
                print("Your answer is too small, " + name + " . Please try again")
            if attempts == 3:
                print("You didn't get the correct answer. The correct answer is " + str(y * times))
        attempts = attempts + 1

def getMode():
    global mode, table
    getName()
    while True:
        print("[1] Testing") 
        print("[2] Learning") 
        print("[3] Exit")
        mode = int(input("Enter your mode (1 for testing, 2 for learning, 3 to exit): ")) 
        table = int(input("Enter the times table you want to practice (Between 2 & 12): ")) 
        if mode == 1: 
            testing(table) 
        elif mode == 2: 
            learning(table) 
        elif mode == 3:
            break
        else: 
            print("Not a valid mode. Please try again.") 

getMode()