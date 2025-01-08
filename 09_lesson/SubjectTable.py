from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
        "add": text(
            "INSERT INTO subject(subject_title) VALUES (:subject_title)"),
        "edit by id": text(
            "UPDATE subject SET subject_title ="
            " :new_title WHERE subject_id = :id"),
        "delete by id": text(
            "DELETE FROM subject WHERE subject_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get(self):
        with self.__db.connect() as connection:
            result = connection.execute("SELECT * FROM subject")
            return result.fetchall()

    def add(self, subject_title):
        with self.__db.connect() as connection:
            with connection.begin():
                result = connection.execute(
                     self.__scripts["add"], {"subject_title": subject_title}
                 )
            return result.rowcount

    def edit(self, new_title, id):
        with self.__db.connect() as connection:
            with connection.begin():
                result = connection.execute(
                    self.__scripts["edit by id"], {
                        "new_title": new_title, "id": id}
                )
                return result.rowcount

    def delete(self, id):
        with self.__db.connect() as connection:
            with connection.begin():  # Фиксация транзакции
                result = connection.execute(
                    self.__scripts["delete by id"], {"id": id}
                )
                return result.rowcount

    def max_count(self):
        with self.__db.connect() as connection:
            result = connection.execute(text(
                "SELECT MAX(subject_id) FROM subject"))
            return result.scalar()
