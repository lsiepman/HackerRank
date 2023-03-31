SELECT MAX(months * salary), COUNT(*)
FROM Employee WHERE (salary * months) = (SELECT MAX(months * salary) FROM Employee);