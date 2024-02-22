bookings = [["X", "X", "X", "X", "B"],
            ["B", "X", "B", "X", "X"],
            ["X", "X", "X", "B", "X"],
            ["X", "B", "B", "X", "X"]]
count = 0


def getSeat():
    global row, seat
    row = int(input("Which row: ")) - 1
    while row < 0 or row > 3:
        print("Incorrectly entered row. It should be between 1 and 4. Please try again. ")
        row = int(input("Which row: ")) - 1
    seat = int(input("Which seat: ")) - 1
    while seat < 0 or row > 4:
        print("Incorrectly entered seat. It should be between 1 and 5. Please try again. ")
        seat = int(input("Which seat: ")) - 1

def handleProgram():
    global count
    seats = int(input("Enter how many seats would you like to book: "))
    while count < seats:
        getSeat()
        while bookings[row][seat] == "B":
            print("This seat is already booked. Please try booking another seat. ")
            getSeat()
        bookings[row][seat] = "B"
        print("Booking confirmed. ")
        count = count + 1

def printNewSeats():
    for r in bookings:
        for c in r:
            print(c, end=" ")
        print()

printNewSeats()
handleProgram()
printNewSeats()
