CREATE VIEW
    `turnover_per_year` AS
SELECT
    YEAR (`date`) AS `year`,
    SUM(`actual_price` * `quantity`) AS `turnover`
FROM
    `si`.`sales`
    JOIN `si`.`product_details` ON `si`.`sales`.`id` = `si`.`product_details`.`sales_id`
    JOIN `products` ON `si`.`product_details`.`products_id` = `products`.`id`
GROUP BY
    YEAR (`date`)
ORDER BY
    `year`;