10024_Wine varieties tasted by 'Roger Voss'.md

```yml
Company : Wine Magazine
Difficulty : Easy
Question Type : 
Title : Wine varieties tasted by 'Roger Voss'
```

- My solution
```sql
select distinct variety
from winemag_p2
where taster_name='Roger Voss'
and region_1 is not null;
```

- Analyze
```
Easy
```

