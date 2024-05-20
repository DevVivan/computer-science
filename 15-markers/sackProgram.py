sandSacks = 0
gravelSacks = 0
cementSacks = 0
count = 0
rejectedSacks = 0
sumWeight = 0.0
weight = 0.0
maxWeightSandGravel = 50.1
minWeightSandGravel = 49.9
maxWeightCement = 25.1
minWeightCement = 24.9

# cementSacks = int(input("How many cement sacks do you want to enter: "))
# sandSacks = int(input("How many sand sacks do you want to enter: "))
# gravelSacks = int(input("How many gravel sacks do you want to enter: "))

# while count != cementSacks:
#     weight = float(input("Enter the weight of your cement sack (More than 24.9 kg & Less than 25.1 kg): "))
#     if weight <= minWeightCement:
#         print("The cement sack is underweight. It has to be more than " + str(minWeightCement) + " kg. Please try again.")
#         rejectedSacks = rejectedSacks + 1
#     elif weight >= maxWeightCement:
#         print("The cement sack is overweight. It has to be less than " + str(maxWeightCement) + " kg. Please try again.")
#         rejectedSacks = rejectedSacks + 1
#     else:
#         print("The cement sack has been accepted. It contains cement and it's weight is " + str(weight) + " kg.")
#         sumWeight = sumWeight + weight
#         count = count + 1

# count = 0

# while count != gravelSacks:
#     weight = float(input("Enter the weight of your gravel sack (More than 49.9 kg & Less than 50.1 kg): "))
#     if weight <= minWeightSandGravel:
#         print("The gravel sack is underweight. It has to be more than " + str(minWeightSandGravel) + " kg. Please try again.")
#         rejectedSacks = rejectedSacks + 1
#     elif weight >= maxWeightSandGravel:
#         print("The gravel sack is overweight. It has to be less than " + str(maxWeightSandGravel) + " kg. Please try again.")
#         rejectedSacks = rejectedSacks + 1
#     else:
#         print("The gravel sack has been accepted. It contains gravel and it's weight is " + str(weight) + " kg.")
#         sumWeight = sumWeight + weight
#         count = count + 1

# count = 0

# while count != sandSacks:
#     weight = float(input("Enter the weight of your sand sack (More than 49.9 kg & Less than 50.1 kg): "))
#     if weight <= minWeightSandGravel:
#         print("The sand sack is underweight. It has to be more than " + str(minWeightSandGravel) + " kg. Please try again.")
#         rejectedSacks = rejectedSacks + 1
#     elif weight >= maxWeightSandGravel:
#         print("The sand sack is overweight. It has to be less than " + str(maxWeightSandGravel) + " kg. Please try again.")
#         rejectedSacks = rejectedSacks + 1
#     else:
#         print("The sand sack has been accepted. It contains sand and it's weight is " + str(weight) + " kg.")
#         sumWeight = sumWeight + weight
#         count = count + 1


weight = float(input("Enter the weight of your cement sack (More than 24.9 kg & Less than 25.1 kg): "))
if weight <= minWeightCement:
    print("The cement sack is underweight. It has to be more than " + str(minWeightCement) + " kg. Please try again.")
    rejectedSacks = rejectedSacks + 1
elif weight >= maxWeightCement:
    print("The cement sack is overweight. It has to be less than " + str(maxWeightCement) + " kg. Please try again.")
    rejectedSacks = rejectedSacks + 1
else:
    print("The cement sack has been accepted. It contains cement and it's weight is " + str(weight) + " kg.")
    sumWeight = sumWeight + weight

weight = float(input("Enter the weight of your gravel sack (More than 49.9 kg & Less than 50.1 kg): "))
if weight <= minWeightSandGravel:
    print("The gravel sack is underweight. It has to be more than " + str(minWeightSandGravel) + " kg. Please try again.")
    rejectedSacks = rejectedSacks + 1
elif weight >= maxWeightSandGravel:
    print("The gravel sack is overweight. It has to be less than " + str(maxWeightSandGravel) + " kg. Please try again.")
    rejectedSacks = rejectedSacks + 1
else:
    print("The gravel sack has been accepted. It contains gravel and it's weight is " + str(weight) + " kg.")
    sumWeight = sumWeight + weight

weight = float(input("Enter the weight of your sand sack (More than 49.9 kg & Less than 50.1 kg): "))
if weight <= minWeightSandGravel:
    print("The sand sack is underweight. It has to be more than " + str(minWeightSandGravel) + " kg. Please try again.")
    rejectedSacks = rejectedSacks + 1
elif weight >= maxWeightSandGravel:
    print("The sand sack is overweight. It has to be less than " + str(maxWeightSandGravel) + " kg. Please try again.")
    rejectedSacks = rejectedSacks + 1
else:
    print("The sand sack has been accepted. It contains sand and it's weight is " + str(weight) + " kg.")
    sumWeight = sumWeight + weight
    
print("The total weight of your order is " + str(sumWeight) + " kg.")
print(str(rejectedSacks) + " of your sacks were rejected.")


