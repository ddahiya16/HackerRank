/*Learned the use of replace function*/
select ceiling(sum(wrng.salary - act.salary)/count(wrng.salary)) as s
from employees as wrng
join (select id, replace(salary, 0, '') as salary from employees) as act
on wrng.id = act.id;      
