# Imports necessary libraries
import pandas as pd

# Made by Pedro Elias Souza

#Function that uses pandas to read and edit the chosen parts of the profile base off what the user choses
def edit_profile():
    reader = pd.read_csv('user.csv')

    choice = input("Would you like to:\n1. Change username\n2. Change password\n3. Leave\n")
    
    if choice == "1":
        new_user = input("What is the new username: ")
        reader.loc[0, 'username'] = new_user
        print("Username updated.")

    elif choice == "2":
        new_pass = input("What is the new password: ")
        reader.loc[0, 'password'] = new_pass
        print("Password updated.")

    elif choice == "3":
        print("Leaving edit mode.")

    else:
        print("Invalid input.")

    reader.to_csv('user.csv', index=False)


# Big function with inner functions that stores most of the important variables and defines functions
def profile_main():
    reader = pd.read_csv('user.csv')

    choice = input("Would you like to:\n1. Log in\n2. Edit account\n3. Create new account\n4. Log out\n5. Leave\n")

    if choice == "1":
        def log_in(): #Whole login thing, wher it checks if user got name and password right
            user = input("Enter your username (default is 'username'): ")
            password = input("Enter your password (default is 'Password_123'): ")
            if user == reader.loc[0, 'username'] and password == reader.loc[0, 'password']:
                reader.loc[0, 'status'] = "in"
                print("Successfully logged in.")
            else:
                reader.loc[0, 'status'] = "out"
                print("Incorrect username or password.")
            reader.to_csv('user.csv', index=False)

        log_in()

    elif choice == "2":
        if reader.loc[0, 'status'] == "in":
            edit_profile()
        else:
            print("You need to log in to do this.")

    elif choice == "3":
        print("This feature is not available at the moment.")

    elif choice == "4":
        reader.loc[0, 'status'] = 'out'
        reader.to_csv('user.csv', index=False)
        print("Signed out successfully.")

    elif choice == "5":
        print("Exiting")

    else: #Error managing
        print("Invalid input. Options are 1, 2, 3, or 4.")
