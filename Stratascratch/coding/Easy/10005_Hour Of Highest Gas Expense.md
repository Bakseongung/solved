# 10005_Hour Of Highest Gas Expense.md
```yml
Company : lyft
Difficulty : Easy
Title : Hour Of Highest Gas Expense.md
```

- My solution
```sql
select hour
from Lyft_rides
order by gasoline_cost desc
limit 1;
```

- Analyze
```
Easy
```
