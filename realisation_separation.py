from abc import ABC, abstractmethod
import psycopg2
from typing import Callable


def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        database="mydb",
        user="admin",
        password="secret",
    )


class Storage(ABC):

    @abstractmethod
    def save(self, data: str) -> None: ...

    @abstractmethod
    def retrieve(self, key: int) -> str: ...


class DBStorage(Storage):
    def __init__(self) -> None:
        self._connection_func: Callable = connect_to_db

    def save(self, data: str) -> None:
        conn = self._connection_func()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO some_table (str) VALUES (%s)",
                    (data,),
                )
                conn.commit()
        except Exception as e:
            print("Ошибка при сохранении:", e)
            raise e

    def retrieve(self, key: int) -> str:
        conn = self._connection_func()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT str FROM some_table WHERE id = %s", (key,))
                value = cursor.fetchone()
                return value[0] if value else None
        except Exception as e:
            print("Ошибка при получении:", e)
            raise e


if __name__ == "__main__":
    db_storage: DBStorage = DBStorage()

    db_storage.save("test1")
    db_storage.save("test2")

    print(db_storage.retrieve(41))
    print(db_storage.retrieve(42))
