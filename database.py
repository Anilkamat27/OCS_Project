import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pass123',
            database='testdb'
        )
        self.cursor = self.conn.cursor()

    def insert_user(self, role, user_id, password):
        query = "INSERT INTO users (role, user_id, password) VALUES (%s, %s, %s)"
        values = (role, user_id, password)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_admin_data(self):
        query = "SELECT role, user_id, password FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
