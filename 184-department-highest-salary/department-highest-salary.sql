SELECT Department, Employee, Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentid ORDER BY e.salary DESC) AS rnk
    FROM employee e
    JOIN department d ON e.departmentid = d.id
) AS ranked_employees
WHERE rnk = 1;   