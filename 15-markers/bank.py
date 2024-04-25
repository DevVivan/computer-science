Account = [["Ben","12345"],["Sarah","password"],["Glen","Glen123"]]
AccDetails = [[10050.50,300.00,300.000],[250.50,100.00,200.00],[10.50,500.00,1000.00]]
size = len(Account) #Size was mentioned in the question as we do not know the size of the array
id = 0
name = ""
password = ""

def getAccount():
    global id, name, password
    id = int(input("Enter your account id: "))
    while id > size or id < 0:
        print("Incorrectly entered account id. Please try again.")
        id = int(input("Enter your account id: "))
    name = input("Enter your account name: ")
    while name != Account[id][0]:
        print("That is not your account name. Please try again.")
        name = input("Enter your account name: ")
    password = input("Enter your account password: ")
    while password != Account[id][1]:
        print("That is not your account password. Please try again.")
        password = input("Enter your account password: ")
    print("Login successful. Welcome back " + Account[id][0] + ".")

def login(accountID, name, password, Account):
   if Account[accountID][0] == name and Account[accountID][1] == password:
       return True
   else:
       return False

def displayBalance(accountID, AccDetails):
   balance = AccDetails[accountID][0]
   print("Your current balance is:", balance)

def withdrawMoney(accountID, amount, AccDetails):
   balance = AccDetails[accountID][0]
   overdraftLimit = AccDetails[accountID][1]
   withdrawalLimit = AccDetails[accountID][2]

   if amount > withdrawalLimit:
       print("Withdrawal amount exceeds the withdrawal limit.")
   elif balance - amount < -overdraftLimit:
       print("Withdrawal amount exceeds the overdraft limit.")
   else:
       balance -= amount
       AccDetails[accountID][0] = balance
       print("Withdrawal successful. Your new balance is:", balance)

def depositMoney(accountID, amount, AccDetails):
   balance = AccDetails[accountID][0]
   newBalance = balance + amount
   AccDetails[accountID][0] = newBalance
   print("Deposit successful. Your new balance is:", newBalance)

def main(Account, AccDetails):
   accountID = int(input("Enter your account ID: "))
   name = input("Enter your name: ")
   password = input("Enter your password: ")

   if login(accountID, name, password, Account):
       print("Login successful.")
       displayMenu(accountID, AccDetails)
   else:
       print("Invalid credentials. Please try again.")

def displayMenu(accountID, AccDetails):
   while True:
       print("\nMenu:")
       print("1. Display balance")
       print("2. Withdraw money")
       print("3. Deposit money")
       print("4. Exit")
       choice = int(input("Enter your choice: "))

       if choice == 1:
           displayBalance(accountID, AccDetails)
       elif choice == 2:
           withdrawalAmount = float(input("Enter withdrawal amount: "))
           withdrawMoney(accountID, withdrawalAmount, AccDetails)
       elif choice == 3:
           depositAmount = float(input("Enter deposit amount: "))
           depositMoney(accountID, depositAmount, AccDetails)
       elif choice == 4:
           break
       else:
           print("Invalid choice. Please try again.")
getAccount()
