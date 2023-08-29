# Printing the Welcome Address
print("\n***** Welcome to Vikram's ATM *****\n")

# Getting user name, phone number and inital amount
name = input("Enter your name : ")
ph_number = int(input("Enter your phone number : "))
init_amount = float(input("Enter the initial amount you want to deposit for activating your account : "))
print("\nYour account has been created and activated successfully!")

# record_history -> Records all the transactions
record_history = {}
record_history[len(record_history)+1] = ["Principle", init_amount]

# options() function to show the list of all the options
def options():
    print("""
Enter - 1 for Deposit
2 for Withdraw
3 for Check Balance
4 for Transaction History
5 for Exit Vikram's ATM
          """)

# deposit() function to deposit amount into the account
def deposit():
    global init_amount
    deposit = float(input("Enter the amount you want to deposit : "))
    init_amount += deposit
    record_history[len(record_history)+1] = ["Deposited", deposit]
    print("Successfully deposited!")

# withdraw() function to withdraw amount from the account
def withdraw():
    global init_amount
    withdraw = float(input("Enter the amount you want to withdraw : "))
    if withdraw > init_amount:
        print("* You can't withdraw more than your balance! *")
    else:
        init_amount -= withdraw
        record_history[len(record_history)+1] = ["Withdrawn", withdraw]
        print("Successfully withdrawn!")

# check_balance() function to check the balance of the account
def check_balance():
    global init_amount
    print("Your current balance is :", init_amount)

# transaction_history() function to display all the transactions
def transaction_history():
    keys= list(record_history.keys())
    values = list(record_history.values())
    print("S.No  Activity      Amount\n--------------------------")
    for i in range(len(keys)):
        print(str(keys[i])+"     "+values[i][0]+"     "+str(values[i][1]))

while(True):
    options()
    option = int(input("Enter the option : "))
    if option == 1:
        deposit()
    
    elif option == 2:
        withdraw()

    elif option == 3:
        check_balance()

    elif option == 4:
        transaction_history()

    elif option == 5:
        print("\n***** Thanks for using Vikram's ATM! Visit Again! *****\n")
        break

    else:
        print("*** You have entered a wrong option, kindly enter a correct option! ***")
