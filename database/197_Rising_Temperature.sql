/*
http://bookshadow.com/weblog/2015/03/31/leetcode-rising-temperature/
https://leetcode.com/articles/rising-temperature/

197. Rising Temperature

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+
For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+

题目大意：
给定Weather表，编写SQL查询找出所有温度较前一天高的记录Id。

SQL查询：
# Write your MySQL query statement below
SELECT w1.Id FROM Weather w1 INNER JOIN Weather w2 
ON TO_DAYS(w1.Date) = TO_DAYS(w2.Date) + 1 AND w1.Temperature > w2.Temperature

Solution
Approach: Using JOIN and DATEDIFF() clause [Accepted]

Algorithm
MySQL uses DATEDIFF to compare two date type values.

So, we can get the result by joining this table weather with itself and use this DATEDIFF() function.
MySQL
SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperature
;
*/

# select w1.Id from Weather w1, Weather w2 where to_days(w1.Date) = to_days(w2.Date) + 1 and w1.Temperature > w2.Temperature;

select w1.Id from Weather w1, Weather w2 where datediff(w1.Date, w2.Date) = 1 and w1.Temperature > w2.Temperature;

# select w1.Id from Weather w1 inner join Weather w2 on to_days(w1.Date) = to_days(w2.Date) + 1 and w1.Temperature > w2.Temperature;
