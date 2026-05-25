'''
                                    KT
                                    --
'''
user_info = {"Name":"Harshavardhan",
             "Mobile Number": "",
             "ATM PIN": "6600",
             "Balance": 48784,
             "Transaction History": []
             }

print("Please insert your ATM Card")
remaining_attempts = 3
while remaining_attempts > 0:
    user_pin = input("Please enter your ATM pin: ")
    if len(user_pin) == 4:
        if user_pin in user_info['ATM PIN']:
            
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transaction History")
            print("5. Exit")

            select = int(input("Select Option: "))

            if select == 1:
                print(f"Available Balance: Rs.{user_info['Balance']}")

            elif select == 2:
                amount = float(input("Enter the amount to withdraw: "))

                if amount <= 0:
                    print("Invalid amount")
                elif amount > user_info['Balance']:
                    print("The entered withdrawal amount is more than Available Balance")
                elif amount >= 500 and amount % 100 == 0:
                    user_info['Balance'] -= amount

                    user_info['Transaction History'].append(f"Withdrawn Rs.{amount}")
                    print("Please collect cash")
                else:
                    print("Invalid amount")

            elif select == 3:
                amount = float(input("Enter the amount to deposit: "))

                if amount >= 500:
                    user_info['Balance'] += amount

                    user_info['Transaction History'].append(f"Deposited Rs.{amount}")
                    print("Amount deposited successfully")

                else:
                    print("Invalid Amount")
                    
            elif select == 4:
                print("---Transaction History---")
                if len(user_info['Transaction History']) == 0:
                    print("No Transactions found")
                else:
                    for t in user_info['Transaction History']:
                        print(t)

            elif select == 5:
                print("Thank you for Banking with us.")
                break

            else:
                print("Invalid choice")
                
        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"Invalid pin entered and you have {remaining_attempts} left")
            else:
                print("Your card is blocked. ")
                break
    else:
        print("Invalid!!! Please enter 4-digit pin")

        
            
    

