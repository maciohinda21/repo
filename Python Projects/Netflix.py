# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/Python%20Projects/netflix_data.csv")

# Create a DF with movies only, filter for movies of 1990s
movies_only = netflix_df[netflix_df['type'] == 'Movie']
df1990 = movies_only[(movies_only['release_year'] >= 1990) & (movies_only['release_year'] <= 1999)]
duration_counts = df1990['duration'].value_counts()

#Create a plot of distribution of durations
plt.figure(figsize=(10, 6))
plt.hist(df1990['duration'], bins=range(0, 160, 10), edgecolor='black')
plt.title('Distribution of Durations')
plt.xlabel('Duration')
plt.ylabel('Count')
plt.xticks(range(0, 160, 10))
plt.show()
action1990 = df1990[df1990['genre'] == 'Action']
count_cases = action1990[action1990['duration'] < 90].shape[0]
print(count_cases)
duration = 110
short_movie_count = 7