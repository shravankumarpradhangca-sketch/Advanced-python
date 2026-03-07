#Biling System for a Store
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

    def total_price(self):
        return self.product.price * self.qty


class BillingSystem:
    def __init__(self):
        self.products = []
        self.cart = []
        self.transactions = []

    def add_product(self, pid, name, price):
        product = Product(pid, name, price)
        self.products.append(product)

    def scan_product(self):
        pid = input("Enter Product ID: ")
        qty = int(input("Enter Quantity: "))

        for p in self.products:
            if p.pid == pid:
                item = CartItem(p, qty)
                self.cart.append(item)
                print("Product added to cart")
                return
        print("Product not found")

    def apply_discount(self, total):
        discount = 0
        if total > 1000:
            discount = total * 0.10
        return discount

    def generate_bill(self):
        total = 0
        print("\n----- BILL -----")
        for item in self.cart:
            cost = item.total_price()
            print(item.product.name, "x", item.qty, "=", cost)
            total += cost

        discount = self.apply_discount(total)
        final_total = total - discount

        print("Total:", total)
        print("Discount:", discount)
        print("Final Amount:", final_total)

        self.transactions.append(final_total)
        self.cart.clear()

    def show_transactions(self):
        print("\nTransactions:")
        for t in self.transactions:
            print("Bill Amount:", t)


system = BillingSystem()

# Sample products in store
system.add_product("101", "Milk", 50)
system.add_product("102", "Bread", 40)
system.add_product("103", "Rice", 60)
system.add_product("104", "Sugar", 45)

while True:
    print("\n1. Scan Product")
    print("2. Generate Bill")
    print("3. View Transactions")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        system.scan_product()

    elif choice == 2:
        system.generate_bill()

    elif choice == 3:
        system.show_transactions()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
    