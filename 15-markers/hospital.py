Patient = ["Bob","Jill","Ben","Grace"]
Readings = [[35.60,56.00],[31.50,55.00],[32.60,101.00],[54.00, 101.00]]
newPatient = ""
tempRate = 0.0
pulseRate = 0
counter = 0
length = len(Patient)

def getValues():
    global counter, hospitalNumber
    while counter < length:
        hospitalNumber = int(input("Enter the patient's hospital number: "))
        if hospitalNumber < 1 or hospitalNumber > 1000:
            print("The hospital number is invalid. It must be between 1 and 1000.")
            break
        else:
            print("The patient is " + Patient[hospitalNumber - 1])
        counter = counter + 1

getValues()