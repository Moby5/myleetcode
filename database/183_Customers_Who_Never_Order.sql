/*
http://bookshadow.com/weblog/2015/01/21/leetcode-customers-who-never-order/

183. Customers Who Never Order

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

题目大意：
假设一个网站包含两个表， 顾客表Customers和订单表Orders。编写一个SQL查询找出所有从未下过订单的顾客。

解题思路：
使用NOT IN，NOT EXISTS，或者LEFT JOIN均可。
*/
# Write your MySQL query statement below
# select c.Name as Customers from Customers c where c.Id not in (select o.CustomerId from Orders o);
# select c.Name as Customers from Customers c where not exists (select o.CustomerId from Orders o where o.CustomerId = c.Id);
select c.Name as Customers from Customers c left join Orders o on c.Id = o.CustomerId where o.Id is NULL;

