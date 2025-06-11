import mysql.connector

def connect():
    return mysql.connector.connect(
        database='customer_db',
        host='localhost',
        user='root',
        password='password',
        port=3306
    )

def add_customer(name,email,phone,city):
    conn=connect()
    cursor=conn.cursor()
    sql="INSERT INTO customers (name,email,phone,city) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,(name,email,phone,city))
    conn.commit()
    print("CUSTOMER ADDED SUCCESSFULLY!")
    conn.close()

def view_customers():
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close

def update_customer(customer_id,name,email,phone,city):
    conn=connect()
    cursor=conn.cursor()
    sql="UPDATE customers SET name=%s,email=%s,phone=%s,city=%s WHERE id=%s"
    cursor.execute(sql,(name,email,phone,city,customer_id))
    conn.commit()
    print("CUSTOMER UPDATED SUCCESSFULLY")
    conn.close()

def delete_customer(customer_id):
    conn = connect()
    cursor = conn.cursor()
    sql = "DELETE FROM customers WHERE id=%s"
    cursor.execute(sql, (customer_id,))
    conn.commit()
    print("Customer deleted successfully!")
    conn.close()

def menu():
    while True:
        print("\n--- Customer Management System ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            city = input("Enter city: ")
            add_customer(name, email, phone, city)

        elif choice == '2':
            view_customers()

        elif choice == '3':
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            city = input("Enter new city: ")
            update_customer(customer_id, name, email, phone, city)

        elif choice == '4':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()