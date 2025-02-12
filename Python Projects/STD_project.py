# Libraries
import pandas as pd

# Read in the data
schools = pd.read_csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/Python%20Projects/schools.csv")

# Preview the data
schools.head()

#Best NYC schools in math
# Convert the average_math column to numeric values, handling non-numeric values
schools['average_math'] = pd.to_numeric(schools['average_math'], errors='coerce')

# Drop rows with NaN values in average_math
schools = schools.dropna(subset=['average_math'])

# Filter the dataframe where average_math is higher than 640
best_math_schools = schools[schools['average_math'] > 640]

# Select the required columns and sort the dataframe
best_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)

# Display the resulting dataframe
print(best_math_schools)

#Top 10 overall
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by='total_SAT', ascending=False).head(10)
print(top_10_schools)

#Most deviant borough
borough_stats = schools.groupby('borough').agg(
    num_schools=('school_name', 'size'),
    average_SAT=('total_SAT', 'mean'),
    std_SAT=('total_SAT', 'std')
).reset_index()

# Find the borough with the largest standard deviation
largest_std_dev = borough_stats.loc[borough_stats['std_SAT'].idxmax()]

# Convert the result to a DataFrame
largest_std_dev = pd.DataFrame([largest_std_dev])

# Round numeric values to two decimal places
largest_std_dev[['average_SAT', 'std_SAT']] = largest_std_dev[['average_SAT', 'std_SAT']].round(2)

# Display the resulting dataframe
print(largest_std_dev)