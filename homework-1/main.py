"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import psycopg2
import csv
from datetime import date

postgres_password = os.getenv('PostgreSQL_PSW')

try:
    with (psycopg2.connect(host='localhost', database='north', user='postgres', password=postgres_password) as conn):
        print("Соединение с БД выполнено")
        with conn.cursor() as cur:
            try:
                with open(os.path.join(os.path.dirname(__file__), "north_data", "employees_data.csv"),
                          "r", encoding='utf8') as csv_employees_file:
                    print("Читаем employees_data.csv")
                    reader = csv.DictReader(csv_employees_file)
                    for dict_item in reader:
                        birth_date = date.fromisoformat(dict_item["birth_date"])
                        employee_data = (dict_item["first_name"], dict_item["last_name"], dict_item["title"],
                                         birth_date, dict_item["notes"])
                        cur.execute("INSERT INTO employees (first_name, last_name, title, birth_date, notes)"
                                    " VALUES (%s, %s, %s, %s, %s)",
                                    (employee_data[0], employee_data[1], employee_data[2], employee_data[3],
                                     employee_data[4]))
                    conn.commit()
                    print("Данные добавлены: employees_data.csv --> employees")

            except FileNotFoundError:
                raise FileNotFoundError("Отсутствует файл employees_data.csv")
            except KeyError:
                raise KeyError("Ошибка ключа")

            try:
                with open(os.path.join(os.path.dirname(__file__), "north_data", "customers_data.csv"),
                          "r", encoding='utf8') as csv_customers_file:
                    print("Читаем customers_data.csv")
                    reader = csv.DictReader(csv_customers_file)
                    for dict_item in reader:
                        customer_data = (dict_item["customer_id"], dict_item["company_name"], dict_item["contact_name"])
                        cur.execute("INSERT INTO customers (customer_id, company_name, contact_name)"
                                    " VALUES (%s, %s, %s)",
                                    (customer_data[0], customer_data[1], customer_data[2]))
                    conn.commit()
                    print("Данные добавлены: customers_data.csv --> customers")

            except FileNotFoundError:
                raise FileNotFoundError("Отсутствует файл customers_data.csv")
            except KeyError:
                raise KeyError("Ошибка ключа")

            try:
                with open(os.path.join(os.path.dirname(__file__), "north_data", "orders_data.csv"),
                          "r", encoding='utf8') as csv_orders_file:
                    print("Читаем orders_data.csv")
                    reader = csv.DictReader(csv_orders_file)
                    for dict_item in reader:
                        order_date = date.fromisoformat(dict_item["order_date"])
                        order_data = (int(dict_item["order_id"]), dict_item["customer_id"],
                                      int(dict_item["employee_id"]), order_date, dict_item["ship_city"])
                        cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)"
                                    " VALUES (%s, %s, %s, %s, %s)",
                                    (order_data[0], order_data[1], order_data[2], order_data[3], order_data[4]))
                    conn.commit()
                    print("Данные добавлены: orders_data.csv --> orders")

            except FileNotFoundError:
                raise FileNotFoundError("Отсутствует файл orders_data.csv")
            except KeyError:
                raise KeyError("Ошибка ключа")

except Exception:
    print("Что-то пошло не так!")
finally:
    conn.close()
    print("Соединение с БД закрыто")
