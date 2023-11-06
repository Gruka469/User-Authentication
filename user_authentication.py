user_database = {}
user_profiles = {}

def register_user(username, password):
    if username not in user_database:
        user_database[username] = password
        user_profiles[username] = {}
        print("User registered successfully")
    else:
        print("Username already exists try a different one.")


def authenticate_user(username, password):
    if username in user_database and user_database[username] == password:
        return True
    else:
        return False
    

def profile_info(username):
    if username in user_profiles:
        print(f"Welcome, {username}! Please provide some additional information:")
        additional_info = input("Enter information: ")
        user_profiles[username]["additional_info"] = additional_info
        print("Information saved successfully.")
    else:
        print("User not found. Please log in first.")

def print_user_info(username):
    if username in user_profiles:
        additional_info = user_profiles[username].get("additional_info")
        print(f"Additional information for {username}: {additional_info}")
    else:
        print("User not found.")
    
while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Authenticate")
    print("3. Profile Info")
    print("4. User Information")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        username_input = input("Enter Username: ")
        password_input = input("Enter Password: ")
        register_user(username_input, password_input)

    elif choice == "2":
        username_input = input("Enter Username: ")
        password_input = input("Enter Password: ")
        if authenticate_user(username_input, password_input):
            print("Authentication successful.")
        else:
            print("Authentication failed.")

    elif choice == "3":
        username_input = input("Enter Username: ")
        profile_info(username_input)

    elif choice == "4":
        username_input = input("Enter Username: ")
        print_user_info(username_input)

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")