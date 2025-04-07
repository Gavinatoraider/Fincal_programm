#gavin pierce income page

def expence_add(): #adds income entry
                month = input("what is the month of the income entry? (it needs to be the number of the month ex: 1 = january, or 8 = october)") #adds month
                int(month)
                if month <1:
                        print("you need a valid month.")
                elif month > 12:
                        print("you need a valid month")
                else:
                        print("you need to give a number for the month")

                day = input("what is the day of the income entry (ex: 1 = monday 5 = friday)") #adds day
                int(day)
                if day <1:
                        print("you need a valid day")
                elif day > 7:
                        print("you need a valid day")
                else:
                        print("you need a valid number")
                year = input("what is the year of the income entry (the cut off year is 1600 and 2100)") #adds day
                int(year)
                if year <1600:
                        print("you need a valid year.")
                elif year > 2100:
                        print("you need a valid year.")
                else print()

                int(day)
                if day <1:
                        print("you need a valid day")
                elif day > 7:
                        print("you need a valid day")
                else:
                        print("you need a valid number")

                amount=input("what is the amount of the income entry") #adds amount
                source=input("what is the source of the income entry") #adds sourse
                print("so the day of the income entry is ", date , " the amount is ", amount , " and the sorce is " , source ".")

def expence_subtract():
                month = input("what is the month of the income expence? (it needs to be the number of the month ex: 1 = january, or 8 = october)") #adds month
                int(month)
                if month <1:
                        print("you need a valid month.")
                elif month > 12:
                        print("you need a valid month")
                else:
                        print("you need to give a number for the month")

                day = input("what is the day of the expence entry (ex: 1 = monday 5 = friday)") #adds day
                int(day)
                if day <1:
                        print("you need a valid day")
                elif day > 7:
                        print("you need a valid day")
                else:
                        print("you need a valid number")

                year = input("what is the year of the entry")
                amount=input("what is the amount of the expence entry") #adds amount
                source=input("what is the source of the expence entry") #adds sourse
                print("so the day of the expence entry is ", date , " the amount is ", amount , " and the sorce is " , source ".")

def view_time_span():
        time_to_view
        

def income_expences():
    print("welcome to the income and expenses.")
    while True:
        to_do=("""what would you like to do?
               1. add an income entry
               2. add an expence entry
               3. View total expencese for a certain time fram? """)
        if to_do=="1":
           expence_add()
        elif to_do== "2":
            expence_subtract()
        elif 
        

