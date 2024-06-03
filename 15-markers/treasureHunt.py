import random
map = [[0 for x in range(12)] for y in range(12)] 
guessedRow = 0
guessedCol = 0
squaresAway = 0
counter = 0
option = 0

def game():
    global counter, guessedCol, guessedRow, randomRow, randomCol, squaresAway
    randomRow = random.randint(0,12)
    randomCol = random.randint(0,12)    
    map[randomRow][randomCol] = 1
    print("The treasure is hidden in a random square on the map.")
    while counter < 5:
        guessedRow = int(input("Enter the row where you think the treasure is located in: "))
        guessedCol = int(input("Enter the column where you think the treasure is located in: "))
        if guessedCol == randomCol and guessedRow == randomRow:
            print("Your guess was correct!")
            break
        elif guessedRow >= randomRow and guessedCol >= randomCol:
            squaresAway = (guessedRow - randomRow) + (guessedCol - randomCol)
            print("Incorrect guess. The treasure is " + str(squaresAway) + " squares away.")
        elif guessedRow <= randomRow and guessedCol <= randomCol:
            squaresAway = (randomCol - guessedCol) + (randomRow - guessedRow)
            print("Incorrect guess. The treasure is " + str(squaresAway) + " squares away.")
        elif guessedRow >= randomRow and guessedCol <= randomCol:
            squaresAway = (guessedRow - randomRow) + (randomRow - guessedCol)
            print("Incorrect guess. The treasure is " + str(squaresAway) + " squares away.")
        elif guessedRow <= randomRow and guessedCol >= randomCol:
            squaresAway = (randomRow - guessedCol) + (guessedCol - randomCol)
            print("Incorrect guess. The treasure is " + str(squaresAway) + " squares away.")
        counter = counter + 1

def menu():
    global option
    print("1. Play Game.")
    print("2. Quit")
    option = int(input("Enter the option you would like: "))

while True:
    menu()
    if option == 1:
        game()
    option = int(input("Enter the option you would like: "))