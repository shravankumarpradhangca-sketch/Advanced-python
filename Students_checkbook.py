#Student_Checkbook System
checkbook = {}
def add_transaction():
    transaction_id = len(checkbook) + 1
    t_type = input("Enter transaction type (Deposit/Withdraw): ")
    amount = float(input("Enter amount: "))
    if t_type not in ["Deposit", "Withdraw"]:
        print("Invalid transaction type.")
        return
    checkbook[transaction_id] = {
        "type": t_type,
        "amount": amount
    }
    print("Transaction added successfully!\n")

def view_checkbook():
    if not checkbook:
        print("No transactions found.\n")
        return
    print("Checkbook Transactions:")
    for tid, details in checkbook.items():
        print(f"ID: {tid} | Type: {details['type']} | Amount: {details['amount']}")
    print()
def calculate_balance():
    balance = 0
    for details in checkbook.values():
        if details["type"] == "Deposit":
            balance += details["amount"]
        else:
            balance -= details["amount"]
    print(f"Current Balance: {balance}\n")
def main():
    while True:
        print("=== Student Checkbook System ===")
        print("1. Add Transaction")
        print("2. View Checkbook")
        print("3. Calculate Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_checkbook()
        elif choice == "3":
            calculate_balance()
        elif choice == "4":
            print("Thank you for using the Student Checkbook System!")
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    main()