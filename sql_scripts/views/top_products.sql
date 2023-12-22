CREATE VIEW
    top_products AS
SELECT
    p.name AS product,
    SUM(t.net_sales) AS total_sales
FROM
    travels t
    JOIN products p ON t.product_id = p.id
GROUP BY
    p.name
ORDER BY
    total_sales DESC
LIMIT
    10;