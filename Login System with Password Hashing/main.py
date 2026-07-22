from database import create_database
from auth import register, login

create_database()

while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        register(username, password)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        login(username, password)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")