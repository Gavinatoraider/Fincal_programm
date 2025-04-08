#File that manages both income and expenses addition (also views the income and expenses)

#Imports needed libraries and other file's fucntions
import pandas as pd
from income import add_income
from expenses import add_expense

#Contributed by everyone

#Function to see the income and expenses
def view_data():
    try:
        print("\nIncome:")
        income_df = pd.read_csv("user_income.csv", names=["date", "amount", "source"])
        print(income_df.to_string(index=False))
    except FileNotFoundError:
        print("No income data found.")

    try:
        print("\nExpenses:")
        expense_df = pd.read_csv("user_expenses.csv", names=["date", "amount", "category"])
        print(expense_df.to_string(index=False))
    except FileNotFoundError:
        print("No expense data found.")

def income_expenses():
    print("Income & Expenses Menu\n1. Add Income Entry\n2. Add Expense Entry\n3. View Income and Expenses\n4. Back to Main Menu")
    choice = input("Choose a number: ").strip()

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_data()
    elif choice == "4":
        return
    else:
        print("Not a valid choice!")
