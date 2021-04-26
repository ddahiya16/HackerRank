select max(t.earn), max(t.cnt) from 
(select salary*months as earn, count(salary*months) cnt 
from employee group by salary*months) as t
