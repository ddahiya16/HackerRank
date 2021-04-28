select name
from students as st
join friends as fr
on st.id = fr.id
join packages as pa1
on fr.id = pa1.id
join packages as pa2
on fr.friend_id = pa2.id
where pa1.salary<pa2.salary
order by pa2.salary
