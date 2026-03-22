### 10176_Bikes Last Used
https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=3
```yml
Company : Lyft, DoorDash
Difficulty : Easy
Question Type : 
Title : Bikes Last Used
```

- My solution
```
select
    bike_number,
    max(end_time) as last_used
from dc_bikeshare_q1_2012
group by bike_number
order by last_used desc;
```

- Analyze
```
It seems there's almost nothing to criticize.
```
