Select con.continent, floor(Avg(cit.population)) from Country as con
join City as cit
on con.code = cit.countrycode
group by con.continent
