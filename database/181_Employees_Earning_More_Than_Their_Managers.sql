/*
181. Employees Earning More Than Their Managers

The Employee table holds all employees including their managers. 
Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

题目大意：
雇员表记录了所有雇员的信息，包括他们的经理在内。每一个雇员都有一个Id，和他的经理的Id。

给定雇员表，编写一个SQL查询找出薪水大于经理的员工姓名。对于上表来说，Joe是唯一收入大于经理的员工。

解题思路：
自连接
*/

# create table if not exists Employee( Id int, Name varchar(20), Salary int, ManagerId int );
# insert into Employee values(1, "Joe", 70000, 3);
# insert into Employee values(2, "Henry", 80000, 4);
# insert into Employee values(3, "Sam", 60000, NULL);
# insert into Employee values(4, "Max", 90000, NULL);
# select * from Employee;

# Write your MySQL query statement below
select a.Name as Employee from Employee a, Employee b where a.ManagerId = b.Id and a.Salary > b.Salary;

