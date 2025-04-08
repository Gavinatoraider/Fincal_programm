#File for making the pie chart of expenses by category

#Made by Pedro

import pandas as pd
import matplotlib.pyplot as plt

#List of all categories
categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance", "household", "personal", "debt", "education", "saving", "gift", "entertainment", "other"]

def graph():
    #Read the CSV
    reader = pd.read_csv('user_expenses.csv')

    #Group by category and sum the amounts
    categoryTotals = reader.groupby("category")["amount"].sum()

    #Filter to include only predefined categories
    categoryTotals = categoryTotals[categoryTotals.index.isin(categories)]

    
    #Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(categoryTotals, labels=categoryTotals.index, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.show()
    plt.savefig('chart.png')