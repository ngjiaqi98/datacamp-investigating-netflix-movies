# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# select only needed column
filtered_df = netflix_df[["title","type","country","genre","release_year","duration"]]

# filter data based on type to locate only movies
movies_df = filtered_df[
    (netflix_df['type'] == 'Movie') 
]

# filter movies within year 1990 till 2000
netflix_1990_movies = movies_df[
        (netflix_df['release_year'] >= 1990) 
        & 
        (netflix_df['release_year'] < 2000)
    ]
# print(netflix_1990_movies)

# shape = row count 
netflix_1990_movies.shape

# find mean, median, mode of dataset
mean = netflix_1990_movies['duration'].mean()
median = netflix_1990_movies['duration'].median()
mode = netflix_1990_movies['duration'].mode()[0]
movie_dict = {"mean":mean,"median":median,"mode":mode}
# print(movie_dict)

# set frequency dictionary 
freqs = {}
for dur in netflix_1990_movies['duration']:
    # for loop duration in every row, set duration count = 0; +1 if the duration existed
    freqs[dur] = freqs.get(dur, 0) + 1

# sort the dictionary from most frequent movie duration to least frequent movie duration
freqs = dict(sorted(freqs.items(), key=lambda item:item[1], reverse=True))
# print(freqs)

# set duration = first key which also = mode 
duration = next(iter(freqs.keys()))
duration = mode
print("most frequent movie duration = " , duration)

# filter movie shorter than 90mins 
netflix_1990_short_action_movies = netflix_1990_movies[(netflix_1990_movies['duration']<90) & (netflix_1990_movies["genre"] == "Action")]
short_movie_count = netflix_1990_short_action_movies.shape[0]
print("number of short action movies = ",short_movie_count)
# print(short_movie_count1)

# draw graph
plt.hist(netflix_1990_movies["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()
