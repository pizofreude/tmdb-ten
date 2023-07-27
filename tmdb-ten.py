# Here's ETL script about ten movies from TMDB API

# Import necessary libraries
import pandas as pd
import requests
import config
import json

# EXTRACT
# Send a single GET request to the API
response_list = []
API_KEY = config.api_key

# In response, we receive a JSON record with the ten movie_id ranges from 878 to 888

for movie_id in range(878,888):
  """loop that requests a movie one at a time and appends the response to response_list"""
  url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, API_KEY)
  r = requests.get(url)
  response_list.append(r.json())

# Create a pandas dataframe from the records using from_dict()
df = pd.DataFrame.from_dict(response_list)
# print(df)
# Here we get dirty date with 10 rows x 25 columns

# TRANSFORM
# We didn't need all 25 columns, only the important one. Refer to: https://developer.themoviedb.org/docs/search-and-query-for-details
# In summary, we need: title, overview, release_date, id, imdb_id, genres, runtime, budget, revenue, vote_count, vote_average, popularity.
# Create a new list for selected columns above named df_columns to save selected columns we want from the main dataframe.
# df_columns = ['title', 'overview', 'release_date', 'id', 'imdb_id', 'genres', 'runtime', 'budget', 'revenue', 'vote_count', 'vote_average', 'popularity' ]
# print(df_columns) -> genres is a column of JSON records lists. Need cleaning.

# Clean genres list
genres_list = df['genres'].tolist()
flat_list = [item for sublist in genres_list for item in sublist]

result = []
for l in genres_list:
    r = []
    for d in l:
        r.append(d['name'])
    result.append(r)
df = df.assign(genres_all=result)

df_genres = pd.DataFrame.from_records(flat_list).drop_duplicates()

# new df_columns without 'genres' attribute
df_columns = ['title', 'overview', 'release_date', 'id', 'imdb_id', 'runtime', 'budget', 'revenue', 'vote_count', 'vote_average', 'popularity']
# append genres attribute to df_columns
df_genre_columns = df_genres['name'].to_list()
df_columns.extend(df_genre_columns)
# create the genre columns and join them onto the main table.
s = df['genres_all'].explode()
df = df.join(pd.crosstab(s.index, s))

# expand out the datetime column into a table.
# Pandas has built-in functions to extract specific parts of a datetime.
df['release_date'] = pd.to_datetime(df['release_date'])
df['day'] = df['release_date'].dt.day
df['month'] = df['release_date'].dt.month
df['year'] = df['release_date'].dt.year
df['day_of_week'] = df['release_date'].dt.day_name()
df_time_columns = ['id', 'release_date', 'day', 'month', 'year', 'day_of_week']

# LOAD
# Export results as three csv files
df[df_columns].to_csv('tmdb_ten_movies.csv', index=False)
df_genres.to_csv('tmdb_ten_genres.csv', index=False)
df[df_time_columns].to_csv('tmdb_ten_datetimes.csv', index=False)

