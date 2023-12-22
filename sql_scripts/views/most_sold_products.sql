CREATE VIEW most_sold_products AS
SELECT products.id AS product_id,
       products.name AS product_name,
       products.main_category,
       products.sub_category,
       SUM(product_details.quantity) AS total_quantity_sold
FROM product_details
JOIN products ON product_details.products_id = products.id
GROUP BY product_id,
         product_name,
         main_category,
         sub_category
ORDER BY total_quantity_sold DESC
LIMIT 10;