-- # Write your MySQL query statement below
--https://leetcode.com/problems/employee-bonus/

select name, bonus from
Employee left join Bonus on Employee.empID = Bonus.EmpID where Bonus.bonus < 1000 or Bonus.bonus is null;


