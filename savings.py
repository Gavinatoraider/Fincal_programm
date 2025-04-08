#Import needed library
import pandas as pd

#Done by gavin (fixed and commented up by Pedro as it didn't work)

def savings():
    filename = "goals.csv"  # Name of the CSV file storing goals

    #Load reader/editor of the file
    reader = pd.read_csv(filename)

    #Asks what the user wants to do
    savingsLikeToDo = input(
        "\nWould you like to:\n""1. Set a new goal\n""2. Add savings to a goal\n""3. Check progress\n""4. Back to main\n")

    #If the user wants to set a new goal
    if savingsLikeToDo == "1":
        goal = input("Enter goal name: ").strip()  # Get the goal name from the user
        if goal.lower() in reader["goal"].str.lower().values:  # Check if the goal already exists
            print("That goal already exists.")  # Inform the user if goal exists

        try:
            target = float(input("Enter target amount: "))  # Get target amount for the goal
            reader.loc[len(reader)] = [goal, target, 0.0]  # Add goal to the dataframe with 0 saved
            reader.to_csv(filename, index=False)  # Save the updated data to CSV
            print("Goal added.")  # Confirmation message

        except ValueError:  # Handle invalid input for target amount
            print("Invalid amount.")  # Inform the user of the invalid input

    #If the user wants to add savings to a goal
    elif savingsLikeToDo == "2":
        goal = input("Enter goal name to add savings to: ").strip()  # Get goal name to add savings
        match = reader[reader["goal"].str.lower() == goal.lower()]  # Find the matching goal

        if match.empty:  # If goal is not found
            print("Goal not found.")  # Inform the user that the goal was not found

        try:
            amount = float(input("How much to add? "))  # Get the amount to add to savings
            idx = match.index[0]  # Get the index of the goal to update
            reader.at[idx, "amount_saved"] += amount  # Update the amount saved for that goal
            reader.to_csv(filename, index=False)  # Save the updated data to CSV
            print("Amount added.")  # Confirmation message

        except ValueError:  # Handle invalid input for amount
            print("Invalid number.")  # Inform the user of invalid input

    #If the user wants to check the progress of a goal
    elif savingsLikeToDo == "3":
        goal = input("Enter goal name to check: ").strip()  # Get the goal name to check progress
        match = reader[reader["goal"].str.lower() == goal.lower()]  # Find the matching goal

        if match.empty:  # If goal is not found
            print("Goal not found.")  # Inform the user that the goal was not found

        else:
            row = match.iloc[0]  # Get the first matching goal
            percent = (row["amount_saved"] / row["target_amount"]) * 100  # Calculate the progress percentage
            print(f"{row['goal']} progress: ${row['amount_saved']:.2f} / ${row['target_amount']:.2f} ({percent:.1f}%)")  # Show progress

    #If the user wants to return to the main menu
    elif savingsLikeToDo == "4":
        print("Returning to main.")  # Message before going back to main menu

    else:  # If the user enters an invalid option
        print("Please enter a valid option.")  # Inform the user to enter a valid option
