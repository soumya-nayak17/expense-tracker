import mysql.connector
conn=mysql.connector.connect(
host="localhost",
user="root",
password="YOUR_PASSWORd",
database="expense_tracker"
 )

if conn.is_connected():
    print("Connected successfully")
    while True:
        print("\n1.Add Expense\n2.View Expense\n3.Delete Expense\n4.Exit\n")
        choice=int(input("Enter your choice:"))
        if choice==1: 
            amount=float(input("Enter the amount:"))
            category = input("Enter category:")
            date = input("Enter date(YYYY-MM-DD):")
            description = input("Enter description:")
            cursor = conn.cursor()
            query = "INSERT INTO expenses (amount,category,date,description) VALUES (%s,%s,%s,%s)" 
            values=(amount,category,date,description)
            cursor.execute(query,values)
            conn.commit()
            print("Expense added successfully")
        
        elif choice==2:
            cursor=conn.cursor()
            query="SELECT * from expenses;"
            cursor.execute(query) 
            data=cursor.fetchall()
            if data==[]:
                print("No expenses to view")
            else:
                for row in data:
                    print(f"Id:{row[0]},amount:{row[1]},category:{row[2]},date:{row[3]},description:{row[4]}")


        elif choice==3:
            inp_id=int(input("Enter ID to delete the data:"))
            cursor=conn.cursor()
            query="DELETE FROM expenses WHERE id=%s;"
            cursor.execute(query,(inp_id,))
            conn.commit()
            print("Expense deleted successfully")

        elif choice==4:
            print("Exiting..")
            break

        else:
            print("Invalid option,please enter valid option")

else:
    print("Connection failed")