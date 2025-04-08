#Main file with prompt and UI

#Made by Pedro Elias Souza

#Importing all the files and functions to main so they can be called
from graph_manager import graph_main
from profile_manager import profile_main
from savings import savings

#Function
def main():
    choice = input("Would you like to:\n1. Manage profile\n2. Manage income and expenses\n3. Manage budget\n4. Manage savings\n5. See graphs\n6. Leave\n")

    if choice == "1":
        profile_main()

    elif choice == "2":
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        savings()

    elif choice == "5":
        graph_main()

    elif choice == "6":
        print("Goodbye!")
        exit()

    else:
        print("Invalid input")

#Function called forever (untill the code is terminated with exit())
while True:
    main()