from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
app = FastAPI()
@app.post("/orders")

class OrderItem(BaseModel):
    item: int
    quantity: int
class Order(BaseModel):
    order_items: list[OrderItem]
    
def create_orders(order: Order):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Mypgdb@26"
    )
    cursor = conn.cursor()  
    for item in order.order_items:
        cursor.execute("SELECT Item_price FROM Inventory WHERE Items = %s", (item.order_item,))
        result = cursor.fetchone()                                                
        if not result:
            return {"error": f"Item '{item.order_item}' price not found in inventory."}     
        item_price = result[0]                              
        total_price = item.quantity * item_price            
        cursor.execute("INSERT INTO Orders (Order_list, Quantity, Total_price) VALUES (%s, %s, %s)",
                       (item.order_item, item.quantity, total_price))           
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Order created successfully."}