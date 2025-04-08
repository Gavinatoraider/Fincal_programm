#File that manages the graphs, runs them

#Imports the graph files
from pie import graph as pie_chart
from line import graph as line_graph

#Made by Pedro

#Main graph function that prints out the pie chrt
def graph_main():
    choice = input("Would you like to see:\n1. Expenses by category pie chart\n2. Income and expenses line graph\n3. Expenses to bar graph\n")
    if choice == "1":
        pie_chart()
    elif choice == "2":
        line_graph()
    elif choice == "3":
        pass
    else:
        print("Invalid chart choice, please answer with numbers")