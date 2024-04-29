import psycopg2
from tabulate import tabulate  # Для красивого форматирования вывода таблицы
import csv

conn = psycopg2.connect(database="lab10",
                        host="localhost",
                        user="postgres",
                        password="1111",
                        port="5555")
                        
cursor = conn.cursor()

def insert_data_from_csv(csv_file, table_name):

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cursor.execute(f"INSERT INTO {table_name}(first_name, second_name, number) VALUES ('{row[0]}', '{row[1]}', '{row[2]}')")
    conn.commit()


def insertIntoTableFromConsole():
    name1 = input("First Name: ")
    name2 = input("Second Name: ")
    phone = input("Number: ")
    cursor.execute(f"INSERT INTO users(First_name, Second_name, Number) VALUES('{name1}', '{name2}', '{phone}')")
    conn.commit()  

def changeValue():
    is_wanna_change = input("Do you want to change some values?(Y or N) ")
    if is_wanna_change == "Y":
        columm = input("Which columm would you like to change: ")
        value = input("For what value do you want to change:  ")
        id = int(input("ID of changing row: "))
        cursor.execute(f"UPDATE users SET {columm} = '{value}' WHERE id = {id}")
        conn.commit()  

def print_table(table_name):
    columm = input("By which columm sort: ")
    filter1 = input("ASC or DESC: ")
    try:
        # Выполнение запроса на получение данных из таблицы
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY {columm} {filter1}")

        # Получение результатов запроса
        rows = cursor.fetchall()
        
        # Получение заголовков столбцов
        column_names = [desc[0] for desc in cursor.description]

        # Форматирование и вывод таблицы с использованием tabulate
        print(tabulate(rows, headers=column_names, tablefmt="psql"))

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def delete_value():
    is_wanna_delete = input("Do you want to delete something?(Y or N) ")
    if is_wanna_delete == "Y":
        name = input("name to delete: ")
        cursor.execute(f"DELETE FROM users WHERE First_name = '{name}'")
        conn.commit()  


# insertIntoTableFromConsole()
# changeValue()
# delete_value()
# insert_data_from_csv('file.csv', 'users')
# print_table("users")

cursor.close()
conn.close()
