#File for adding income stuff

#Imports needed library
import pandas as pd

#Income and expenses part was split between all members

#Function is to get the month of the user in right formatting without any impossible days
def get_month():
    while True:
        month = input("Enter month (MM): ").zfill(2)
        if month.isdigit() and 1 <= int(month) <= 12:
            return month
        else:
            print("Invalid month.")

#Fucntion to get the day to add to month making sure it matches and is possible
def get_day(month):
    #variables for which months have which amount of days
    thirty_one = ["01", "03", "05", "07", "08", "10", "12"]
    thirty = ["04", "06", "09", "11"]

    while True:
        day = input("Enter day (DD): ").zfill(2)
        if not day.isdigit():
            print("Invalid day.")
            continue
        day_int = int(day)
        if month in thirty_one and 1 <= day_int <= 31:
            return day
        elif month in thirty and 1 <= day_int <= 30:
            return day
        elif month == "02" and 1 <= day_int <= 28:
            return day
        else:
            print("Invalid day for the month.")

#function gets year and makes sure it is valid
def get_year():
    while True:
        year = input("Enter year (YYYY): ")
        if year.isdigit() and len(year) == 4:
            return year
        else:
            print("Invalid year.")

#Puts month, year and day toghether
def get_date():
    month = get_month()
    day = get_day(month)
    year = get_year()
    return f"{month}/{day}/{year}"

#Function to get the amount needed of money
def get_amount():
    while True:
        try:
            return float(input("Enter amount: "))
        except:
            print("Not a valid number.")

#Main fucntion for this, asks all the questions and then puts them in the csv
def add_income():
    date = get_date()
    amount = get_amount()
    source = input("Enter income source (e.g., job, gift): ").strip()

    newData = pd.DataFrame([[date, amount, source]], columns=["date", "amount", "source"])
    newData.to_csv("user_income.csv", mode="a", index=False, header=False)
    print("Income added.\n")
