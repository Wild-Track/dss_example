CREATE VIEW sales_by_category AS
SELECT products.main_category,
       SUM(product_details.quantity) AS total_quantity_sold
FROM product_details
JOIN products ON product_details.products_id = products.id
GROUP BY products.main_category;