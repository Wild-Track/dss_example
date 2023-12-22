CREATE VIEW
    top_selling_country_per_month AS
SELECT
    c.name AS country,
    DATE_FORMAT (t.date, '%Y-%m') AS month,
    COUNT(*) AS sales_count
FROM
    insurance_example.travels t
    JOIN insurance_example.countries c ON t.country_id_of_destination = c.id
GROUP BY
    c.name,
    DATE_FORMAT (t.date, '%Y-%m')
ORDER BY
    sales_count DESC;