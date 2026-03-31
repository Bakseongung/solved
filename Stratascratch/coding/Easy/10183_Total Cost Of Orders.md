### 10183_Total Cost Of Orders
https://platform.stratascratch.com/coding/10183-total-cost-of-orders?code_type=3
```yml
Company : Amazon, Etsy
Difficulty : Easy
Question Type : 
Title : Total Cost Of Orders
```

- My solution
```
perfectly solved
```
```sql
select 
    c.id,
    c.first_name,
    SUM(o.total_order_cost)
from customers c
join orders o on c.id=o.cust_id
group by id
order by c.first_name;
```

- Analyze
```
Easy
```


