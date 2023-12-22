import pandas as pd
import mysql.connector
import math
import json

# region Import Data

# Setup connection to MySQL database
conn = mysql.connector.connect(
    host="localhost", port="3306", user="root", password="root", database="si"
)
cursor = conn.cursor()

# Read CSV files
clients_df = pd.read_csv("./csv_data/clients.csv")
sales_df = pd.read_csv("./csv_data/sales.csv")
products_df = pd.read_csv("./csv_data/data.csv")

# Drop duplicates
products_df = products_df.drop_duplicates(subset=["name", "main_category", "sub_category", "image", "ratings", "no_of_ratings", "discount_price", "actual_price"])

# Insert data into 'clients' table
for index, row in clients_df.iterrows():
    cursor.execute(
        "INSERT INTO clients (id, country) VALUES (%s, %s)",
        (int(row["Id"]), row["country"]),
    )
conn.commit()

# Insert data into 'products' table
for index, row in products_df.iterrows():
    try:
        if math.isnan(float(row["discount_price"])):
            discount_price = None
    except (ValueError, AttributeError):
        discount_price = float(row["discount_price"][1:].replace(",", ""))

    try:
        if math.isnan(float(row["actual_price"])):
            actual_price = None
    except (ValueError, AttributeError):
        actual_price = float(row["actual_price"][1:].replace(",", ""))

    if math.isnan(float(row["ratings"])):
        ratings = None
    else:
        ratings = float(row["ratings"])

    try:
        if math.isnan(float(row["no_of_ratings"])):
            no_of_ratings = None
    except (ValueError, AttributeError):
        no_of_ratings = int(row["no_of_ratings"].replace(",", ""))

    cursor.execute(
        "INSERT INTO products (id, name, main_category, sub_category, image, link, rating, nb_rating, discount_price, actual_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            int(row["Id"]),
            row["name"],
            row["main_category"],
            row["sub_category"],
            row["image"],
            row["link"],
            ratings,
            no_of_ratings,
            discount_price,
            actual_price,
        ),
    )
conn.commit()

# Insert data into 'sales' table
for index, row in sales_df.iterrows():
    try:
        cursor.execute(
            "INSERT INTO sales (id, date, is_discount, clients_id) VALUES (%s, %s, %s, %s)",
            (
                int(row["Id"]),
                row["date"],
                int(row["is_discounted"]),
                int(row["client_id"]),
            ),
        )
    except Exception:
        pass
conn.commit()

# Insert data into 'product_details' table
for index, row in sales_df.iterrows():
    product_ids = json.loads(row['products'])
    for product_id in set(product_ids):
        quantity = product_ids.count(product_id)
        try:
            cursor.execute(
                "INSERT INTO product_details (sales_id, products_id, quantity) VALUES (%s, %s, %s)",
                (int(row["Id"]), int(product_id), int(quantity)),
            )
        except Exception:
            pass
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

# endregion Import Data
