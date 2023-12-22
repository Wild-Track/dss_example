CREATE VIEW
    age_per_destination AS
SELECT
    c.name AS destination,
    t.age AS most_common_age,
    COUNT(*) AS age_count
FROM
    insurance_example.travels t
    JOIN insurance_example.countries c ON t.country_id_of_destination = c.id
GROUP BY
    c.name,
    t.age
ORDER BY
    c.name,
    age_count DESC;