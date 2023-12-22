CREATE VIEW
    sales_by_discount AS
SELECT
    products.discount_price IS NOT NULL AS is_discounted,
    COUNT(sales.id) AS total_sales
FROM
    sales
    JOIN product_details ON sales.id = product_details.sales_id
    JOIN products ON product_details.products_id = products.id
GROUP BY
    is_discounted;