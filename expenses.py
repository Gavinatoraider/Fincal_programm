#Set expenses to csv

#Imports necessary libraries
import pandas as pd
from income import get_date, get_amount

#List of categories for expenses and budget
categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance", "household", "personal", "debt", "education", "saving", "gift", "entertainment", "other"]

#Function that adds it
def add_expense():
    date = get_date()  #Uses income's get date thing to get the date
    amount = get_amount()  #Same with amount
    category = input("Enter expense category (e.g., food, insurance): ").strip().lower()  #Asks for category the thing is in

    #Check if the category is valid
    if category not in categories:
        print(f"Warning: '{category}' is not a valid category. Please choose from the following:")
        print(", ".join(categories))
        return  #Exit if invalid category

    #Load the budget to check if the expense exceeds the budget
    try:
        budget_df = pd.read_csv("budget.csv")
    except FileNotFoundError:
        print("No budget file found. Proceeding without budget check.")
        budget_df = pd.DataFrame()

    #Check if the budget for this category exists
    if category in budget_df.columns:
        budget_limit = budget_df[category].iloc[0]  #Get the budget limit for the category
        if amount > budget_limit:
            confirmation = input(f"Warning: You are going over the budget for {category}. Budget limit is ${budget_limit}. Are you sure you want to continue? (yes/no): ").strip().lower()
            if confirmation != 'yes':
                print("Expense not added.")
                return  #Exit if the user doesn't confirm

    #Saves the data in csv
    newData = pd.DataFrame([[date, amount, category]], columns=["date", "amount", "category"])
    newData.to_csv("user_expenses.csv", mode="a", index=False, header=False)
    print("Expense added.\n")
