SELECT SUM(ci.population)
FROM CITY ci
JOIN COUNTRY co ON ci.countrycode = co.code
WHERE co.continent = 'Asia';