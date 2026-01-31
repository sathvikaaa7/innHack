import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")

df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

distinct_users = df['user_id'].nunique()
print("Distinct users", distinct_users)

gold_df = df[df['membership'] == 'Gold']
gold_aov = round(gold_df['total_amount'].mean(), 2)
print("Gold member AOV:", gold_aov)

high_rating_orders = df[df['rating'] >= 4.5].shape[0]
print(">= 4.5", high_rating_orders)

gold_city_revenue = (
    gold_df.groupby('city')['total_amount']
    .sum()
    .sort_values(ascending=False)
)

top_city = gold_city_revenue.index[0]
print("top gold revenue city", top_city)
orders_in_top_city = gold_df[gold_df['city'] == top_city].shape[0]
print("Gold orders highst", orders_in_top_city)

total_gold_orders = gold_df.shape[0]
print("Total gold orders", total_gold_orders)

hyd_revenue = round(
    df[df['city'] == 'Hyderabad']['total_amount'].sum()
)
print("Hyderabad revenue", hyd_revenue)