import pandas as pd
import sqlite3

orders = pd.read_csv("orders.csv")
users = pd.read_json("users.json")

conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()

with open("restaurants.sql", "r", encoding="utf-8") as f:
    sql = f.read()

cursor.executescript(sql)
conn.commit()

restaurants = pd.read_sql_query(
    "SELECT * FROM restaurants",
    conn
)

final_df = pd.merge(orders, users, on="user_id", how="left")
final_df = pd.merge(final_df, restaurants, on="restaurant_id", how="left")

final_df.to_csv("final_food_delivery_dataset.csv", index=False)

conn.close()