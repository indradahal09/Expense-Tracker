import datetime
import json

expense_list = []
   

def Add_Expense():
    while True:
        try:
            expense = float(input("Enter expense amount:"))
            if(expense>0):
                break
            else:
                print("enter a positive number")
        except ValueError:
            print('enter a float value')


    category = input("Enter category:")
    description = input("Enter Description:")
    while True:
        try:
            date1 = input("enter date in YYYY-MM-DD format")
            year, month, day = map(int, date1.split("-"))
            date = datetime.date(year, month, day)
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    id = len(expense_list)+1
    expense_dict = {
        "Expense Amount": expense,
        "Category": category,
        "description": description,
        "date": date,
        "id": id
    }
    expense_list.append(expense_dict)
    save_expenses()
    print("Expense added successfully!")


def View_Expense():
    if(len(expense_list)==0):
        print("No expense to show")
    else:
        print("Id\tExpense\tCategory\tDescription\tdate")
        for i  in expense_list:
            print(f"{i["id"]}\t{i['Expense Amount']}\t{i['Category']}\t{i['description']}\t{i['date']}")

def search_expense():
    expense_category = input("enter the expense category")
    found = False
    print("Id\tExpense\tCategory\tDescription\tdate")
    for i in expense_list:
        if((i["Category"]).capitalize() == expense_category.capitalize()):
            print(f"{i["id"]}\t{i['Expense Amount']}\t{i['Category']}\t{i['description']}\t{i['date']}")
            found = True
    
    if(found == False):
        print("category not found")

def expense_summary():
    print("=================================")
    print("         Expnese Summary         ")
    print("=================================")
    total_expense = 0
    for i in expense_list:
        total_expense += i["Expense Amount"]

    number_of_expense = len(expense_list)
    if(number_of_expense == 0):
        print("no summary to show")
    else:
        avg_expense = total_expense / number_of_expense
        print("Total Expense:", total_expense)
        print("Number of expense:", number_of_expense)
        print("Average Expense:", avg_expense)

        max_amount = expense_list[0]["Expense Amount"]
        for i in expense_list:
            if(i["Expense Amount"] > max_amount):
                max_amount = i["Expense Amount"]
        print("Maximum expense:", max_amount)

        min_amount = expense_list[0]["Expense Amount"]
        for i in expense_list:
            if(min_amount > i["Expense Amount"]):
                min_amount = i["Expense Amount"]
        print("minimum amount:", min_amount)


def delete_expense():
    input_id = int(input("enter the id to delete"))
    found = False
    for i in expense_list:
        if(input_id == i['id']):
            found = True
            validation = input("do you want to delete it?")
            if(validation == "yes"):
                expense_list.remove(i)
                print("expense deleted")
                break
    if not found:
        print('id not matched')        

    new_id = 1
    for i in expense_list:
        i["id"]  = new_id
        new_id +=1

    save_expenses()

def save_expenses():
    explist_cpy = []
    for i in expense_list:
        dict = {
            'id': i['id'],
            'category': i['Category'],
            'expense amount': i['Expense Amount'],
            'description': i['description'],
            'date': datetime.datetime.strftime(i['date'], "%Y-%m-%d")
        }
        explist_cpy.append(dict)
    with open("expenses.json","w") as f:
        json.dump(explist_cpy,f)

def load_expenses():
    add_list = []
    try:
        with open('expenses.json','r') as f:
            data = json.load(f)
            for i in data:
                exp_dict = {
                    'id': i['id'],
                    'category': i['Category'],
                    'expense amount': i['Expense Amount'],
                    'description': i['description'],
                    'date': datetime.datetime.strptime(i['date'], "%Y-%m-%d").date()
                }
                add_list.append(exp_dict)
    except FileNotFoundError:
        return []
    
    return add_list


expense_list = load_expenses()
print(expense_list)


print("=================================")
print("         Expnese Tracker         ")
print("=================================")


User_Choice_loop = True
while User_Choice_loop:
    print("click \n1.Add Expense")
    print("2.View Expense")
    print("3.Search Expense")
    print("4.Expense Summary")
    print("5.Delete Expense")
    print("6.Exit")

    User_Choice = None
    while True:
        try:
            User_Choice = int(input("Enter a number from 1 to 6"))
            if(User_Choice >=1 and User_Choice<=6):
                break
            else:
                print("enter number between 1 to 6")
                
        except ValueError:
            print("please input a number")
        
   
    if(User_Choice == 1):
        Add_Expense()
    elif(User_Choice == 2):
        View_Expense()
    elif(User_Choice == 3):
        search_expense()
    elif(User_Choice == 4):
        expense_summary()
    elif(User_Choice == 5):
        delete_expense()
    elif(User_Choice == 6):
        break
        
    
