set @number = 21;
select star from (select repeat('* ', @number := @number - 1) 
        as star from information_schema.tables 
                  having star != '' order by star asc) as temp;
