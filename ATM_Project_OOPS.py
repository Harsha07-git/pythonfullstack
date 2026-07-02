class ATM:
    def __init__(self, name, account_no, pin, balance):
        self.name = name
        self.account_no = account_no
        self.__pin = pin
        self.__balance = balance

    def check_pin(self):
        entered_pin = input("Enter PIN: ")
        return entered_pin == self.__pin

    def check_balance(self):
        print(f"\nAvailable Balance: ₹{self.__balance:.2f}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            self.__balance += amount
            print("Deposit Successful!")
            print(f"Updated Balance: ₹{self.__balance:.2f}")
        else:
            print("Invalid Amount!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid Amount!")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print("Withdrawal Successful!")
            print(f"Remaining Balance: ₹{self.__balance:.2f}")

    def change_pin(self):
        old_pin = input("Enter Current PIN: ")
        if old_pin == self.__pin:
            new_pin = input("Enter New 4-digit PIN: ")
            self.__pin = new_pin
            print("PIN Changed Successfully!")
        else:
            print("Incorrect Current PIN!")

    def account_details(self):
        print("\n------ ACCOUNT DETAILS ------")
        print("Account Holder :", self.name)
        print("Account Number :", self.account_no)



print("========== WELCOME TO ATM ==========\n")

name = input("Enter Account Holder Name: ")
account_no = input("Enter Account Number: ")
pin = input("Set a 4-digit ATM PIN: ")
balance = float(input("Enter Initial Balance: ₹"))

atm = ATM(name, account_no, pin, balance)

print("\nAccount Created Successfully!")

attempts = 3

while attempts > 0:
    if atm.check_pin():
        print("\nLogin Successful!")

        while True:
            print("\n========== ATM MENU ==========")
            print("1. Account Details")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Change PIN")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                atm.account_details()

            elif choice == "2":
                atm.check_balance()

            elif choice == "3":
                atm.deposit()

            elif choice == "4":
                atm.withdraw()

            elif choice == "5":
                atm.change_pin()

            elif choice == "6":
                print("\nThank you for using our ATM!")
                exit()

            else:
                print("Invalid Choice! Please try again.")

    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN! {attempts} attempt(s) remaining.")
        else:
            print("\nAccount Blocked!")
            print("You have entered the wrong PIN 3 times.")
            print("Please contact your bank.")

            
