#Main file with prompt and UI

#Made by Pedro Elias Souza

#Importing all the libraries, files and functions to main so they can be called
import pandas as pd
from graph_manager import graph_main
from profile_manager import profile_main
from savings import savings
from budgeting import budget
from income_expense import income_expenses

#Function that checks for what the thing we should do is
def main():
    #Load the user profile to check if they are logged in
    reader = pd.read_csv('user.csv')
    
    #Check if the user is logged in
    is_logged_in = reader.loc[0, 'status'] == 'in'

    if is_logged_in:
        #If logged in, show full menu
        choice = input("Would you like to:\n1. Manage profile\n2. Manage income and expenses\n3. Manage budget\n4. Manage savings\n5. See graphs\n6. Leave\n")
    else:
        #If not logged in, show limited menu
        choice = input("You need to log in to access most options.\nWould you like to:\n1. Manage profile\n2. Leave\n")

    if choice == "1":
        profile_main()

    elif choice == "2":
        if is_logged_in:
            income_expenses()
        else:
            print("Please log in to manage income and expenses.")

    elif choice == "3":
        if is_logged_in:
            budget()
        else:
            print("Please log in to manage your budget.")

    elif choice == "4":
        if is_logged_in:
            savings()
        else:
            print("Please log in to manage your savings.")

    elif choice == "5":
        if is_logged_in:
            graph_main()
        else:
            print("Please log in to see graphs.")

    elif choice == "6":
        print("Goodbye!")
        exit()

    else:  #Error handling for invalid input
        print("Invalid input")

#Function called forever (until the code is terminated with exit())
while True:
    main()
