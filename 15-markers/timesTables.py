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
		userAnswer = input(str(x) + " x " + str(times) + " =") 
		if  userAnswer == x * times: 
            score = score + 1			 
        count = count + 1 
    print(str(name) + " your score is " + str(score))
	if score == 5: 
        print("Well done, you got full marks.") 
    elif score == 4: 
        print("Good, you almost got full marks.") 
    elif score == 3: 
        print("You did alright, practice more.")	 
    elif score <= 2: 
        print("You didn't do very well. Practice is needed.")	 

def learning(y): 
	print("hi") 

def getMode(): 
	global mode, table 
	while True: 
		print("[1] Testing") 
		print("[2] Learning") 
        print("[3] Exit")
        mode = int(input("Enter your mode (1 for testing, 2 for learning): ")) 
        table = int(input("Enter the times table you want to practice (Between 2 & 12)")) 
        if mode == 1: 
            testing(table) 
        elif mode == 2: 
            Learning(table) 
        elif mode == 3:
            break
        else: 
            Print("Not a valid mode. Please try again.") 