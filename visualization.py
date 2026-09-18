import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import mysql.connector

conn=mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="expense_tracker"
)

cursor=conn.cursor()
cursor.execute("SELECT * FROM expenses")
data=cursor.fetchall()
df=pd.DataFrame(data,columns=["id","amount","category","date","payment_method","description"])

#Spending Over Time
df['date']=pd.to_datetime(df['date'])
daily_spending=df.groupby('date')['amount'].sum()
print("Daily Spending:",daily_spending)
plt.plot(daily_spending.index,daily_spending.values)
plt.title("Spending Over Time")
plt.xlabel("Date")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.show()

#Spending by Category and Payment Method
sns.barplot(data=df,x="category",y="amount",hue="payment_method")
plt.title("Spending by Category and Payment Method")
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.show()

#Monthly Spending
monthly_spending=df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
print("Monthly Spending:\n",monthly_spending)
plt.plot(monthly_spending.index.astype(str),monthly_spending.values)
plt.title("Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.show()
