import pandas as pd
import plotly.express as px
import plotly.io as pio
from sqlalchemy import create_engine

db_infos = {
    "user": "root",
    "password": "root",
    "host": "localhost",
    "port": "3306",
    "database": "insurance_example",
}
conn = create_engine(
    f"mysql+mysqlconnector://{db_infos['user']}:{db_infos['password']}@{db_infos['host']}:{db_infos['port']}/{db_infos['database']}"
)


# region top_agencies
query = "SELECT * FROM top_agencies"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="agency",
    y="total_turnover",
    title="Top agencies",
    labels={"agency": "Agency", "total_turnover": "Total turnover"},
)

pio.write_image(fig, "./images/top_agencies.png")
# endregion --------------------------------------

# region top_products
query = "SELECT * FROM top_products"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="product",
    y="total_sales",
    title="Top products",
    labels={"product": "Product", "total_sales": "Total turnover by sales"},
)

pio.write_image(fig, "./images/top_products.png")
# endregion --------------------------------------

# region top_categories
query = "SELECT * FROM top_categories"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="category",
    y="total_sales",
    title="Top categories",
    labels={"category": "Category", "total_sales": "Total turnover by sales"},
)

pio.write_image(fig, "./images/top_categories.png")
# endregion --------------------------------------

# # region age_range_per_destination
query = "SELECT * FROM age_range_per_destination"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="age_range",
    y="age_count",
    color="destination",
    title="Age Distribution per Destination",
    labels={"age_range": "Age range", "age_count": "Age count", "destination": "Destination"},
)

fig.update_layout(barmode="stack", legend = dict(font = dict(size = 10, color = "black")))

pio.write_image(fig, "./images/age_range_per_destination.png")
# endregion --------------------------------------

# region age_per_destination
query = "SELECT * FROM age_per_destination"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="most_common_age",
    y="age_count",
    color="destination",
    title="Age Distribution per Destination",
    labels={"most_common_age": "Most Common Age", "age_count": "Occurrence", "destination": "Destination"},
)

fig.update_layout(barmode="stack", legend = dict(font = dict(size = 10, color = "black")))

pio.write_image(fig, "./images/age_per_destination.png")
# endregion --------------------------------------

# region income_per_age_range
query = "SELECT * FROM income_per_age_range"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="age_range",
    y="average_income",
    title="Average income per age range",
    labels={"age_range": "age range", "average_income": "Average income"},
)

pio.write_image(fig, "./images/income_per_age_range.png")
# endregion --------------------------------------

# region top_destinations_per_month
query = "SELECT * FROM top_destinations_per_month"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="month",
    y="total_sales",
    color="destination",
    title="top_destinations_per_month",
    labels={"agency": "Agency", "total_turnover": "Total turnover"},
)

pio.write_image(fig, "./images/top_destinations_per_month.png")
# endregion --------------------------------------

# region top_agencies_profit
query = "SELECT * FROM top_agencies_profit"
df = pd.read_sql(query, conn)

fig = px.bar(
    df,
    x="agency_name",
    y="profit",
    title="Top agencies profit",
    labels={"agency_name": "Agency", "profit": "Profit"},
)

pio.write_image(fig, "./images/top_agencies_profit.png")
# endregion --------------------------------------


# Close the database connection
conn.dispose()
