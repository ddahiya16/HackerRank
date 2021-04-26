select case 
    when (A+B <= C) OR (A+C <= B) OR (B+C <= C) then 'Not A Triangle'
    when A=B AND B=C then 'Equilateral'
    when (A=B AND B!=C) OR (A=C AND B!=C) OR (B=C AND A!=B) then 'Isosceles'
    when (A!=B AND B!=C) then 'Scalene'
    
END
FROM triangles
