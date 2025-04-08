#Import needed library
import pandas as pd

#Done by gavin (fixed up by Pedro as it didn't work)

def savings():
    filename = "goals.csv"

    #Load reader/editor of the file
    reader = pd.read_csv(filename)

    
    savings_like_to_do = input(
        "\nWould you like to:\n""1. Set a new goal\n""2. Add savings to a goal\n""3. Check progress\n""4. Back to main\n")

    if savings_like_to_do == "1":
        goal = input("Enter goal name: ").strip()
        if goal.lower() in reader["goal"].str.lower().values:
            print("That goal already exists.")
        try:
            target = float(input("Enter target amount: "))
            reader.loc[len(reader)] = [goal, target, 0.0]
            reader.to_csv(filename, index=False)
            print("Goal added.")
        except ValueError:
            print("Invalid amount.")

    elif savings_like_to_do == "2":
        goal = input("Enter goal name to add savings to: ").strip()
        match = reader[reader["goal"].str.lower() == goal.lower()]
        if match.empty:
            print("Goal not found.")
        try:
            amount = float(input("How much to add? "))
            idx = match.index[0]
            reader.at[idx, "amount_saved"] += amount
            reader.to_csv(filename, index=False)
            print("Amount added.")
        except ValueError:
            print("Invalid number.")

    elif savings_like_to_do == "3":
        goal = input("Enter goal name to check: ").strip()
        match = reader[reader["goal"].str.lower() == goal.lower()]
        if match.empty:
            print("Goal not found.")
        else:
            row = match.iloc[0]
            percent = (row["amount_saved"] / row["target_amount"]) * 100
            print(f"{row['goal']} progress: ${row['amount_saved']:.2f} / ${row['target_amount']:.2f} ({percent:.1f}%)")

    elif savings_like_to_do == "4":
        print("Returning to main.")

    else:
        print("Please enter a valid option.")
