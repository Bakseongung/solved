### 2254_Missing Values in Data Set
https://platform.stratascratch.com/technical/2254-missing-values-in-data-set
```yml
Company : Here Technologies
Difficulty : Easy
Question Type : Technical
Title : Missing Values in Data Set
```

- My solution
```
Generally, I use `dropna` to handle missing values, but when following specific model guidelines, 
I use MSE for regression models and log-loss for classification models.
```

- Analyze
```
The intention of the problem was to follow the Python Padnas Dataframe commands.
It seems my approach was incorrect.
The solution proposed by user 'WilmaTrainbelate1':
```
```
Identifying missing values in a dataset is dependent on
the type of software or programming language the analyst is dealing with.
In pandas, identifying missing data is as simple as, ‘dataframe.isnull().sum()’.
This code returns the number of missing values within each column, that is, if any exists.
In Microsoft excel, the ISNA() function can be used to find missing values.
The formula looks thus: IF ( ISNA ( VLOOKUP ( cell_value , list , 1 , 0 )), "Missing" , "Is There" ).
Remember, finding missing values is all software dependent.
```
