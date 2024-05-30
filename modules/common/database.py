import os
import re
import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect('become_qa_auto.db')
        self.connection.execute('PRAGMA foreign_keys = 1')
        self.connection.commit()
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

    def insert_product(self, product_id, name, description, qnt, replace = True):
        if replace:
            query = "INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES (?, ?, ?, ?)"
        else:
            query = "INSERT INTO products (id, name, description, quantity) \
                            VALUES (?, ?, ?, ?)"
        try:
            self.cursor.execute(query, (product_id, name, description, qnt))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

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
    def insert_orders(self, id, customer_id, product_id, order_date):
        query = "INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
         VALUES (?, ?, ?, ?);"
        try:
            self.cursor.execute(query, (id, customer_id, product_id, order_date))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

