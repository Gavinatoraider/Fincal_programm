#Import necessary things
import pandas as pd

#List of categories
categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance", "household", "personal", "debt", "education", "saving", "gift", "entertainment", "other"]

#Made by Asher (fixed and commented by Pedro as it didn't work)

#Big function with inner function, calls and defines inner functions
def budget():
    #Function to ask the user for a specific month and year
    def get_month_and_year():
        while True:
            monthYear = input("Enter the month and year (MM/YYYY): ").strip()
            if len(monthYear) == 7 and monthYear[2] == '/':
                month, year = monthYear.split('/')
                if month.isdigit() and year.isdigit() and 1 <= int(month) <= 12:
                    return month, year
            print("Invalid format. Please enter in MM/YYYY format.")

    #Ask for the specific month and year
    month, year = get_month_and_year()

    #Load the income data
    reader = pd.read_csv("user_income.csv")
    
    #Convert date column to datetime
    reader["date"] = pd.to_datetime(reader["date"], format="%m/%d/%Y")

    #Filter rows for the given month and year
    filtered_data = reader[(reader["date"].dt.month == int(month)) & (reader["date"].dt.year == int(year))]

    #Calculate total income for that month
    total_income = filtered_data["amount"].sum()
    print(f"Total income for {month}/{year}: ${total_income:.2f}")

    #Function to set budget based on total income
    def set_budget(total_income):
        limits = {}
        total_percent = 0

        #Ask user for percentage of income to allocate to each category
        for category in categories[:-1]:  #Exclude 'other' category for now
            while True:
                limitChoice = input(f"What percent of your income do you want {category} limits to be? (Leave 0 To Not Use): ")
                
                #Check if input is a valid number
                if limitChoice.isdigit():
                    limitChoice = int(limitChoice)
                    if limitChoice < 0:
                        print("Please enter a positive number.")
                    else:
                        limits[category] = limitChoice
                        total_percent += limitChoice
                        break
                else:
                    print("Invalid input. Please enter a valid number.")
        
        #If the total percentage exceeds 100, adjust the 'other' category
        if total_percent > 100:
            print("Total budget percentages exceed 100%. Adjusting 'other' category to balance.")
            limits["other"] = total_percent - 100
        else:
            limits["other"] = 100 - total_percent  #Ensure total is 100%

        #Save or update the budget for the specified month
        budget_data = pd.DataFrame([limits], columns=categories)
        budget_data.insert(0, "month", f"{month}/{year}")

        try:
            existing_data = pd.read_csv("budget.csv")
            if f"{month}/{year}" in existing_data["month"].values:
                #If the month already exists, update it
                existing_data.loc[existing_data["month"] == f"{month}/{year}", categories] = budget_data[categories].values
                existing_data.to_csv("budget.csv", index=False)
            else:
                #Append if the month doesn't exist
                budget_data.to_csv("budget.csv", mode="a", index=False, header=not existing_data.empty)
            print(f"Budget for {month}/{year} saved.")
        except FileNotFoundError:
            #Create the file if it doesn't exist
            budget_data.to_csv("budget.csv", mode="w", index=False, header=True)
            print(f"Budget for {month}/{year} saved.")

    #Ask the user if they want to set a budget
    print("""
    Budget Choices
    1. Set Budget Limit
    2. Exit""")

    budget_choice = input("Choose a Number: ")

    if budget_choice == "1":
        set_budget(total_income)
    elif budget_choice == "2":
        return
    else:
        print("Not an Option!")
        budget()
