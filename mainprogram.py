from datetime import datetime
import mysql.connector
conn=mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="expense_tracker"
 )

def get_payment_method():
    while True:
            payment_method=input("Enter payment method(Cash/UPI/Card):").strip().lower()
            if payment_method == "cash":
                return "Cash"
            elif payment_method == "upi":
                return "UPI"
            elif payment_method == "card":
                return "Card"
            else:
                print("Invalid payment method. Please enter Cash, UPI, or Card.")

def get_category():
    while True:
            category = input("Enter category:").strip().lower()
            if category:
                return category.capitalize()
            else:
                print("Category cannot be empty. Please enter a category")

def display_expenses(data):
    if data==[]:
            print("No expenses to view")
    else:
        for row in data:
            print(f"Id:{row[0]},amount:{row[1]},category:{row[2]},date:{row[3]},payment_method:{row[4]},description:{row[5]}")
    
def add_expense():
    while True:
        try:
            amount=float(input("Enter the amount:"))
            if amount<=0:
                print("Enter valid amount")
                continue
            break
        except ValueError:
            print("Invalid input!! Please try again")
            continue
    category =get_category()
    while True:
        try:
            date = input("Enter date(YYYY-MM-DD):")
            valid_date=datetime.strptime(date,"%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format or real date.Please use YYYY-MM-DD.")  
            continue
    payment_method=get_payment_method()
    description = input("Enter description:")
    cursor = conn.cursor()
    query = "INSERT INTO expenses (amount,category,date,payment_method,description) VALUES (%s,%s,%s,%s,%s)" 
    values=(amount,category,date,payment_method,description)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    print("Expense added successfully")

def view_expense():
    cursor=conn.cursor()
    query="SELECT * from expenses;"
    cursor.execute(query) 
    data=cursor.fetchall()
    cursor.close()
    display_expenses(data)

def update_expense():
    while True:
        try:
            upd_id=int(input("Enter the ID to update the data:"))   
            if upd_id<=0:
                print("Invalid ID! Please try again") 
                continue
            break
        except ValueError:
            print("Try again and enter valid ID")
            continue   
    cursor=conn.cursor()
    query="SELECT EXISTS(SELECT 1 FROM expenses WHERE ID=%s)"
    cursor.execute(query,(upd_id,))
    result=cursor.fetchone()
    if result[0]==1:
        while True:
                try:
                    upd_amt=float(input("Enter the new amount:"))
                    if upd_amt<=0:
                        print("Enter valid amount")
                        continue
                    break
                except ValueError:
                    print("Invalid input!! Please try again")
                    continue
        upd_cat=get_category()
        while True:
            try:
                upd_date=input("Enter new date:")
                valid_date=datetime.strptime(upd_date,"%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format or real date.Please use YYYY-MM-DD.")  
                continue    
        new_paymeth=get_payment_method()
        upd_des=input("Enter new description:")
        query="UPDATE expenses SET amount=%s,category=%s,date=%s,payment_method=%s,description=%s WHERE id=%s"
        values=(upd_amt,upd_cat,upd_date,new_paymeth,upd_des,upd_id)
        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        print("Update Successful")
    else:
        cursor.close()
        print("ID doesn't exist")
        return

def delete_expense():
    while True:
            try:
                inp_id=int(input("Enter the ID to delete the data:"))   
                if inp_id<=0:
                    print("Invalid ID! Please try again") 
                    continue
                break
            except ValueError:
                print("Try again and enter valid ID")
                continue    
    cursor=conn.cursor()
    query="SELECT EXISTS(SELECT 1 FROM expenses WHERE ID=%s)"
    cursor.execute(query,(inp_id,))
    result=cursor.fetchone()
    if result[0]==1:
        query="DELETE FROM expenses WHERE id=%s;"
        cursor.execute(query,(inp_id,))
        conn.commit()
        cursor.close()
        print("Expense deleted successfully")
    else:
        cursor.close()
        print("ID doesn't exist")

def search_expense():
    print("1.Search by category\n2.Search by Date\n3.View all")
    user_input=int(input("Enter your option:"))
    if user_input==1:
        while True:
                cat_input = input("Enter category:").strip()
                if cat_input:
                    break
                else:
                    print("Category cannot be empty.Please enter a category.")
        cursor=conn.cursor()
        query="SELECT * FROM expenses WHERE category=%s"
        value=(cat_input,)
        cursor.execute(query,value)
        result=cursor.fetchall()
        cursor.close()
        display_expenses(result)
        
    elif user_input==2:
        while True:
            try:
                date_input=input("Enter date(YYYY-MM-DD):")
                valid_date=datetime.strptime(date_input,"%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format or real date.Please use YYYY-MM-DD.")  
                continue
        cursor=conn.cursor()
        query="SELECT * FROM expenses WHERE date=%s"
        value=(date_input,)
        cursor.execute(query,value)
        result=cursor.fetchall()
        cursor.close()
        display_expenses(result)

    elif user_input==3:
        cursor=conn.cursor()
        query="SELECT * FROM expenses"
        cursor.execute(query)
        result=cursor.fetchall()
        cursor.close()
        display_expenses(result)
    else:
        print("Invalid option, please try again!")        
 
if conn.is_connected():
    print("Connected successfully")
    while True:
        print("\n1.Add Expense\n2.View Expense\n3.Update Expense\n4.Delete Expense\n5.Search Expense\n6.Exit\n")
        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            print("Invalid input! Enter integer")
            continue
        if choice==1: 
            add_expense()
        
        elif choice==2:
            view_expense()

        elif choice==3:
            update_expense()

        elif choice==4:
            delete_expense()

        elif choice==5:
            search_expense()

        elif choice==6:
            print("Exiting..")
            conn.close()
            break

        else:
            print("Invalid option, please enter valid option!")

else:
    print("Connection failed") 