import pandas as pd
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="insurance_example"
)
cursor = conn.cursor(buffered=True)

travels_df = pd.read_csv("./csv_data/travel.csv")
revenues_df = pd.read_csv("./csv_data/agencies_revenues.csv")

product_category_mapping = {}

for index, row in travels_df.drop_duplicates().iterrows():
    cursor.execute(
        "INSERT INTO insurance_example.agencies_types (name) SELECT %s FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM insurance_example.agencies_types WHERE name = %s)",
        (row['Agency Type'], row['Agency Type'])
    )
    cursor.execute("SELECT id FROM agencies_types WHERE name = %s", (row['Agency Type'],))
    type_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO insurance_example.agencies (name, type_id) SELECT %s, %s FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM insurance_example.agencies WHERE name = %s AND type_id = %s)",
        (row['Agency'], type_id, row['Agency'], type_id)
    )
    cursor.execute("SELECT id FROM agencies WHERE name = %s", (row['Agency'],))
    agency_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO insurance_example.categories (name) SELECT %s FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM insurance_example.categories WHERE name = %s)",
        (row['Product Name'], row['Product Name'])
    )
    cursor.execute("SELECT id FROM insurance_example.categories WHERE name = %s", (row['Product Name'],))
    category_id = cursor.fetchone()[0]


    cursor.execute(
        "INSERT INTO insurance_example.products (name, category_id) SELECT %s, %s FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM insurance_example.products WHERE name = %s AND category_id = %s)",
        (row['Product Name'], category_id, row['Product Name'], category_id)
    )
    cursor.execute("SELECT id FROM products WHERE name = %s", (row['Product Name'],))
    product_id = cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO insurance_example.countries (name) SELECT %s FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM insurance_example.countries WHERE name = %s)",
        (row['Destination'], row['Destination'])
    )
    cursor.execute("SELECT id FROM countries WHERE name = %s", (row['Destination'],))
    country_id = cursor.fetchone()[0]

    if row['Distribution Channel'] == "Online" and row['Age'] > 18 and row['Age'] < 99 and abs(float(row['Net Sales'])) >= float(row['Commision (in value)']):
        cursor.execute(
            "INSERT INTO insurance_example.travels (agency_id, product_id, claim, country_id_of_destination, net_sales, commission, age, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (agency_id, product_id, row['Claim'], country_id, abs(float(row['Net Sales'])), float(row['Commision (in value)']), row['Age'], row['Date'])
        )

conn.commit()

# Insert data into 'agencies' table
for index, row in revenues_df.drop_duplicates().iterrows():
    # Get agency_id based on agency name
    cursor.execute(
        "SELECT id FROM insurance_example.agencies WHERE name = %s", (row["Agency"],)
    )
    agency_id = cursor.fetchone()[0] if cursor.rowcount > 0 else None

    if agency_id is not None:
        date = datetime.strptime(row["year_month"], "%Y-%m")

        # Insert data into 'agencies_revenues' table
        cursor.execute(
            "INSERT INTO insurance_example.agencies_revenues (`agency_id`, `year_month`, `total_income`, `expenses`) VALUES (%s, TIMESTAMP(%s), %s, %s)",
            (
                agency_id,
                date,
                float(row["total_income"]),
                float(row["expenses"]),
            ),
        )
conn.commit()

cursor.close()
conn.close()
