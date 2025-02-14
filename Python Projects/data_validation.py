import csv
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

# Path to the CSV file.
file_path = "https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/Python-Scikit%20learn%20project/product_sales.csv" 

data = pd.read_csv(file_path)

# Create a KNN Imputer object
imputer = KNNImputer(n_neighbors=5)  # Number of neigbors can be adjusted

# Select the columns to use for finding nearest neighbors (exclude 'revenue' column)
columns_for_imputation = ['week', 'sales_method', 'nb_sold', 
                         'years_as_customer', 'nb_site_visits', 'state']

# Encode categorical variables
le = LabelEncoder()
for col in ['sales_method', 'state']:
    data[col] = le.fit_transform(data[col])

# Create a KNN Imputer object
imputer = KNNImputer(n_neighbors=5) 

# Fit and transform the data using selected columns
data_for_imputation = data[columns_for_imputation + ['revenue']]
data_for_imputation = imputer.fit_transform(data_for_imputation)

# Update the 'revenue' column in the original DataFrame
data['revenue'] = data_for_imputation[:, -1] 

# Convert 'revenue' to numeric with 2 decimal places
data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').round(2) 

# Print the data with imputed values
print(data)

# [Optional] Save the imputed data to a new CSV file. Replace placeholder with your folder path
data.to_csv("[PLACEHOLDER]\\imputed_product_sales.csv", index=False) 
