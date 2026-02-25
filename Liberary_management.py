# Library Management System

library = {}   

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    library[book_id] = {
        "title": title,
        "author": author,
        "issued": False
    }
    
    print("Book added successfully!\n")


def view_books():
    if not library:
        print("No books in library.\n")
        return
    
    for book_id, details in library.items():
        status = "Issued" if details["issued"] else "Available"
        print(f"ID: {book_id}")
        print(f"Title: {details['title']}")
        print(f"Author: {details['author']}")
        print(f"Status: {status}")
        print("-" * 30)


def issue_book():
    book_id = input("Enter Book ID to issue: ")
    
    if book_id in library:
        if not library[book_id]["issued"]:
            library[book_id]["issued"] = True
            print("Book issued successfully!\n")
        else:
            print("Book is already issued.\n")
    else:
        print("Book not found.\n")


def return_book():
    book_id = input("Enter Book ID to return: ")
    
    if book_id in library:
        if library[book_id]["issued"]:
            library[book_id]["issued"] = False
            print("Book returned successfully!\n")
        else:
            print("Book was not issued.\n")
    else:
        print("Book not found.\n")


def delete_book():
    book_id = input("Enter Book ID to delete: ")
    
    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!\n")
    else:
        print("Book not found.\n")


# Main Menu
while True:
    print("====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        print("Exiting... Thank You!")
        break
    else:
        print("Invalid choice! Try again.\n")