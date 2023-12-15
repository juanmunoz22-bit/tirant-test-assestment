import sqlite3

class Database:

    @classmethod
    def connect(cls, database_name: str="inventory.db"):
        connection = sqlite3.connect(database=database_name)
        return connection
    
    @classmethod
    def create_table(cls, connection: sqlite3.Connection, sql: str):
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()

    @classmethod
    def insert(cls, connection: sqlite3.Connection, sql: str, params: tuple):
        cursor = connection.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        connection.commit()
        cursor.close()

    @classmethod
    def fetch_one(cls, connection: sqlite3.Connection, sql: str):
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()

        return result
    
    @classmethod
    def fetch_all(cls, connection: sqlite3.Connection, sql: str):
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()

        return result


    @classmethod
    def close_connection(cls, connection: sqlite3.Connection):
        if connection:
            connection.close()