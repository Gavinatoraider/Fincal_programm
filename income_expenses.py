def income_expenses():

    def add_income():
        def get_date():
            
            thirty_one = ["01", "03", "05", "07", "08", "10", "12"]
            thirty = ["04", "06", "09", "11"]

            
            
            def get_month():
                month = input("What month did you get the income(Cant be less than 0 or greater than 12(MM format)): ")

                try:
                    int(month)
                except:
                    print("Not a Number")
                    get_month()

                if month < 1 or month > 12:
                    print("Not a Valid Month!")
                    get_month()

                return month
            
            def get_day(month):
                day = input("What day did you get the income(Has to be a day in the month): ")

                try:
                    int(day)
                except:
                    print("Not a Number")
                    get_day()
                
                
                if month in thirty_one:
                    if day > 31 or day < 0:
                        print("Not a Valid Day")
                        get_day()
                elif month in thirty:
                    if day > 30 or day < 0:
                        print("Not a Valid Day")
                        get_day()
                elif month == "02":
                    if day > 28 or day < 0:
                        print("Not a Valid Day")
                        get_day()
                
                return day

            def get_year():
                pass


            month = get_month()
            day = get_day(month)
            year = get_year()
        
        get_date()
        with open("user_income.csv", "a"):
            pass
    
    
    
    
    
    print("""
    Income Expenses Choices
    1. Add Income Entires
    2. Add Expense Entries
    3. View Income and Expenses
    4. Exit""")

    choice = input("Choose a Number: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    else:
        print("Not a Choice!")
        income_expenses()