import mysql.connector

def connect():
    return mysql.connector.connect(
        database='pms',
        host='localhost',
        user='root',
        password='password',
        port=3306
    )
def add_product(name,category,price,quantity):
    conn=connect()
    cursor=conn.cursor()
    sql="INSERT INTO product (name,category,price,quantity) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,(name,category,price,quantity))
    conn.commit()
    print("PRODUCT ADDED SUCCESSFULLY!")
    conn.close()
def view_products():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM product")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close
def update_product(id,name,category,price,quantity):
    conn=connect()
    cursor=conn.cursor()
    sql="UPDATE product SET name=%s,category=%s,price=%s,quantity=%s WHERE id=%s"
    cursor.execute(sql,(name,category,price,quantity,id))
    conn.commit()
    print("PRODUCT UPDATED SUCCESSFULLY")
    conn.close()
def delete_product(id):
    conn = connect()
    cursor = conn.cursor()
    sql = "DELETE FROM product WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Product deleted successfully!")
    conn.close()
def price_range(r1,r2):
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM product WHERE price BETWEEN %s AND %s"
    cursor.execute(sql, (r1, r2))
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close

def menu():
    while True:
        print("\n--- Product Management System ---")
        print("1. Add Product")
        print("2. View Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Price Range Products")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            category = input("Enter category: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            add_product(name,category,price,quantity)

        elif choice == '2':
            view_products()

        elif choice == '3':
            id = int(input("Enter product ID to update: "))
            name = input("Enter new name: ")
            category = input("Enter new category: ")
            price = input("Enter new price: ")
            quantity = input("Enter new quantity: ")
            update_product(id, name,category,price,quantity)

        elif choice == '4':
            id = int(input("Enter product ID to delete: "))
            delete_product(id)

        elif choice == '5':
            r1 = float(input("Price Range \nFrom: "))
            r2 = float(input("To:"))
            price_range(r1,r2)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
