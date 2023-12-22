CREATE VIEW
    top_clients AS
SELECT
    clients.id AS client_id,
    clients.country,
    SUM(products.actual_price * product_details.quantity) AS total_turnover
FROM
    clients
    JOIN sales ON clients.id = sales.clients_id
    JOIN product_details ON sales.id = product_details.sales_id
    JOIN products ON product_details.products_id = products.id
GROUP BY
    client_id,
    clients.country
ORDER BY
    total_turnover DESC
LIMIT
    10;