#File for making the pie chart of expenses by category

#Made by Pedro

import pandas as pd
import matplotlib.pyplot as plt
import numpy 

#List of all categories
categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance", "household", "personal", "debt", "education", "saving", "gift", "entertainment", "other"]

def graph():
    #Read the CSV
    reader = pd.read_csv('user_expenses.csv')

    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()
    plt.title("Expenses by Category")
    plt.show()
    plt.savefig('chart.png')