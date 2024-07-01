import mysql.connector
from mysql.connector import Error
from logzero import logger

import settings
import json


class MySqlDb:
    def __init__(self):
        self.connection = self.get_mysql_connection()

    def get_mysql_connection(self, new=False):
        if new or not hasattr(self, 'connection') or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host=settings.MYSQL_HOST,
                    user=settings.MYSQL_USER,
                    password=settings.MYSQL_PASSWORD,
                    database=settings.MYSQL_DB
                )
            except Error as err:
                logger.error(f"Error: '{err}'")
                self.connection = None
        return self.connection

    def define_table(self, table):
        self.table = table

    def insert_one(self, data: dict):
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"INSERT INTO {self.table} ( {columns} ) VALUES ( {placeholders} )"
        values = list(data.values())

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, values)
            self.connection.commit()
            return cursor.lastrowid
        except Error as ex:
            logger.error(f"Error: '{ex}'")
            raise ex

    def find_all(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {self.table}")
            result = cursor.fetchall()
            return result
        except Error as ex:
            logger.error(f"Error: '{ex}'")
            raise ex

    def find_one(self, document_id: int):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {self.table} WHERE id = %s", (document_id,))
            result = cursor.fetchone()
            if result is None:
                raise ValueError("Record not found")
            return result
        except Error as ex:
            logger.error(f"Error: '{ex}'")
            raise ex

    def update_one(self, document_id: int, document: dict):
        placeholders = ', '.join([f"{key} = %s" for key in document.keys()])
        sql = f"UPDATE {self.table} SET {placeholders} WHERE id = %s"
        values = list(document.values())
        values.append(document_id)

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, values)
            self.connection.commit()
            if cursor.rowcount == 0:
                raise ValueError("Record not found")
            return self.find_one(document_id)
        except Error as ex:
            logger.error(f"Error: '{ex}'")
            raise ex

    def delete_one(self, document_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM {self.table} WHERE id = %s", (document_id,))
            self.connection.commit()
            if cursor.rowcount == 0:
                raise ValueError("Record not found")
        except Error as ex:
            logger.error(f"Error: '{ex}'")
            raise ex
