transactions = []
transaction_id = 1
def add_transaction(t_type, amount):
    global transaction_id

    if amount <= 0:
        print("Invalid amount!")
        return
    if t_type == "Withdraw" and amount > check_balance():
        print("Insufficient balance!")
        return

    transaction = {
        "ID": transaction_id,
        "Type": t_type,
        "Amount": amount
    }

    transactions.append(transaction)
    transaction_id += 1
    print(f"{t_type} Successful!")

def check_balance():
    balance = 0
    for t in transactions:
        if t["Type"] == "Deposit":
            balance += t["Amount"]
        else:
            balance -= t["Amount"]
    return balance

def show_transactions():
    if not transactions:
        print("No transactions found.")
        return

    print("\nTransaction History:")
    for t in transactions:
        print(f"ID: {t['ID']} | {t['Type']} | Amount: {t['Amount']}")

def main():
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Transactions")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter deposit amount: "))
            add_transaction("Deposit", amt)

        elif choice == "2":
            amt = float(input("Enter withdraw amount: "))
            add_transaction("Withdraw", amt)

        elif choice == "3":
            print("Current Balance:", check_balance())

        elif choice == "4":
            show_transactions()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

main()
