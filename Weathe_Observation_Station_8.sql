/*Learned to regexp instead of like, improving the readability and reducinng the line of code.*/

select city 
from station 
where city regexp '^[aeiou].*[aeiou]$';
