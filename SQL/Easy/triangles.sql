SELECT CASE
    -- all equal sides
    WHEN A = B AND B = C THEN 'Equilateral' 
    --  the combined value of sides A and B is not larger than that of side C.
    WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle' 
    -- Two sides of equal length
    WHEN A = B OR B = C OR A = C THEN 'Isosceles' 
    ELSE 'Scalene' 
END 
FROM TRIANGLES;