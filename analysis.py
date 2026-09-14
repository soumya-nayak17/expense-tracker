import mysql.connector
import pandas as pd

conn=mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="expense_tracker"
 )

cursor=conn.cursor()
cursor.execute("SELECT * FROM expenses")
data=cursor.fetchall()
df=pd.DataFrame(data,columns=["id","amount","category","date","description"])
print(df)

no_of_expns=len(df)
print("Number Of Expenses:",no_of_expns)

total_spending=df["amount"].sum()
print("Total Spending:",total_spending)

avg_expns=df["amount"].mean()
print("Average Expense:",avg_expns)

high_expns=df["amount"].max()
print("Highest Expense:",high_expns)

low_expns=df["amount"].min()
print("Lowest Expense:",low_expns)

cat_spending=df.groupby("category")["amount"].sum()
print("Spending by Category:\n",cat_spending)

high_category=cat_spending.idxmax()
high_cat_amt=cat_spending.max()
print("Highest spending category:",high_category)
print("Highest category amount:",high_cat_amt)

low_category=cat_spending.idxmin()
low_cat_amt=cat_spending.min()
print("Lowest spending category:",low_category)
print("Lowest category amount:",low_cat_amt)

df["date"]=pd.to_datetime(df["date"])
monthly_spending=df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
print("Monthly Spending:\n",monthly_spending)

print("Basic Statistics:\n",df["amount"].describe())