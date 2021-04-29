/*Learned new function char_length()/length() to calculate the lenght of a value
Two select statment can be combined in this case
use of limit function*/

select city, length(city) from station
order by length(city),city asc
limit 1;
select city, length(city) from station
order by length(city) desc
limit 1;
