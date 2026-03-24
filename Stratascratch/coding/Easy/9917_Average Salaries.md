### 9917_Average Salaries
https://platform.stratascratch.com/coding/9917-average-salaries?code_type=1
```yml
Company : Salesforce, Glassdoor
Difficulty : Easy
Question Type : 
Title : Average Salaries
```

- My solution
```
Solved
```
```sql
select
    e.department,
    e.first_name,
    e.salary,
    d.avg_salary
from
(
    select
        department,
        avg(salary) as avg_salary
    from employee
    group by department
) d
right join employee e on d.department=e.department 
```

- Analyze
```
I looked for solutions and found two of them,
one of which uses `with as`.
I wish I had used that one too.
However, since user HarryPits117’s answer was so clean and concise...
I’m posting this one as well.
```
```sql
-- The original correct answer
WITH dept_avg AS
  (SELECT department,
          AVG(salary) AS avg_salary
   FROM employee
   GROUP BY department)
SELECT e.department,
       e.first_name,
       e.salary,
       d.avg_salary
FROM employee e
JOIN dept_avg d ON e.department = d.department
ORDER BY e.department;

-- user HarryPits117's solution
select department, first_name, salary, avg(salary) over (partition by department)
from employee
```
