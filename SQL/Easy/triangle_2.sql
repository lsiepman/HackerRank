set @number = 0;
select repeat('* ', @number := @number + 1) 
from information_schema.tables
where @number < 20;