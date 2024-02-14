-- Напишите запросы, которые выводят следующую информацию:
-- 1. "имя контакта" и "город" (contact_name, city) из таблицы customers (только эти две колонки)
SELECT contact_name, city FROM customers;

-- 2. идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
SELECT order_id, avg(orders.shipped_date - orders.order_date) as date_diff FROM orders GROUP BY order_id;

-- 3. все города без повторов, в которых зарегистрированы заказчики (customers)
SELECT DISTINCT city FROM customers ORDER BY city;

-- 4. количество заказов (таблица orders)
SELECT COUNT(*) AS count_orders FROM orders;

-- 5. количество стран, в которые отгружался товар (таблица orders, колонка ship_country)
SELECT COUNT(DISTINCT ship_country) AS count_countries FROM orders;