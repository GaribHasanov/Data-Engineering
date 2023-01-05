import pandas as pd
import googletrans
from googletrans import Translator

# getting messy data
df = pd.read_csv('Images-Book.csv',usecols = ['Identifier', 'Edition Statement','Place of Publication','Date of Publication'
,'Publisher','Title', 'Author','Contributors','Shelfmarks' ], keep_default_na = False ,nrows = 200)

# cleansing 'Place of Publication' column
df = df.sort_values(by = ['Place of Publication'],ascending=False)                         # r'.*?\[(.*)].*'
df['Place of Publication'] = df['Place of Publication'].str.lower().str.replace(r'\]', '', regex=True)#implement regex behavior

# importing all cities and measure with df.Place of Publication column
cities = pd.read_csv('world-cities.csv', usecols = ['name']  )
cities['name'] = cities['name'].str.lower()
#cities = cities.sort_values(by = ['name'])

# left join df.Place of Publication column to cities.name column
join_table = df.merge(cities, how = 'left',left_on = 'Place of Publication', right_on = 'name')
# finding null(not matched rows) and clean messy data. We define the messy column by finding not matched rows with cities df
join_table_not_null = join_table[join_table['name'].notnull()] #matched
join_table_null =     join_table[join_table['name'].isnull()]  #notmatched


# Translate 
# Translating not matched rows. Because some of the 'df.Place of Publication 'rows are in different language.
translator = Translator()
join_table_null['Place of Publication'] = join_table_null['Place of Publication'].apply(lambda x: translator.translate(x, dest='en').text).str.lower()

# UnFinished. Need implementation
# Joining again the 'Place of Publication' column with cities df
join_table_2 = join_table_null.merge(cities, how = 'left', left_on = 'Place of Publication', right_on = 'name' )
join_table_2_notnull = join_table_2[join_table_2['name_y'].notnull()] #matched
join_table_2_null =    join_table_2[join_table_2['name_y'].isnull() ] #notmatched
# Next time will use regex and find unmatched similar rows of "Place of Publication" of 'join_table_2_null' object and concat with concat_table object


frames = [join_table_not_null[['Identifier','Edition Statement','Place of Publication','Date of Publication','Publisher','Title','Author','Contributors','Shelfmarks']],join_table_2_notnull[['Identifier','Edition Statement','Place of Publication','Date of Publication','Publisher','Title','Author','Contributors','Shelfmarks']]]
concat_table = pd.concat(frames).drop_duplicates()
concat_table['Place of Publication'] = concat_table['Place of Publication'].str.title()
concat_table.to_excel('book_concating_v3.xlsx', sheet_name = 'Cleansed data',index = False)