CREATE VIEW top_agencies AS
SELECT a.name AS agency, SUM(t.net_sales) AS total_turnover
FROM travels t
JOIN agencies a ON t.agency_id = a.id
GROUP BY a.name
ORDER BY total_turnover DESC
LIMIT 10;

CREATE VIEW top_products AS
SELECT p.name AS product, SUM(t.net_sales) AS total_sales
FROM travels t
JOIN products p ON t.product_id = p.id
GROUP BY p.name
ORDER BY total_sales DESC
LIMIT 10;

CREATE VIEW top_categories AS
SELECT c.name AS category, SUM(t.net_sales) AS total_sales
FROM travels t
JOIN products p ON t.product_id = p.id
JOIN categories c ON p.category_id = c.id
GROUP BY c.name
ORDER BY total_sales DESC
LIMIT 10;

CREATE VIEW age_range_per_destination AS
SELECT
    c.name AS destination,
    CASE
        WHEN t.age BETWEEN 0 AND 18 THEN '0-18'
        WHEN t.age BETWEEN 19 AND 30 THEN '19-30'
        WHEN t.age BETWEEN 31 AND 40 THEN '31-40'
        WHEN t.age BETWEEN 41 AND 50 THEN '41-50'
        WHEN t.age BETWEEN 51 AND 60 THEN '51-60'
        ELSE '61+'
    END AS age_range,
    COUNT(*) AS age_count
FROM
    insurance_example.travels t
JOIN
    insurance_example.countries c ON t.country_id_of_destination = c.id
GROUP BY
    c.name, age_range
ORDER BY
    c.name, age_range;

CREATE VIEW age_per_destination AS
SELECT
    c.name AS destination,
    t.age AS most_common_age,
    COUNT(*) AS age_count
FROM
    insurance_example.travels t
JOIN
    insurance_example.countries c ON t.country_id_of_destination = c.id
GROUP BY
    c.name, t.age
ORDER BY
    c.name, age_count DESC;

CREATE VIEW income_per_age_range AS
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        WHEN age BETWEEN 56 AND 65 THEN '56-65'
        ELSE '65+'
    END AS age_range,
    AVG(net_sales) AS average_income
FROM travels
GROUP BY age_range;

CREATE VIEW top_destinations_per_month AS
SELECT 
    c.name AS destination, 
    DATE_FORMAT(t.date, '%Y-%m') AS month,
    SUM(t.net_sales) AS total_sales
FROM travels t
JOIN countries c ON t.country_id_of_destination = c.id
GROUP BY destination, month
ORDER BY total_sales DESC
LIMIT 10;
