import pandas as pd
import plotly.express as px
import plotly.io as pio
from sqlalchemy import create_engine

db_infos = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "port": "3306",
    "database": "si",
}
conn = create_engine(
    f"mysql+mysqlconnector://{db_infos['user']}:{db_infos['password']}@{db_infos['host']}:{db_infos['port']}/{db_infos['database']}"
)

# region turnover_per_year
query = "SELECT * FROM turnover_per_year"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="year",
    y="turnover",
    title="Turnover per year",
    labels={"turnover": "Turnover", "year": "Year"},
)

pio.write_image(fig, "./images/turnover_per_year.png")
# endregion --------------------------------------

# region top_clients
query = "SELECT * FROM top_clients"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="client_id",
    y="total_turnover",
    title="Top 10 Clients - Turnover per client",
    labels={"total_turnover": "Turnover", "client_id": "Client ID"},
    barmode="relative",
)

fig.update_xaxes(type="category")

pio.write_image(fig, "./images/top_clients_turnover.png")
# endregion --------------------------------------

# region top_countries
query = "SELECT * FROM top_countries"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="country",
    y="total_turnover",
    title="Top 10 Countries - Turnover per country",
    labels={"total_turnover": "Turnover", "country": "Country"},
    barmode="relative",
)

pio.write_image(fig, "./images/top_countries_turnover.png")
# endregion --------------------------------------

# region most_sold_products
query = "SELECT * FROM most_sold_products"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="product_id",
    y="total_quantity_sold",
    title="Top 10 Products - Total quantity sold",
    labels={"total_quantity_sold": "Total quantity sold", "product_id": "Product ID"},
    barmode="relative",
)

fig.update_xaxes(type="category")

pio.write_image(fig, "./images/most_sold_products.png")
# endregion --------------------------------------

# region sales_by_category
query = "SELECT * FROM sales_by_category"
df = pd.read_sql(query, conn)

fig = px.pie(
    df,
    names="main_category",
    values="total_quantity_sold",
    labels={
        "main_category": "Main category",
    },
    title="Sales by main category",
)

pio.write_image(fig, "./images/sales_by_category_pie.png")
# endregion --------------------------------------

# region sales_by_country
query = "SELECT * FROM sales_by_country"
df = pd.read_sql(query, conn)

fig = px.pie(
    df,
    names="country",
    values="total_sales",
    labels={
        "country": "Country",
    },
    title="Number of sales per country",
)

pio.write_image(fig, "./images/sales_by_country_pie.png")
# endregion --------------------------------------

# region sales_by_discount
query = "SELECT * FROM sales_by_discount"
df = pd.read_sql(query, conn)

df["is_discounted_label"] = df["is_discounted"].map({1: "discounted", 0: "regular"})

fig = px.pie(
    df,
    names="is_discounted_label",
    values="total_sales",
    title="Number of sales (discount vs normal price)",
    labels={"is_discounted_label": "Type of sale"},
)

pio.write_image(fig, "./images/sales_by_discount_pie.png")
# endregion --------------------------------------

# region KPI
query_sales = "SELECT * FROM total_sales_indicator"
query_turnover = "SELECT * FROM total_turnover_indicator"
query_clients = "SELECT * FROM total_clients_indicator"

query_avg_sales_turnover = "SELECT * FROM avg_sales_turnover_indicator"
query_avg_products_per_order = "SELECT * FROM avg_products_per_order_indicator"

query_std_dev_product_prices = "SELECT * FROM std_dev_product_prices_indicator"

total_sales = pd.read_sql(query_sales, conn)["total_sales"].iloc[0]
total_turnover = pd.read_sql(query_turnover, conn)["total_turnover"].iloc[0]
total_clients = pd.read_sql(query_clients, conn)["total_clients"].iloc[0]

avg_sales_turnover = pd.read_sql(query_avg_sales_turnover, conn)[
    "avg_sales_turnover"
].iloc[0]
avg_products_per_order = pd.read_sql(query_avg_products_per_order, conn)[
    "avg_products_per_order"
].iloc[0]

std_dev_product_prices = pd.read_sql(query_std_dev_product_prices, conn)[
    "std_dev_product_prices"
].iloc[0]

print(f"Total number of sales : {total_sales}")
print(f"Total turnover : {total_turnover:.2f}")
print(f"Total number of clients : {total_clients}")

print(f"Average sales turnover : {avg_sales_turnover:.2f}")
print(f"Average number of products in orders : {avg_products_per_order:.2f}")

print(f"Price gap of sold products : {std_dev_product_prices:.2f}")
# endregion --------------------------------------

# Close the database connection
conn.dispose()
