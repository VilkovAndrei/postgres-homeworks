"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import psycopg2
import csv

postgres_password = os.getenv('PostgreSQL_PSW')

try:
    with psycopg2.connect(host='localhost', database='nord', user='postgres', password=postgres_password) as conn:
        with conn.cursor() as cur:
            try:
                with open(os.path.join(os.path.dirname(__file__),"north_data","employees_data.csv"), "r", encoding='utf8') as csv_employees_file:
                    reader = csv.DictReader(csv_employees_file)
                    for dict_item in reader:
                        SQL = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)"
                        data = (dict_item["first_name"], dict_item["last_name"], dict_item["title"], dict_item["birth_date"], dict_item["notes"])
                        cur.execute(SQL, data)
                conn.commit()
            except FileNotFoundError:
                raise FileNotFoundError("Отсутствует файл employees_data.csv")
            except KeyError:
                raise KeyError("Ошибка ключа")

            try:
                with open(os.path.join(os.path.dirname(__file__),"north_data","customers_data.csv"), "r", encoding='utf8') as csv_customers_file:
                    reader = csv.DictReader(csv_customers_file)
                    for dict_item in reader:
                        SQL = "INSERT INTO customers VALUES (%s, %s, %s)"
                        data = (dict_item["customer_id"], dict_item["company_name"], dict_item["contact_name"])
                        cur.execute(SQL, data)
                conn.commit()
            except FileNotFoundError:
                raise FileNotFoundError("Отсутствует файл customers_data.csv")
            except KeyError:
                raise KeyError("Ошибка ключа")

            try:
                with open(os.path.join(os.path.dirname(__file__),"north_data","orders_data.csv"), "r", encoding='utf8') as csv_orders_file:
                    reader = csv.DictReader(csv_orders_file)
                    for dict_item in reader:
                        SQL = "INSERT INTO customers VALUES (%s, %s, %s, %s, %s)"
                        data = (dict_item["order_id"], dict_item["customer_id"], dict_item["employee_id"], dict_item["order_date"], dict_item["ship_city"])
                        cur.execute(SQL, data)
                conn.commit()
            except FileNotFoundError:
                raise FileNotFoundError("Отсутствует файл orders_data.csv")
            except KeyError:
                raise KeyError("Ошибка ключа")

except Exception:
    print("Что-то пошло не так!")
finally:
    conn.close()
