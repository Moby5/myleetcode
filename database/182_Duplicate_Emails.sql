/*
http://bookshadow.com/weblog/2015/01/17/leetcode-duplicate-emails/
    
    182. Duplicate Emails

    Write a SQL query to find all duplicate emails in a table named Person.

    +----+---------+
    | Id | Email   |
    +----+---------+
    | 1  | a@b.com |
    | 2  | c@d.com |
    | 3  | a@b.com |
    +----+---------+
    For example, your query should return the following for the above table:

    +---------+
    | Email   |
    +---------+
    | a@b.com |
    +---------+
    Note: All emails are in lowercase.
        
    题目大意：
    编写一个SQL查询从Person表中找出所有重复的邮箱地址。

    例如，上表的查询结果应该返回a@b.com

    所有的邮箱地址均为小写字母。

    解题思路：
    使用GROUP BY和HAVING即可
    */

    # create table if not exists Person( Id int, Email varchar(20) );
    # insert into Person values(1, 'a@b.com');
    # insert into Person values(2, 'c@d.com');
    # insert into Person values(3, 'a@b.com');
    # select * from Person;

    # Write your MySQL query statement below
    select Email from Person group by Email having count(*) > 1;
