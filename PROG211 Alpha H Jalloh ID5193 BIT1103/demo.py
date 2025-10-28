# ============================
# demo.py
# ============================
from operation import *

def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            total = int(input("Enter total copies: "))
            print(add_book(isbn, title, author, genre, total))

        elif choice == "2":
            member_id = int(input("Enter member ID: "))
            name = input("Enter member name: ")
            email = input("Enter email: ")
            print(add_member(member_id, name, email))

        elif choice == "3":
            keyword = input("Enter book title or author to search: ")
            print(search_book(keyword))

        elif choice == "4":
            member_id = int(input("Enter member ID: "))
            isbn = input("Enter book ISBN: ")
            print(borrow_book(member_id, isbn))

        elif choice == "5":
            member_id = int(input("Enter member ID: "))
            isbn = input("Enter book ISBN: ")
            print(return_book(member_id, isbn))

        elif choice == "6":
            isbn = input("Enter ISBN to delete: ")
            print(delete_book(isbn))

        elif choice == "7":
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
