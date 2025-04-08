categories = ["housing", "transportation", "food", "utility", "clothing", "medical", "insurance", "household", "personal", "debt", "education", "saving", "gift", "entertainment", "other"]

#Done by Asher

def budget(total_income):
    
    def set_budget(total_income):
        limits = {}
        for i in categories:
            limit_choice = input(f"What percent of your income do you want {i} limits to be?(Leave Blank To Not Use): ")
            try:
                limit_choice = (int(limit_choice)/100)*total_income
            except:
                print("Not A Number")
                set_budget()
            limits[i] = limit_choice
        return limits
    
    print("""
    Budget Choices
    1. Set Budget Limit
    2. Exit""")

    budget_choice = input("Choose a Number: ")

    if budget_choice == "1":
        set_budget()
    elif budget_choice == "2":
        return
    else:
        print("Not an Option!")
        budget()