/*
Enter your query here.
*/
select if(g.grade>7, s.name, null) 
,g.grade , s.marks
from students as s 
join grades as g
on s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name asc, s.marks asc
