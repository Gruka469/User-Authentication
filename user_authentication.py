user_database = {}

def register_user(username, password):
    if username not in user_database:
        user_database[username] = password
        print("User registered successfully")
    else:
        print("Username already exists try a different one.")


def authenticate_user(username, password):
    if username in user_database and user_database[username] == password:
        return True
    else:
        return False
    

def profile_info():
    pass
    
while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Authenticate")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        username_input = input("Enter Username: ")
        password_input = input("Enter Password: ")
        register_user(username_input, password_input)
    elif choice == "2":
        username_input = input("Enter Username:")
        password_input = input("Enter Password:")
        if authenticate_user(username_input, password_input):
            print("Authentication successful.")
        else:
            print("Authentication failed.")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please select a valid option.")