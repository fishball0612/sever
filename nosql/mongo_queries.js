db.product_images.find(
    {"product_id": 1001},  // 查詢條件
    {"image_url": 1, "image_type": 1, "order": 1} // 投影 (只顯示這些欄位)
).sort({"order": 1});