import pandas as pd

categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance", "household", "personal", "debt", "education", "saving", "gift", "entertainment", "other"]

def budget():
    def total_recentMonth_income():
        reader = pd.read_csv("user_income.csv")
        
        # Convert date column to datetime
        reader["date"] = pd.to_datetime(reader["date"], format="%m/%d/%Y")

        # Find most recent month and year
        latest = reader["date"].max()
        recentMonth = latest.month
        recent_year = latest.year

        # Filter rows from that month and year
        recentData = reader[(reader["date"].dt.month == recentMonth) & (reader["date"].dt.year == recent_year)]

        total = recentData["amount"].sum()
        print(f"Total income for {recentMonth:02}/{recent_year}: ${total}")
        return total

    total_income = total_recentMonth_income()

    def set_budget(total_income):
        limits = {}
        for i in categories:
            while True:
                limit_choice = input(f"What percent of your income do you want {i} limits to be? (Leave 0 To Not Use): ")

                # Check if input is a valid number and handle non-numeric input
                if limit_choice.isdigit():
                    limit_choice = int(limit_choice)
                    if limit_choice != 0:
                        limit_choice = (limit_choice / 100) * total_income
                    limits[i] = limit_choice
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
                    
        return limits
    
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
