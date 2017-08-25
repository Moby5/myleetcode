"""
http://bookshadow.com/weblog/2015/01/12/leetcode-combine-two-tables/

175. Combine Two Tables

LeetCode在原有的算法（Algorithm）题目分类基础之上，推出了全新的数据库（Database）题目分类，旨在帮助开发者提高数据库的开发技能。

Database分类下的第一题叫做Combine Two Tables，非常简单，大家可以拿来练手。只需将SQL语句填写在答题区即可。

题目描述：

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State

题目大意：
有两个数据表：Person表和Address表。Person（人员）表主键为PersonId，Address（地址）表主键是AddressId，通过PersonId与Person表关联。

编写一个SQL查询，对于Person表中的每一个人，取出FirstName, LastName, City, State属性，无论其地址信息是否存在。

解题思路：
Person表是主表，Address表是从表，通过Left Outer Join左外连接即可。
"""

# Write your MySQL query statement below
select Person.FirstName, Person.LastName, Address.City, Address.State from Person left join Address on Person.PersonId = Address.PersonId;

# Write your MySQL query statement below
# SELECT p.FirstName, p.LastName, a.City, a.State FROM Person p LEFT OUTER JOIN Address a USING (PersonId);
