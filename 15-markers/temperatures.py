Days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday", "Sunday"]
Readings = [[0.0 for x in range(3)] for y in range (7)]
AverageTemp = [0.0] * 7
numDays = len(Days)
numReadingsPerDay = len(Readings[0])
index = 0
index2 = 0
reading = 0.0

def getValues(): # get the temperatures
    global index, index2, reading
    index = 0
    while index < numDays:
        index2 = 0
        while index2 < numReadingsPerDay:
            reading = float(input("Enter the temperature reading for hour " + str(index2 + 1) + " on day " + str(index + 1) + ": "))
            while reading < -20 or reading > 50:
                print("Incorrectly entered reading. Please try again.")
                reading = float(input("Enter the temperature reading for hour " + str(index2 + 1) + " on day " + str(index + 1) + ": "))
            Readings[index][index2] = reading
            index2 = index2 + 1
        index = index + 1

getValues()
print(Readings)
