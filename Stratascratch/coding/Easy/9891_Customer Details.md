### 9891_Customer Details
https://platform.stratascratch.com/coding/9891-customer-details?code_type=1
```yml
Company : Apple, Amazon
Difficulty : Easy
Question Type : 
Title : Customer Details
```

- My solution
```
perfecly solved
```
```sql
select
    first_name,
    last_name,
    city,
    order_details
from customers
left join orders on customers.id=orders.cust_id
order by first_name, order_details;
```

- Analyze
```
There don't seem to be any issues.
```

<br>
