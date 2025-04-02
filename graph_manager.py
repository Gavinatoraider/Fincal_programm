import pandas as pd
import matplotlib.pyplot as plt

categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance"]

def graph_main():
    # Read the CSV
    reader = pd.read_csv('user_expenses.csv')

    # Group by category and sum the amounts
    category_totals = reader.groupby("category")["amount"].sum()

    # Filter to include only predefined categories
    category_totals = category_totals[category_totals.index.isin(categories)]

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.show()
    plt.savefig('chart.png')
