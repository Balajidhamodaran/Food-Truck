import psycopg2

conn=psycopg2.connect(
    host="localhost",                                                                                           
    database="postgres",
    user="postgres",
    password="Mypgdb@26"
)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Inventory (
    Id SERIAL,
    Items VARCHAR(255) NOT NULL PRIMARY KEY,
    available_quantity INTEGER,
    Item_price INTEGER
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Orders (
    Order_id SERIAL PRIMARY KEY,
    Order_list TEXT NOT NULL,
    Quantity INTEGER,
    Total_price INTEGER
)""")


conn.commit()
cursor.close()
conn.close()    