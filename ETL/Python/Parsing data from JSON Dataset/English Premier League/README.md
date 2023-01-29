# "English Premier League"- season match stats 2017/2018
### Extract data from "English Premier League" semi-structed (JSON) dataset, parse, transform and load into an Excel file.

***Hi,Friends***
I am going to show you getting data from semi-structed (JSON) dataset, parse, transform and load into an Excel file
Steps:
1. Extracting data from JSON dataset
2. Parsing and Transforming
3. Loading into an Excel file.

***Used tools:***<br>
1. Jupyter Notebook
2. Pyton (Pandas Library)

JSON dataset content:
"English Premier League"-season match stats 2017/2018

![image](https://user-images.githubusercontent.com/60735401/215338209-e1eb446d-579c-473c-97a1-85ad94016394.png)

***First of all***

We need Jupyter notebook. We can follow the steps with different application or tools. The Jupyter notebook is one of the powerful web application for data purpose
1.	We have to import pandas.
2.	Use “read_json” function to convert JSON string to pandas object. 

![image](https://user-images.githubusercontent.com/60735401/215338281-125577ec-7b93-42b4-925e-7cf42bf0f057.png)
<h4 align="center">Pic:1</h1>

The output is not understandable because keys of JSON are defined as indexes instead of columns.
In this case, we have to use orient="index" and replace indexes to columns and columns to indexes.

***orient="index"*** – defines indexes as columns<br>
***head(10) function*** – retriving 10 rows.<br>

![image](https://user-images.githubusercontent.com/60735401/215338309-c2a2f6b5-cc51-43fb-a62d-4b56578c5d6a.png)
<h4 align="center">Pic:2</h1>

So, we extracted and parsed the JSON dataset into a readable and understandable form.<br>
Now, it's time to transform data.
Let’s try to get date, time, day, month, year parts from 'date_string' column.

***Used functions:***<br>
1. pd.to_datetime - converting argument/string/object to datetime data type.<br>
2. dt.date - extracts date part from datetime.<br>
3. dt.day -  extracts day part from datetime.<br>
4. dt.month_name() - extracts month part (with name) from datetime.<br>
5. dt.year - extracts year part from datetime.<br>
6. dt.time - extracts time part from datetime.<br>

We need to add new columns and assign extracted value with above function to it.<br> 

***New columns:***<br> 

df['match_date'] =<br> 
df['day'] =<br> 
df['month'] =<br> 
df['year'] =<br> 
df['time'] =<br> 

In Python, if you want to add new column to the pandas object you have to define column name and assign value to it. If new column name is existing column name in this case the existing column name will be updated, if there is no any matched column name with new column name then it will be added as a new column.

![image](https://user-images.githubusercontent.com/60735401/215339766-5ca25ef0-9950-4083-9985-4b5a45c23043.png)
<h4 align="center">Pic:3</h1>

***Continue transformation.***<br>
Let’s concatenate parentheses with ***'half_time_score'*** and ***'full_time_score'*** values.<br>
***df['half_time_score']*** = ***'(' + df[['half_time_score']] + ')'*** <br>
***df['full_time_score']*** = ***'(' + df[['full_time_score']] + ')'*** <br>
After that add new ***“match result “*** column and concatenate ***'home_team_name'*** and ***'away_team_name'*** column values with the values of ***'full_time_score'*** column.<br>
***df['match result']*** = ***df['home_team_name'] +' '+ df['full_time_score'] +' '+ df['away_team_name']***
