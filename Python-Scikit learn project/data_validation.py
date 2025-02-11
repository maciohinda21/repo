import csv
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

# Path to the CSV file
file_path = "C:\\Users\\macio\\Downloads\\product_sales.csv" 

data = pd.read_csv(file_path)

# Create a KNN Imputer object
imputer = KNNImputer(n_neighbors=5)  # You can adjust the number of neighbors as needed

# Select the columns to use for finding nearest neighbors (exclude 'revenue' column)
columns_for_imputation = ['week', 'sales_method', 'nb_sold', 
                         'years_as_customer', 'nb_site_visits', 'state']

# Encode categorical variables (if necessary)
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

# Save the imputed data to a new CSV file (optional)
data.to_csv("C:\\Users\\macio\\Downloads\\imputed_product_sales.csv", index=False) 
