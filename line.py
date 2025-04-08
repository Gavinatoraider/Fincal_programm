#File for making the line chart of income vs expenses per month
#Made by Pedro

import pandas as pd
import matplotlib.pyplot as plt

def graph():
    #Read the CSVs
    income = pd.read_csv('user_income.csv')
    expenses = pd.read_csv('user_expenses.csv')

    #Convert date columns to datetime
    income['date'] = pd.to_datetime(income['date'])
    expenses['date'] = pd.to_datetime(expenses['date'])

    #Create "month" column for grouping
    income['month'] = income['date'].dt.to_period('M')
    expenses['month'] = expenses['date'].dt.to_period('M')

    #Group by month and sum amounts
    monthly_income = income.groupby('month')['amount'].sum()
    monthly_expenses = expenses.groupby('month')['amount'].sum()

    #Align both series (fill missing months with 0)
    combined = pd.concat([monthly_income, monthly_expenses], axis=1).fillna(0)
    combined.columns = ['Income', 'Expenses']

    #Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(combined.index.astype(str), combined['Income'], label='Income', marker='o')
    plt.plot(combined.index.astype(str), combined['Expenses'], label='Expenses', marker='x')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Monthly Income vs Expenses')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('chart.png')
    plt.show()
