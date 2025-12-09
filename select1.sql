SELECT
    C.category_name,
    -- 計算該分類在已完成訂單中的總銷售額
    SUM(OI.quantity * OI.unit_price) AS total_sales_amount, 
    -- 計算該分類下所有商品的平均定價
    AVG(P.price) AS average_product_price 
FROM 
    category C
JOIN 
    product P ON C.category_id = P.category_id
JOIN 
    order_item OI ON P.product_id = OI.product_id
JOIN 
    `order` O ON OI.order_id = O.order_id
WHERE 
    O.status = 'Completed' -- 只計算已完成的訂單
GROUP BY 
    C.category_name
ORDER BY 
    total_sales_amount DESC;