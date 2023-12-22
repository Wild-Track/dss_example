CREATE VIEW
    top_agencies_profit AS
SELECT
    a.name AS agency_name,
    SUM(ar.total_income - ar.expenses) AS profit
FROM
    agencies AS a
    INNER JOIN agencies_revenues AS ar ON a.id = ar.agency_id
GROUP BY
    a.id
ORDER BY
    profit DESC
LIMIT
    10;