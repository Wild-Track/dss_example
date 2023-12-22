CREATE VIEW total_sales_indicator AS
SELECT COUNT(id) AS total_sales
FROM sales;


CREATE VIEW total_turnover_indicator AS
SELECT SUM(products.actual_price * product_details.quantity) AS total_turnover
FROM product_details
JOIN products ON product_details.products_id = products.id;


CREATE VIEW total_clients_indicator AS
SELECT COUNT(id) AS total_clients
FROM clients;


CREATE VIEW total_products_indicator AS
SELECT COUNT(DISTINCT id) AS total_products
FROM products;


CREATE VIEW avg_sales_turnover_indicator AS
SELECT AVG(products.actual_price * product_details.quantity) AS avg_sales_turnover
FROM product_details
JOIN products ON product_details.products_id = products.id;


CREATE VIEW avg_products_per_order_indicator AS
SELECT AVG(product_details.quantity) AS avg_products_per_order
FROM product_details;


CREATE VIEW avg_sales_per_client_indicator AS
SELECT clients.id AS client_id,
       AVG(products.actual_price * product_details.quantity) AS avg_sales_amount
FROM clients
JOIN sales ON clients.id = sales.clients_id
JOIN product_details ON sales.id = product_details.sales_id
JOIN products ON product_details.products_id = products.id
GROUP BY client_id;


CREATE VIEW avg_products_per_sale_indicator AS
SELECT AVG(product_details.quantity) AS avg_products_per_sale
FROM product_details;

CREATE VIEW std_dev_product_prices_indicator AS
SELECT STDDEV(products.actual_price) AS std_dev_product_prices
FROM products;