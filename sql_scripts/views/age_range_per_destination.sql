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
