import psycopg2
from tabulate import tabulate  # Для красивого форматирования вывода таблицы

conn = psycopg2.connect(database="lab10",
                        host="localhost",
                        user="postgres",
                        password="1111",
                        port="5555")
                        
cursor = conn.cursor()

def insertIntoTableFromConsole():
    name1 = input("First Name: ")
    name2 = input("Second Name: ")
    phone = input("Number: ")
    cursor.execute(f"SELECT first_name FROM users WHERE first_name like '{name1}' and second_name like '{name2}'")
    name = cursor.fetchall()
    if name:
        cursor.execute(f"UPDATE users SET number = {phone} WHERE first_name like '{name1}' and second_name like '{name2}'")
    else:
        cursor.execute(f"INSERT INTO users(First_name, Second_name, Number) VALUES('{name1}', '{name2}', '{phone}')")

    conn.commit()  


errors = []
def insert_many():
    while True:
        user_input = input("first name: ")
        if user_input.lower() != 'exit':

            name1 = user_input
            name2 = input("Second name: ")
            number = input("Number: ")
            is_cor = True

            for i in number:
                try:
                    if int(i) not in range(0, 10):
                        continue
                except:
                    errors.append((name1, name2, number))
                    is_cor = False

            if is_cor:
                cursor.execute(f"INSERT INTO users(First_name, Second_name, Number) VALUES('{name1}', '{name2}', '{number}')")
                conn.commit()
                is_cor = True

        else:
            print("PROBLEMS WITH NUMBER: ", errors)
            break

def print_by_page():
    page = int(input("Which page: "))
    n = page*5 #every 5 is new page
    cursor.execute(f"SELECT first_name, second_name, number FROM users WHERE id between '{n-4}' and '{n}'")
    
    rows = cursor.fetchall()

    # Получение заголовков столбцов
    column_names = [desc[0] for desc in cursor.description]

    # Форматирование и вывод таблицы с использованием tabulate
    print(tabulate(rows, headers=column_names, tablefmt="psql"))



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
        param = input("delete by name or phone? (n or p)")
        if param == "n":
            name = input("name to delete: ")
            cursor.execute(f"DELETE FROM users WHERE First_name = '{name}'")
        else:
            phone = input("phone number to delete: ")
            cursor.execute(f"DELETE FROM users WHERE number = '{phone}'")
        conn.commit()  

def show_all_records():
    cursor.execute(f"SELECT first_name, second_name, Number FROM users")
    column_names = [desc[0] for desc in cursor.description]
    record = cursor.fetchall()
    print(tabulate(record, headers=column_names, tablefmt="psql"))

# insertIntoTableFromConsole()
# insert_many()
# changeValue()
# delete_value()
# print_table("users")
# show_all_records()
# print_by_page(1)

cursor.close()
conn.close()
