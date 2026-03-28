### 10087_Find all posts which were reacted to with a heart
https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=3
```yml
Company : Meta
Difficulty : Easy
Question Type : 
Title : Find all posts which were reacted to with a heart
```

- My solution
```
perfectly solved
```
```sql
select distinct p.*
from facebook_posts p
join facebook_reactions r on r.post_id=p.post_id
where r.reaction='heart'
```

- Analyze
```
To be honest, i'm not really sure why my code was marked as "perfectly solved".
I think it's inefficient because it uses hash sort to handle duplicate rows.
instead, user M&M 's code is very efficient, so i plan to use it as a reference.
```
```sql
select * from facebook_posts
where post_id IN (select post_id from facebook_reactions WHERE reaction = 'heart')
```
