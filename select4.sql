SELECT
    P.product_id,
    P.product_name,
    P.stock_quantity,
    C.category_name
FROM
    product P
JOIN
    category C ON P.category_id = C.category_id
WHERE
    P.stock_quantity < 50
ORDER BY
    P.stock_quantity ASC;