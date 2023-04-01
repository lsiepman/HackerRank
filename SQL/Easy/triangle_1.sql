set @number = 20 + 1;
select repeat('* ', @number := @number - 1) 
from information_schema.tables;