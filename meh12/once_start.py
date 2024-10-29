import sqlite3

def fill_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    
    products = [
        ("Product1", "описание 1", 100),
        ("Product2", "описание 2", 200),
        ("Product3", "описание 3", 300),
        ("Product4", "описание 4", 400)
    ]
    
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    connection.commit()
    connection.close()

fill_products()
