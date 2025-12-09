SELECT
    U.username,
    U.email,
    SUM(O.total_amount) AS total_spent_amount,
    COUNT(O.order_id) AS total_orders
FROM 
    user U
JOIN 
    `order` O ON U.user_id = O.user_id
WHERE 
    O.status = 'Completed' -- 僅計算完成的訂單金額
GROUP BY
    U.user_id, U.username, U.email
ORDER BY 
    total_spent_amount DESC
LIMIT 
    10; -- 顯示前 10 名