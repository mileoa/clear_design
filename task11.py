# Было
from psycopg2.extras import RealDictCursor
from abc import ABC, abstractmethod
from psycopg2 import pool
from contextlib import contextmanager


class UserService:

    def get_all_users(limit: int = 10, offset: int = 0):
        connection = psycopg2.connect(
            host="localhost",
            database="mydb",
            user="admin",
            password="secret",
        )
        try:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    "SELECT * FROM users LIMIT %s OFFSET %s", (limit, offset)
                )
                users = cursor.fetchall()
        except Exception as e:
            users = None
            print("Ошибка при получении продуктов:", e)
        return users


# Стало
class DBConnection(ABC):

    @abstractmethod
    def get_connection(self):
        pass


class PGPoolConnection(DBConnection):

    def __init__(self, min_conn, max_conn, conn_string):
        self._pool = pool.SimpleConnectionPool(min_conn, max_conn, conn_string)

    @contextmanager
    def get_connection(self):
        connection = self._pool.getconn()
        try:
            yield connection
        finally:
            self._pool.putconn(connection)


class UserService:

    def __init__(self, db_connection: DBConnection):
        self._db_connection: DBConnection = db_connection

    def get_all_users(self, limit: int = 10, offset: int = 0):
        try:
            with self._db_connection.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(
                        "SELECT * FROM users LIMIT %s OFFSET %s", (limit, offset)
                    )
                    users = cursor.fetchall()
        except Exception as e:
            users = None
            print("Ошибка при получении продуктов:", e)
        return users
