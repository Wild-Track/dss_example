CREATE VIEW
    top_agencies AS
SELECT
    a.name AS agency,
    SUM(t.net_sales) AS total_turnover
FROM
    travels t
    JOIN agencies a ON t.agency_id = a.id
GROUP BY
    a.name
ORDER BY
    total_turnover DESC
LIMIT
    10;