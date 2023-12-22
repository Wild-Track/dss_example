CREATE VIEW
    top_categories AS
SELECT
    c.name AS category,
    SUM(t.net_sales) AS total_sales
FROM
    travels t
    JOIN products p ON t.product_id = p.id
    JOIN categories c ON p.category_id = c.id
GROUP BY
    c.name
ORDER BY
    total_sales DESC
LIMIT
    10;