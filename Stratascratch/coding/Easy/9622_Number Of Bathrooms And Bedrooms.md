### 9622_Number Of Bathrooms And Bedrooms
https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=1
```yml
Company : Airbnb
Difficulty : Easy
Question Type : 
Title : Number Of Bathrooms And Bedrooms
```

- My solution
```
perfectly solved
```
```sql
select
    city,
    property_type,
    avg(bathrooms) as n_bathrooms_avg,
    avg(bedrooms) as n_bedrooms_avg
from airbnb_search_details
group by city,property_type
```

- Analyze
```
If the problem had required preserving each row or performing comparisons,
it might have been interesting to solve it using 'PARTITION BY'.
However, I decided that using a 'GROUP BY' clause would be more efficient for this problem.
```
```sql
select
    city,
    property_type,
    avg(bathrooms) over (partition by city, property_type) as n_bathrooms_avg,
    avg(bedrooms) over (partition by city, property_type) as n_bedrooms_avg
from airbnb_search_details;
```
