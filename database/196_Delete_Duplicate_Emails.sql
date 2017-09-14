/*
http://bookshadow.com/weblog/2015/03/29/leetcode-delete-duplicate-emails/

196. Delete Duplicate Emails

Write a SQL query to delete all duplicate email entries in a table named Person, 
keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

题目大意：
编写SQL删除Person表中所有的重复email条目，只保留Id最小的唯一email记录。
其中，Id是表的主键。

SQL语句：
解法一：
DELETE p1 FROM Person p1 INNER JOIN Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;

上述SQL使用了MySQL DELETE语法的多表语法I，参阅：https://dev.mysql.com/doc/refman/5.0/en/delete.html
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    tbl_name[.*] [, tbl_name[.*]] ...
    FROM table_references
    [WHERE where_condition]
    
解法二：
DELETE FROM p1 USING Person p1 INNER JOIN Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
上述SQL使用了MySQL DELETE语法的多表语法II
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    FROM tbl_name[.*] [, tbl_name[.*]] ...
    USING table_references
    [WHERE where_condition]
    
解法三：
# Write your MySQL query statement below
DELETE FROM Person WHERE ID NOT IN 
(SELECT * FROM (SELECT MIN(Id) FROM Person p GROUP BY Email) t);

注意，使用下面的SQL会抛出运行时错误：
DELETE FROM Person WHERE ID NOT IN (SELECT MIN(Id) FROM Person GROUP BY Email);
Runtime Error Message:    You can't specify target table 'Person' for update in FROM clause
Last executed input:    {"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": []}}
上述SQL的错误原因为：
在MySQL中，禁止在FROM子句中指定被更新的目标表。
*/

DELETE p1 FROM Person p1 INNER JOIN Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
