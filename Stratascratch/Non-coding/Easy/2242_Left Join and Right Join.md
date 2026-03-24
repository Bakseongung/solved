### 2242_Left Join and Right Join
https://platform.stratascratch.com/technical/2242-left-join-and-right-join/discussion
```yml
Company : Credit Acceptance 
Difficulty : Easy
Question Type : Technical
Title : Left Join and Right Join
```

- My solution
```
A left join is the sum of the difference between A and B, as well as the intersection of A and B.
A right join is the sum of the difference between B and A, as well as the intersection of B and A.
```

- Analyze
```
I hadn't realized that the table on the right was filled with null values.
The following answer could be the collect one.
```
```
With a left join,
all of the rows from the left table will be returned and the missing values from the right table will be filled with NULL values.
Meanwhile,
a right join is the opposite of a left join,
where all of the rows from the right table will be returned and the missing values from the left table will be filled with NULL values.
```
