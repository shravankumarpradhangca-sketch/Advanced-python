#ATM System using multiple accounts
accounts = {}
def create_account():
    acc_num = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    
    accounts[acc_num] = {
        "name": name,
        "balance": balance 
    }
    
    print("Account created successfully!\n")

def deposit():
    acc_num = input("Enter Account Number: ")
    amount = float(input("Enter Deposit Amount: "))
    
    if acc_num in accounts:
        accounts[acc_num]["balance"] += amount
        print("Deposit successful!\n")
    else:
        print("Account not found.\n")

def withdraw():
    acc_num = input("Enter Account Number: ")
    amount = float(input("Enter Withdrawal Amount: "))
    
    if acc_num in accounts:
        if accounts[acc_num]["balance"] >= amount:
            accounts[acc_num]["balance"] -= amount
            print("Withdrawal successful!\n")
        else:
            print("Insufficient balance.\n")
    else:
        print("Account not found.\n")

def check_balance():
    acc_num = input("Enter Account Number: ")
    
    if acc_num in accounts:
        print(f"Account Holder: {accounts[acc_num]['name']}")
        print(f"Current Balance: {accounts[acc_num]['balance']}\n")
    else:
        print("Account not found.\n")

def main():
    while True:
        print("=== ATM System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the ATM System!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
