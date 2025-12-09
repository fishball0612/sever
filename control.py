import mysql.connector
from pymongo import MongoClient
import json
from typing import Dict, Any, List

# -----------------------------------------------------
# 0. 資料庫連線配置 (請替換為您的實際資訊)
# -----------------------------------------------------
# MySQL 配置 (SQL)
MYSQL_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'ninalee940501',
    'database': 'schema' # 您的 SQL 資料庫名稱 (參照截圖)
}

# MongoDB 配置 (NoSQL)
MONGODB_URI = "mongodb://localhost:27017/"
MONGODB_DB_NAME = "ecommerce_db" # 您的 MongoDB 資料庫名稱 (參照截圖)
MONGODB_COLLECTION_NAME = "product_images" # 您的 Collection 名稱

PRODUCT_ID_TO_QUERY = 1001

# -----------------------------------------------------
# 1. 核心功能 A: 查詢商品詳細資訊 (SQL + NoSQL 結合查詢)
# -----------------------------------------------------
def get_product_details(product_id: int) -> Dict[str, Any]:
    """
    查詢商品的結構化資訊 (SQL) 和非結構化圖片 (NoSQL)。
    """
    sql_data = {}
    
    print(f"--- 1. 查詢商品 ID: {product_id} 的 SQL 數據 ---")
    
    # 模擬 SQL 查詢 (在實際 PoC 中您需要連線並執行 SQL 查詢)
    try:
        # my_db = mysql.connector.connect(**MYSQL_CONFIG)
        # my_cursor = my_db.cursor(dictionary=True)
        
        sql_query = """
        SELECT 
            P.product_name, 
            P.price, 
            P.stock_quantity, 
            C.category_name
        FROM 
            product P
        JOIN 
            category C ON P.category_id = C.category_id
        WHERE 
            P.product_id = %s;
        """
        # my_cursor.execute(sql_query, (product_id,))
        # sql_data = my_cursor.fetchone()
        
        # 模擬結果 (使用假數據)
        if product_id == 1001:
            sql_data = {
                "product_id": 1001,
                "product_name": "4K Monitor 27\"",
                "price": 12000.00,
                "stock_quantity": 10,
                "category_name": "Electronics"
            }
            print("✅ SQL 查詢成功。")
        else:
            print(f"❌ SQL 查詢結果：商品 ID {product_id} 不存在。")
            return {"error": f"商品 ID {product_id} 不存在。"}

    except Exception as e:
        # print(f"MySQL 連線/查詢錯誤: {e}")
        return {"error": "SQL 資料庫錯誤。"}
    
    
    # -----------------------------------------------------
    # 2. 查詢 NoSQL 資料庫 (MongoDB)
    # -----------------------------------------------------
    image_list: List[Dict[str, Any]] = []
    
    print(f"\n--- 2. 查詢商品 ID: {product_id} 的 NoSQL 圖片數據 ---")

    try:
        # client = MongoClient(MONGODB_URI)
        # db = client[MONGODB_DB_NAME]
        # collection = db[MONGODB_COLLECTION_NAME]
        
        mongodb_query = { "product_id": product_id }
        mongodb_projection = { "image_url": 1, "image_type": 1, "order": 1, "_id": 0 }
        
        # 模擬 MongoDB 查詢結果 (參照您的 Compass 截圖數據)
        if product_id == 1001:
            image_list = [
                { "image_type": "main", "image_url": "https://cdn.shop.com/monitor_1001_main.jpg", "order": 1 },
                { "image_type": "gallery", "image_url": "https://cdn.shop.com/monitor_1001_side.jpg", "order": 2 }
            ]
            print(f"✅ NoSQL 查詢成功獲取圖片數量：{len(image_list)} 張。")

    except Exception as e:
        # print(f"MongoDB 連線/查詢錯誤: {e}")
        print("❌ NoSQL 資料庫錯誤，返回空圖片列表。")
        image_list = []
        
    
    # -----------------------------------------------------
    # 3. 彙總並返回最終結果
    # -----------------------------------------------------
    return {
        "基本資訊": {
            "商品名稱": sql_data["product_name"],
            "價格": f"NT$ {sql_data['price']:.2f}",
            "分類": sql_data["category_name"],
            "庫存": sql_data["stock_quantity"]
        },
        "圖片資源": sorted(image_list, key=lambda x: x['order'])
    }


# -----------------------------------------------------
# 執行 PoC
# -----------------------------------------------------
if __name__ == "__main__":
    
    print("==================================================")
    print("====== 概念驗證 (PoC) 協同查詢 =======")
    print("==================================================")
    
    product_details = get_product_details(PRODUCT_ID_TO_QUERY)
    
    print("\n--- 4. 整合最終商品詳情 (應用程式輸出) ---")
    print(json.dumps(product_details, indent=4, ensure_ascii=False))