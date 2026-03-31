### 2084_DELETE and TRUNCATE
https://platform.stratascratch.com/technical/2084-delete-and-truncate
```yml
Company : Southwest Airlines
Difficulty : Easy 
Question Type : Technical
Title : DELETE and TRUNCATE
```

- My solution
```
`DELETE` deletes a specific row, while `TRUNCATE` deletes all rows.
```

- Analyze
```
I hadn't even considered the possibility of a rollback.
I liked dataquest135's answer:
```
```
Truncate removes all the rows of a table with only schema intact,
whereas Delete can remove specific row(s) of a table by Where clause
Truncate operation cannot rollback, whereas Delete can revert/undo.
Truncate is a DDL(Data Definition Language) ,
focus on structure of schema/table; on the contrary,
Delete is a DML (Data Manipulate Language),
focus more on data entries in a table.
```
