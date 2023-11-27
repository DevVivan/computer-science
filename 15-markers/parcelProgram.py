minWeight = 1
maxWeight = 10
maxDimension = 80
sumDimensions = 200
accepted = True

def getWeight():
    global weight
    weight = int(input("Enter the weight of the parcel: "))

def getDimensions():
    global height, length, breadth
    height = int(input("Enter the height of the parcel: "))
    length = int(input("Enter the length of the parcel: "))
    breadth = int(input("Enter the breadth of the parcel: "))

def calculateParcel(w, h, l, b):
    global accepted
    if (w >= minWeight and w <= maxWeight) and (h + l + b <= sumDimensions) and (h <= maxDimension) and (l <= maxDimension) and (b <= maxDimension):
        accepted = True
    else: 
        if (w > 10):
            print("-" * 100)
            print("The parcel's weight exceeds " + str(maxWeight) + " kg.")
            accepted = False
        if (w < 1):
            print("-" * 100)
            print("The parcel's weight is less than " + str(minWeight) + " kg.")
            accepted = False
        if (h + l + b > sumDimensions):
            print("-" * 100)
            print("The sum of the dimensions of the parcel exceeds " + str(sumDimensions) + " cm.")
            accepted = False
        if (h > maxDimension):
            print("-" * 100)
            print("The height of the parcel exceeds " + str(maxDimension) + " cm.")
            accepted = False
        if (l > maxDimension):
            print("-" * 100)
            print("The length of the parcel exceeds " + str(maxDimension) + " cm.")
            accepted = False
        if (b > maxDimension):
            print("-" * 100)
            print("The breadth of the parcel exceeds " + str(maxDimension) + " cm.")
            accepted = False

def output():
    global totalParcels, acceptedParcels, rejectedParcels, count, acceptedWeight, price, sumPrise
    price = 0
    sumPrice = 0
    count = 0
    totalParcels = 0
    acceptedParcels = 0
    rejectedParcels = 0
    acceptedWeight = 0
    print("-" * 100)
    totalParcels = int(input("Enter the number of parcels you want to add to the consignment: "))
    print("-" * 100)
    while count < totalParcels:
        getWeight()
        getDimensions()
        calculateParcel(weight, height, length, breadth)
        if accepted == False:
            print("-" * 100)
            print("The parcel has not been accepted. Please try again.")
            print("-" * 100)
            getWeight()
            getDimensions()
            calculateParcel(weight, height, length, breadth)
            print("-" * 100)
            rejectedParcels += 1
        else:
            acceptedWeight = acceptedWeight + weight
            acceptedParcels += 1
            totalParcels = acceptedParcels + rejectedParcels
            if weight >= 1 and weight <= 5:
                price = 10
                sumPrice = sumPrice + 10
            if weight > 5 and weight <= 10:
                price = 10 + (weight - 5) * 10 * 0.1
                sumPrice = sumPrice + (10 + (weight - 5) * 10 * 0.1)
            print("-" * 100)
            print("The parcel has been accepted.")
            print("The price of the parcel is $" + str(price) + ".")
            print("-" * 100)
        count = count + 1
    print("There are " + str(totalParcels) + " total parcels in your consignment.")
    print(str(acceptedParcels) + " parcels were accepted. The total weight of these accepted parcels is " + str(acceptedWeight) + " kg." )
    print(str(rejectedParcels) + " parcels were rejected.")
    print("The total price of the parcels was $" + str(sumPrice) + ".")
output()
