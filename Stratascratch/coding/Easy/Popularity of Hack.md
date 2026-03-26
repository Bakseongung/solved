### 10061_Popularity of Hack
https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=3
```yml
Company : Meta
Difficulty : Easy
Question Type : 
Title : Popularity of Hack
```

- My solution
```
perfectly solved
```
```sql
select
    e.location,
    avg(s.popularity) as avg_popularity
from facebook_employees e
join facebook_hack_survey s on  e.id=s.employee_id
group by location
```

- Analyze
```
x
```

