
from Expense import Expense


def main():
    file_path= "expense.csv"
    expense1 = get_data()
    expense_to_file(expense1 ,file_path)
    summarize(file_path)

    
def get_data():
    print("Getting User Input")
    print("Expense name: ")
    expense_name= input(">")
    print("Expense Cost: ")
    expense_cost= input(">")
    expense_category=[
        "Food",
        "Entertainment",
        "Work",
        "Misc",
    ]
        
    

    for i, value in enumerate(expense_category):
        print( f" {i+1}. {expense_category[i]}")
        i=i+1
    print("pick category [1,5]")
    selected_index= int(input(">"))
    # add conditional checking if input is valid later
    expense_cat= expense_category[selected_index-1]
    new_expense= Expense(name=expense_name,category=expense_cat, amount=expense_cost)
    return new_expense
def expense_to_file(expense: Expense, file_path):
    with open(file_path, 'a') as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    

def summarize(file_path):
    numb=0
    counter1=0
    counter2=0
    counter3=0
    counter4=0

    with open(file_path, 'r') as f:     #total amount spent 
        lines= f.readlines()
        for line in lines:
            split=line.split(",")
            numb= numb+ int(split[1])
            cate= (split[2]).strip()
            
            if cate== "Food":
                counter1= counter1+ int(split[1])
            if cate== "Entertainment":
                counter2= counter2+ int(split[1])
            if cate== "Work":
                counter3= counter3+ int(split[1])
            if cate== "Misc":
                counter4= counter4+ int(split[1])
   
    with open(file_path, "a") as f:
        f.write(f"Total: ${numb}\n")
    print("Expense by category")
    print(f"Food: $ {counter1}")
    print(f"Entertainment: ${counter2}")
    print(f"Work: ${counter3}")
    print(f"Misc: ${counter4}")
    #print(f"Total: {numb}")

if __name__=="__main__":
    main()    