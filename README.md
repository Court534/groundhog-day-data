
# Groundhog day Data

Using python pandas and sqlite3 to manipulate data in an SQL table.


## Helpful Documentation

- [Pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)

- [sqlite3 user guide](https://www.sqlite.org/doclist.html)

- [Link to CVS file (Groundhog Day Forecasts and Temperatures)](https://www.kaggle.com/datasets/groundhogclub/groundhog-day)



## User guide/Examples
import the necessary dependencies
```python
import pandas as pd
import sqlite3
```

Using pandas to read the data from a CSV file and print the results to the console (please change file location to where the file is location on your local machine)
```python
df = pd.read_csv("C:/(File Location)/groundhog-day-data.csv")
```

Setting up the connection with sqlite3 and naming the database
```python
conn = sqlite3.connect("groundhog-day-data.db")
cur = conn.cursor()
```

Using sqlite3 commands to create a table "groundhogdata"
```python
cur.execute('''
           CREATE TABLE groundhogdata
           ([year] INTEGER PRIMARY KEY, [punxsutawney_phil] TEXT, [feb_average_temp] TEXT, [march_average_temp] TEXT)
           ''')
                     
conn.commit()
conn.close()
```
Manually adding the values into the database
```python
cur.execute('''
          INSERT INTO groundhogdata (year, punxsutawney_phil, feb_average_temp, march_average_temp)

                VALUES
                (2001,'Full Shadow', '33.98', '41.49'),
                (2002,'Full Shadow', '36.39', '39.54'),
                (2003,'Full Shadow', '32.79', '43.03'),
                (2004,'Full Shadow', '33.57', '47.41'),
                (2005,'Full Shadow', '37.94', '42.31'),
                (2006,'Full Shadow', '34.83', '42.62'),
                (2007,'No Shadow', '32.41', '47.66'),
                (2008,'Full Shadow', '34.07', '41.86'),
                (2009,'Full Shadow', '36.77', '42.87'),
                (2010,'Full Shadow', '31.80', '43.57'),
                (2011,'No Shadow', '33.04', '43.07'),
                (2012,'Full Shadow', '37.51', '50.41'),
                (2013,'No Shadow', '34.77', '40.91'),
                (2014,'Full Shadow', '32.13', '40.51'),
                (2015,'Full Shadow', '32.99', '45.39'),
                (2016,'No Shadow', '39.47', '47.05')
          ''')
conn.commit()
```
Picture below shows the SQLite3 table in VScode using the SQLite Viewer extention





Manually selecting the information we want to look at from the database
```python
cur.execute('''
          SELECT
          year,
          punxsutawney_phil,
          feb_average_temp,
          march_average_temp
          FROM groundhogdata
          ''')
```
Using pandas to select the information we want from the database
```python
df = pd.DataFrame(cur.fetchall(), columns=['year','punxsutawney_phil', 'feb_average_temp', 'march_average_temp'])
conn.commit()
```
Verify that the result of the SQL query is stored in the dataframe and closing the connection
```python
print(df)
conn.close()
```
## Authors

- [@Court534](https://www.github.com/Court534)

