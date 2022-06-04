from functional.CREATE import CREATE
from functional.INSERT import INSERT
from functional.SELECT import SELECT1, SELECT2, SELECT3, SELECT4, SELECT5, SELECT6
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def functional():
    global connection
    try:
        connection = psycopg2.connect(user="postgres",
                                      password= password_db,
                                      port="5432"
                                      )

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        print("\nИдёт создание новой базы данных...\n")
        sql_create_database = f'create database {name_db}'
        cursor.execute(sql_create_database)



        print(f"Подключение к базе данных {name_db}")
        connection = psycopg2.connect(user="postgres",
                                      password= password_db,
                                      port="5432",
                                      database=name_db
                                      )
        connection.autocommit = True



        #     СREATE TABLE
        with connection.cursor() as cursor:
            print("\nИдёт создание таблиц!\n")
            cursor.execute(CREATE)


        #       INSERT
        with connection.cursor() as cursor:
            print("\nИдёт заполнение таблиц!\n")
            cursor.execute(INSERT)

        #       SELECT
        with connection.cursor() as cursor:
            cursor.execute(SELECT1)
            print(f'1. Альбомы вышедшие в 2018 году: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT2)
            print(f'2. Самый длительный трек: {cursor.fetchone()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT3)
            print(f'3. Треки продолжительностью более 3.5мин: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT4)
            print(f'4. сборники вышедшие в период с 2018 по 2020 год включительно: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT5)
            print(f'5. Исполнители, чье имя состоит из 1 слова: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT6)
            print(f'6. Треки которые содержат слово "мой" или "my": {cursor.fetchall()}')

    # ОШИБКА
    except Exception as ex:
        print("\n                     !!!ПРОБЛЕМС!!!\n", ex)

    # ЗАКРЫТИЕ ПРОГРАММЫ
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("\n!!!ПРОГРАММА ЗАВЕРШЕНА!!!\n")



if __name__ == "__main__":
    name_db = input("Введите название для базы данных: ")
    password_db = input('Введите пароль от пользователя "postgres": ')
    functional()


