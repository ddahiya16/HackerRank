set @row1=0, @row2=0, @row3=0, @row4=0;
select min(Doc), min(Prof), min(Sing), min(Act)
from(select case 
            when occupation='Doctor' then (@row1:=@row1+1)
            when occupation='Professor' then (@row2:=@row2+1)
            when occupation='Singer' then (@row3:=@row3+1)
            when occupation='Actor' then (@row4:=@row4+1) end as RowNumber,
    case when occupation='Doctor' then name end as Doc,
    case when occupation='Professor' then name end as Prof,
    case when occupation='Singer' then name end as Sing,
    case when occupation='Actor' then name end as Act
  from occupations
  order by name
) as t
group by RowNumber
