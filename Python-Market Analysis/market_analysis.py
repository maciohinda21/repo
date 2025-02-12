# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a data frame and group by months
df = pd.read_csv('https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/Python-Market%20Analysis/real_product_sales.csv')
df['month'] = pd.to_datetime(df['month']).dt.year
year_str = df.groupby('month')['workout_worldwide'].sum().idxmax()

# Finding the most popular keyword in 2020
df = pd.read_csv('https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/Python-Market%20Analysis/three_keywords.csv')
df['month'] = pd.to_datetime(df['month']).dt.year
df_2020 = df[df['month'] == 2020]
home_workout_sum = df_2020['home_workout_worldwide'].sum()
gym_workout_sum = df_2020['gym_workout_worldwide'].sum()
home_gym_sum = df_2020['gym_workout_worldwide'].sum()
keyword_sums = {
    'home_workout_worldwide': home_workout_sum,
    'gym_workout_worldwide': gym_workout_sum,
    'home_gym_worldwide': gym_workout_sum
}

peak_covid = max(keyword_sums, key=keyword_sums.get)
most_popular_value = keyword_sums[peak_covid]

print(f"The most popular keyword in 2020 is {peak_covid} with a value of {most_popular_value}.")

# Find the most popular keyword in 2023
df_2023 = df[df['month'] == 2023]
home_workout_sum = df_2023['home_workout_worldwide'].sum()
gym_workout_sum = df_2023['gym_workout_worldwide'].sum()
home_gym_sum = df_2023['gym_workout_worldwide'].sum()
keyword_sums = {
    'home_workout_worldwide': home_workout_sum,
    'gym_workout_worldwide': gym_workout_sum,
    'home_gym_worldwide': gym_workout_sum
}

current = max(keyword_sums, key=keyword_sums.get)
most_popular_value1 = keyword_sums[current]
print(f"The most popular keyword in 2023 is {current} with a value of {most_popular_value}.")
