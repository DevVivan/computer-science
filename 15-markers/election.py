Candidates = [""] * 4
candidate1 = 0 
candidate2= 0 
candidate3 = 0 
candidate4 = 0 
abstained = 0
name = ""
index = 0
votes = []
choice = 0

def enterCandidates():
    global index, choice, name
    while index < len(Candidates):
        name = input("Enter the name of candidate " + str(index + 1) + ": ")
        while len(name) == 0:
            print("No name has been entered. Please try again.")
            name = input("Enter the name of candidate " + str(index + 1) + ": ")
        Candidates[index] = name
        index = index + 1

def voting():
    global candidate1, candidate2, candidate3, candidate4, abstained
    index = 0
    print("Candidates:")
    print("1. " + str(Candidates[0]))
    print("2. " + str(Candidates[1]))
    print("3. " + str(Candidates[2]))
    print("4. " + str(Candidates[3]))
    print("5. Abstain")
    while index < 3:
        choice = int(input("Enter the student's choice: "))
        while choice > 5 or choice < 1:
            print("Incorrectly entered choice. Please try again.")
            choice = int(input("Enter the student's choice: "))
        if choice == 1:
            candidate1 = candidate1 + 1
        elif choice == 2:
            candidate2 = candidate2 + 1
        elif choice == 3:
            candidate3 = candidate3 + 1
        elif choice == 4:
            candidate4 = candidate4 + 1
        else:
            abstained = abstained + 1
        index = index + 1

def displayWinner():
    global index, votes
    if candidate1 == candidate2 == candidate3 == candidate4:
        print("All candidates got equal votes and recieved " + str(candidate1) + " votes.")
    elif candidate1 == candidate2 == candidate3:
        print("Candidates 1, 2, 3 all got equal votes and recieved " + str(candidate1) + " votes.")
    elif candidate2 == candidate3 == candidate4:
        print("Candidates 2, 3, 4 all got equal votes and recieved " + str(candidate2) + " votes.")
    elif candidate1 == candidate3 == candidate4:
        print("Candidates 1, 3, 4 all got equal votes and recieved " + str(candidate1) + " votes.")
    elif candidate1 == candidate2 == candidate4:
        print("Candidates 1, 2, 4 all got equal votes and recieved " + str(candidate1) + " votes.")
    elif candidate1 == candidate2:
        print("Candidates 1 & 2 got equal votes and recieved " + str(candidate1) + " votes.")
    elif candidate2 == candidate3:
        print("Candidates 2 & 3 got equal votes and recieved " + str(candidate2) + " votes.")
    elif candidate3 == candidate4:
        print("Candidates 3 & 4 got equal votes and recieved " + str(candidate3) + " votes.")
    elif candidate1 == candidate3:
        print("Candidates 1 & 3 got equal votes and recieved " + str(candidate3) + " votes.")
    elif candidate1 == candidate4:
        print("Candidates 1 & 4 got equal votes and recieved " + str(candidate4) + " votes.")
    elif candidate2 == candidate4:
        print("Candidates 2 & 4 got equal votes and recieved " + str(candidate2) + " votes.")

    votes = [candidate1, candidate2, candidate3, candidate4]
    for i in range(len(votes)):
        for j in range(0, len(votes) - i -1):
            if votes[j] > votes[j+1]:
                votes[j], votes[j+1] = votes[j+1], votes[j]
            
    print("The winner was candidate number " + str(Candidates[len-1]))
 
enterCandidates()
voting()
displayWinner()

