/*
http://bookshadow.com/weblog/2015/01/12/leetcode-second-highest-salary/

176. Second Highest Salary

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/

create database myleetcode;
use myleetcode;
create table if not exists Employee( Id int, Salary int);
insert into Employee values (1, 100);
insert into Employee values (2, 200);
insert into Employee values (3, 300);
select * from Employee;

# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary from Employee where Salary < ( select max(Salary) from Employee);
