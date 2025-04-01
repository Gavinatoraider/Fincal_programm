#savings page

import goals.csv

while True:
    savings_like_to_do=input("welcome to savings what would you like to do?\n1. make a new goal\n2. see goal status\n3. back to main.")
    if savings_like_to_do == "1":
        new_goal=input("what is your new goal? ")
        #adds goal to goals.csv
        #if new_goal in goals.csv
        like_to_change_goal=input("that goal already exists do you want to make a new goal instead? (yes or no)")
        while True:
            if like_to_change_goal=="yes":
                new_goal=input("what is your new goal? ")
                #add goal to CSV
            elif like_to_change_goal == "no":
                break
            else: print("you need a valid choice.")
    elif savings_like_to_do == "2":
        goal_to_see=("what is the goal you want to see? ")
        if goal_to_see in goals.csv: #displays goal status.
            
            else:
            print("that goal does not exist.")