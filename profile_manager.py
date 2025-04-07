#Imports necessary libraries
import pandas as pd

#Made by Pedro Elias Souza

def edit_profile():
    reader = pd.read_csv('user.csv')
    choice = input("Would you like to:\n1. Changer username\n2. Change password\n3. Leave\n")
    if choice == "1":
        def change_user():
            new_user = input("What is the new username: ")
            reader.loc[0, 0] = new_user
        
        change_user

    elif choice == "1":
        pass



#Big function with inner functions that stores most of the important variables and defines functions
def profile_main():
    reader = pd.read_csv('user.csv')

    choice = input("Would you like to:\n1. Log in\n2. Edit account\n3. Create new account\n4. Leave\n")
    if choice == "1":
        def log_in():
            user = input("What is the username you want to log in to? (default is 'username') ")
            password = input("What is the password for the amount? (default is 'Password_123') ")
            if user == reader.loc[0, 0] and user == reader.loc[0, 1]:
                reader.loc[0, 2] = "in"
                print("succesfully logged in")
            else:
                reader.loc[0, 2] = "out"
                print("incorrect password")
        
        log_in()

    elif choice == "2":
        if reader.loc[0, 2] == "in":
            edit_profile()
        else:
            print("You need to log in to do this")

    elif choice == "3":
        print("This feature is not avaliable for use in this moment")

    elif choice == "4":
        pass
    
    else:
        print("Invalid input, your options are 1, 2 and 3")
