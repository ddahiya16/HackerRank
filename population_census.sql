select sum(ct.population) 
from city as ct
join country as cnt
on ct.Countrycode = cnt.code
where cnt.continent = 'Asia'
