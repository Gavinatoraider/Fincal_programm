import pandas as pd
from income import get_date, get_amount

def add_expense():
    date = get_date()
    amount = get_amount()
    category = input("Enter expense category (e.g., food, insurance): ").strip().lower()

    newData = pd.DataFrame([[date, amount, category]], columns=["date", "amount", "category"])
    newData.to_csv("user_expenses.csv", mode="a", index=False, header=False)
    print("Expense added.\n")

