/*Learned about the repeat function
Infomation_schema.tables: INFORMATION_SCHEMA provides access to database metadata, information about the MySQL server such as the name of a database or table, the data type of a column, or access privileges.  */

set @number = 21;
select repeat('* ', @number := @number - 1) from information_schema.tables;
