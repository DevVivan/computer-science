Guests = [""] * 5
Bookings = [[0.00 for i in range (4)] for i in range(5)]
RoomType = ["Single", "Double", "Suite"]
Price = [50.00, 80.00, 120.00]
name = ""
nights = 0
length = len(Bookings)
row = 0
length2 = len(Bookings[row])

while row < length:
    col = 0
    name = input("Enter guest " + str(row + 1) + "'s name: ")
    Guests[row] = name
    while col < length2:
        col = col + 1
        nights = int(input("Enter the number of nights you will stay, " + Guests[row] + ": "))
        while nights < 1 or nights > 30:
            print("Incorrectly entered number of nights, it must be between 1-30. Please try again.")
            nights = int(input("Enter the number of nights you will stay, " + Guests[row] + ": "))
    row = row + 1

print(Guests)