balance = 5000
while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your Balance = Rs.", balance)
    elif choice == 2:
        deposit_amount = int(input("Enter amount to deposit: "))
        balance += deposit_amount
        print("Amount deposited successfully.")
    elif choice == 3:
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    elif choice == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")
balance = 5000
while True:
 print("\n----- ATM Menu -----")
 print("1. Check Balance")
 print("2. Deposit")
 print("3. Withdraw")
 print("4. Exit")
 choice = int(input("Enter your choice: "))
 if choice == 1:
    print("Your Balance = Rs.", balance)
 elif choice == 2:
    deposit_amount = int(input("Enter amount to deposit: "))
    balance += deposit_amount
    print("Amount deposited successfully.")
 elif choice == 3:
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
 elif choice == 4:
    print("Thank you for using ATM")
    break
 else:
    print("Invalid choice")
