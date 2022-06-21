from functional.CREATE import CREATE
from functional.INSERT import INSERT
from functional.SELECT import *
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



        print(f"Подключение к базе данных ")
        connection = psycopg2.connect(user="postgres",
                                      password= 1212,
                                      port="5432",
                                      database="new"
                                      )
        connection.autocommit = True



            # СREATE TABLE
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
            print(f'1. Количество исполнителей в каждом жанре: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT2)
            print(f'2. Количество треков, вошедших в альбомы 2019-2020 годов: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT3)
            print(f'3. Средняя продолжительность треков по каждому альбому: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT4)
            print(f'4. Все исполнители, которые не выпустили альбомы в 2020 году: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT5)
            print(f'5. Названия сборников, в которых присутствует Mayot: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT6)
            print(f'6. Название альбомов, в которых присутствуют исполнители более 1 жанра: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT7)
            print(f'7. Наименование треков которые не входят в сборник: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT8)
            print(f'8. Исполнители написавшие самый короткий трек: {cursor.fetchall()}')
        with connection.cursor() as cursor:
            cursor.execute(SELECT9)
            print(f'9. Название альбомов, содержащих наименьшее количество треков: {cursor.fetchall()}')

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


