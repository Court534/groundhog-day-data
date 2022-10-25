import pandas as pd
import numpy as np
import sqlite3

## Using pandas to read the data from a CSV file and print the results to the console
df = pd.read_csv("C:/Users/CourtneyStow/OneDrive - JCW Resourcing/Desktop/groundhog-day-data.csv")

path_to_date = 'C:/Users/CourtneyStow/OneDrive - JCW Resourcing/Desktop/'
groundhog_data = pd.read_csv(path_to_date + 'groundhog-day-data.csv')
print('groundhog_data_shape:', groundhog_data.shape)

print(df.info())

conn = sqlite3.connect("groundhog-day-data.db")
cur = conn.cursor()

# cur.execute('''
#           CREATE TABLE groundhogdata
#           ([year] INTEGER PRIMARY KEY, [punxsutawney_phil] TEXT, [feb_average_temp] TEXT, [march_average_temp] TEXT)
#           ''')
                     
# conn.commit()

# cur.execute('''
#           INSERT INTO groundhogdata (year, punxsutawney_phil, feb_average_temp, march_average_temp)

#                 VALUES
#                 (2001,'Full Shadow', '33.98', '41.49'),
#                 (2002,'Full Shadow', '36.39', '39.54'),
#                 (2003,'Full Shadow', '32.79', '43.03'),
#                 (2004,'Full Shadow', '33.57', '47.41'),
#                 (2005,'Full Shadow', '37.94', '42.31'),
#                 (2006,'Full Shadow', '34.83', '42.62'),
#                 (2007,'No Shadow', '32.41', '47.66'),
#                 (2008,'Full Shadow', '34.07', '41.86'),
#                 (2009,'Full Shadow', '36.77', '42.87'),
#                 (2010,'Full Shadow', '31.80', '43.57'),
#                 (2011,'No Shadow', '33.04', '43.07'),
#                 (2012,'Full Shadow', '37.51', '50.41'),
#                 (2013,'No Shadow', '34.77', '40.91'),
#                 (2014,'Full Shadow', '32.13', '40.51'),
#                 (2015,'Full Shadow', '32.99', '45.39'),
#                 (2016,'No Shadow', '39.47', '47.05')
#           ''')
# conn.commit()

cur.execute('''
          SELECT
          year,
          punxsutawney_phil,
          feb_average_temp,
          march_average_temp
          FROM groundhogdata
          ''')

df = pd.DataFrame(cur.fetchall(), columns=['year','punxsutawney_phil', 'feb_average_temp', 'march_average_temp'])
conn.commit()

## Accessing the information from the database with pandas
df = pd.read_sql_query("SELECT * from groundhogdata", conn)

## Verify that the result of the SQL query is stored in the dataframe
print(df)

conn.close()