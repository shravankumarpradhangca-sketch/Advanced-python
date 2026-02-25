#Online Shopping Cart System
cart = {}

def add_item():
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))
    quantity = int(input("Enter Quantity: "))
    
    cart[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    print("Item added to cart successfully!\n")

def view_cart():
    if not cart:
        print("Your cart is empty.\n")
        return
    
    total = 0
    print("Items in your cart:")
    for item_id, details in cart.items():
        item_total = details["price"] * details["quantity"]
        total += item_total
        print(f"ID: {item_id}")
        print(f"Name: {details['name']}")
        print(f"Price: {details['price']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Total: {item_total}")
        print("-" * 30)
    
    print(f"Cart Total: {total}\n")

def remove_item():
    item_id = input("Enter Item ID to remove: ")
    
    if item_id in cart:
        del cart[item_id]
        print("Item removed from cart successfully!\n")
    else:
        print("Item not found in cart.\n")

def checkout():
    if not cart:
        print("Your cart is empty. Add items before checkout.\n")
        return
    
    total = 0
    print("Checkout Summary:")
    for item_id, details in cart.items():
        item_total = details["price"] * details["quantity"]
        total += item_total
        print(f"ID: {item_id}")
        print(f"Name: {details['name']}")
        print(f"Price: {details['price']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Total: {item_total}")
        print("-" * 30)
    
    print(f"Total Amount Due: {total}\n")
    print("Thank you for shopping with us!")

def main():
    while True:
        print("1. Add Item to Cart")
        print("2. View Cart")
        print("3. Remove Item from Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()





