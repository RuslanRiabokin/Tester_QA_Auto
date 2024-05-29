import os
import re
import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect('become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"

        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Failed to insert product due to database error: {e}") from e


    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()


    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record


# My tests
    def insert_product_luscious(self, product_id, name, description, qnt):
        if not re.match(r'^\d+$', str(qnt)):
            raise ValueError(f"Invalid quantity: {qnt}. Quantity must be an integer.")

        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            raise ValueError(f"Failed to insert product due to database error: {e}") from e