CREATE VIEW
    sales_by_country AS
SELECT
    clients.country,
    COUNT(sales.id) AS total_sales
FROM
    clients
    JOIN sales ON clients.id = sales.clients_id
GROUP BY
    clients.Country;