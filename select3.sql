SELECT
    U.username,
    O.order_id,
    O.order_date,
    O.status AS order_status,
    P.product_name,
    OI.quantity,
    OI.unit_price
FROM 
    user U
JOIN 
    `order` O ON U.user_id = O.user_id
JOIN 
    order_item OI ON O.order_id = OI.order_id
JOIN 
    product P ON OI.product_id = P.product_id
WHERE 
    U.user_id = 1 -- 鎖定特定用戶 (Alice)
ORDER BY 
    O.order_id DESC, OI.order_item_id ASC;