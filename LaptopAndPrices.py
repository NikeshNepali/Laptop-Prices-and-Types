# Importing the required modules.
import pandas as pd
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi

# AUthenticating the API
api = KaggleApi()
api.authenticate()  # Uses the kaggle.json file

# Downloading the dataset and assigning it a folder by unzipping it.
api.dataset_download_files(
    "ehtishamsadiq/uncleaned-laptop-price-dataset",
    path='uncleaned_laptop',
    unzip=True
)

# Display of all columns
pd.set_option('display.max_column', None)

# Reading the data.
df = pd.read_csv("uncleaned_laptop/laptopData.csv")

# Describes the overall data in mathematicall sense
print(df.describe())

# Displays first five results.
print(df.head())

# Finding the empty values Before Data Cleaninng
print(df.isnull().sum())

# Display of unique values to do the data cleaning checking STEP
for col in df.columns:
    print(df[col].unique())

print(df['Weight'].unique()) # Checking

# Cleaning data Starts.
df['Weight'] = df['Weight'].str.replace(r'[^\d\.]', '', regex=True)  # Keep only digits and dot
df['Weight'] = df['Weight'].str.strip() # Removes empty spaces.
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce') # converts values to numeric and replaces null for empty value

# Cleaning ScreenResolution data
df['ScreenResolution'] = df['ScreenResolution'].str.replace(r'\d+|x', '', regex=True).str.strip() # Removes numbers and x
df['ScreenResolution'] = df['ScreenResolution'].str.replace('K', '4K') # Re arranging the Valid value

# Checking the result. 
print(df['ScreenResolution'].unique())

# Cleaning the Memory Data
df[['Storage','Storage Type']] = df['Memory'].str.split(" ",n=1, expand= True)
print(df['Storage'].unique())
print(df['Storage Type'].unique())

# Removing the empty value
df = df.dropna()
# Changing the required data Types.
df['Weight'] = df['Weight'].astype(float)
print(df.isnull().sum())

# Cleaned Data Types
print(df.dtypes)

# Changing Data Types
print(df.dtypes)
