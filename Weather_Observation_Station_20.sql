/*Learned how to calculate the median.*/
set @id = 0;
set @cnt = (select count(id)/2 from station);
select round(temp.lat_n, 4)
from (select @id:=@id+1 as id, lat_n 
      from station order by lat_n) as temp
where temp.id = @cnt;
