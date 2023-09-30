-- Write your MySQL query statement below
-- https://leetcode.com/problems/rising-temperature/description/
-- select id from (
-- select id, temperature, lag(Weather.temperature) over (order by Weather.recordDate) as past
-- from Weather) AS CTE
-- where CTE.temperature > CTE.past;


-- # Write your MySQL query statement below
select w2.id from Weather w1 left join Weather w2 
on DATEDIFF (w1.recordDate, w2.recordDate) = -1
where w2.temperature > w1.temperature;