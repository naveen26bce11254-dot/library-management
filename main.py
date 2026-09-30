# Library Management System
# Developed for VIT Course Project

def show_menu():
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add New Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

def main():
    # Dictionary to store library inventory
    library_data = {}
    next_id = 101

    while True:
        show_menu()
        user_choice = input("Enter choice (1-6): ").strip()

        # Option 1: Add a new book
        if user_choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            
            if title != "" and author != "":
                library_data[next_id] = {"title": title, "author": author, "issued": False}
                print(f"Book added successfully! Book ID: {next_id}")
                next_id += 1
            else:
                print("Error: Title and Author cannot be empty!")

        # Option 2: Display all books
        elif user_choice == '2':
            if len(library_data) == 0:
                print("No books available in the library!")
            else:
                print("\nID\t Title\t\t Author\t\t Status")
                print("-" * 50)
                for b_id in library_data:
                    book = library_data[b_id]
                    if book["issued"] == True:
                        status = "Issued"
                    else:
                        status = "Available"
                    print(f"{b_id}\t {book['title']}\t\t {book['author']}\t\t {status}")

        # Option 3: Search book by title
        elif user_choice == '3':
            query = input("Enter book name to search: ").strip().lower()
            found_flag = False
            for b_id in library_data:
                book = library_data[b_id]
                if query in book["title"].lower():
                    if book["issued"] == True:
                        status = "Issued"
                    else:
                        status = "Available"
                    print(f"Match Found -> ID: {b_id} | Title: {book['title']} | Author: {book['author']} | Status: {status}")
                    found_flag = True
            if found_flag == False:
                print("No book found with this title!")

        # Option 4: Issue a book
        elif user_choice == '4':
            try:
                target_id = int(input("Enter Book ID to issue: "))
                if target_id in library_data:
                    if library_data[target_id]["issued"] == False:
                        library_data[target_id]["issued"] = True
                        print("Book issued successfully!")
                    else:
                        print("This book is already issued!")
                else:
                    print("Book ID not found!")
            except:
                print("Please enter a valid numerical ID!")

        # Option 5: Return a book
        elif user_choice == '5':
            try:
                target_id = int(input("Enter Book ID to return: "))
                if target_id in library_data:
                    if library_data[target_id]["issued"] == True:
                        library_data[target_id]["issued"] = False
                        print("Book returned successfully!")
                    else:
                        print("This book was not issued!")
                else:
                    print("Book ID not found!")
            except:
                print("Please enter a valid numerical ID!")

        # Option 6: Exit program
        elif user_choice == '6':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
  
