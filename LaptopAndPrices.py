# Importing the required modules.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re # Importing new module.
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

# Assigning the Operating system into each of it
df['OpSys'] = df['OpSys'].str.capitalize()
df['OpSys'] = df['OpSys'].str.replace("Macos|Mac os x", "Mac OS",regex=True).str.strip()
df.loc[df['OpSys'].isin(["Windows 10", "Windows 7","Windows 1", "Windows 10 s"]),"OpSys"] = "Windows OS"

df['Weight'] = df['Weight'].str.replace(r'[^\d\.]', '', regex=True)  # Keep only digits and dot
df['Weight'] = df['Weight'].str.strip() # Removes empty spaces.
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce') # converts values to numeric and replaces null for empty value

# Cleaning ScreenResolution data
df['ScreenResolution'] = df['ScreenResolution'].str.replace(r'\d+|x', '', regex=True).str.strip() # Removes numbers and x
df['ScreenResolution'] = df['ScreenResolution'].str.replace('K', '4K').str.strip() # Re arranging the Valid value
df['ScreenResolution'] = df['ScreenResolution'].replace('', "Unkown")

# Checking the result. 
print(df['ScreenResolution'].unique())

# Cleaning the Memory Data
# Expanding the table
df[['Storage','Storage Type']] = df['Memory'].str.split(" ",n=1, expand= True)
# Result of both the expanded tables.
df['Storage'] = df['Storage'].str.replace('[^a-zA-Z0-9|.]'," ", regex=True).str.strip()
df.loc[df['Storage Type'].str.contains(r"\+",case=False, na= False),'Storage Type'] = "Dual"
print(df['Storage'].unique())
print(df['Storage Type'].unique())

# Removing the empty value
df = df.dropna()
df = df.drop(columns=["Memory"])
# Changing the required data Types.
df['Weight'] = df['Weight'].astype(float)
print(df.isnull().sum())

# Cleaned Data Types
print(df.dtypes)
print(df.tail())


plt.figure(figsize=(8,6))
# Now making the necessary graphs.
MostOSUsed = df['OpSys'].value_counts().reset_index()
MostOSUsed.columns = ['OpSys','Count']

# Using seaborn for barchart plotting and label.
ax = sns.barplot(x= 'OpSys', y ='Count' ,data=MostOSUsed, color = 'green' )
for bar in ax.patches:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2,
            height,
            f'{height:.0f}',
            ha = 'center',
            va = 'bottom') 

plt.title("Most Used Operating System")
plt.xlabel("OpSys")
plt.ylabel("Counts")
plt.tight_layout()

# Making bar graph for ScreenResolution.
plt.figure(figsize=(8,6))
MostSRUsed = df['ScreenResolution'].value_counts().head(5).reset_index() # Gives the top 5 results.
MostSRUsed.columns = ['ScreenResolution','Counter']

# Plotting the bar graph.
ax2 = sns.barplot(x= 'ScreenResolution', y ='Counter' ,data=MostSRUsed, color = 'red' )
for bar in ax2.patches:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2,
            height,
            f'{height:.0f}',
            ha = 'center',
            va = 'bottom')

# Writing the title and labeling it.
plt.title("Screen Resolution best in use")
plt.xlabel("Screen Resoulution")
plt.ylabel("Counter")
plt.xticks(fontsize = 8)
plt.tight_layout()

# Stacked Bar Chart. 
# Top 5 Screen Resolution
top5_Resolution = df["ScreenResolution"].value_counts().head(5).index.to_list() # Gives top 5 results.
# Creating pivot table from top 5 values using OpSys Index.
cound_df = df.pivot_table(index= "OpSys", columns= "ScreenResolution", aggfunc= "size",fill_value= 0)
top5_df = cound_df[top5_Resolution] # Top 5 results.

# MComstructing the figure.
ax4 = top5_df.plot(kind= 'bar',stacked= True,figsize= (8,10),colormap= 'tab20')

# Labeling the stacked bar chart figure.
for bar in ax4.patches:
    width = bar.get_width()
    height = bar.get_height()
    x = bar.get_x()
    y = bar.get_y()
    if height > 10:
        ax4.text(x+ width/2,
             y + height/2,
             f'{height:.0f}',
             ha = 'center',
             va = 'center',
             fontsize = 9,
             color = 'black')

# Proper title and labeling.        
plt.ylabel("Count")
plt.xlabel("Screen Resolution and operating system")
plt.xticks(fontsize = 6)
plt.title("Count of top 5 screenResolution per operating system")
plt.tight_layout()

# Finding the relationship between price and storage.
# Using lambda and re module to covert tb into gb.
df['Storage'] = df['Storage'].apply(
    lambda a: int(re.search(r"(\d+)",a).group()) * (1024 if "TB" in a.upper() else 1))


# Constructing the scatter plot.
windows_df = df[df["Company"]== "Apple"] # Only apple data.
plt.figure(figsize=(8,6))
# Making it with seaborn.
sns.scatterplot(data = windows_df, x = "Storage",y = "Price")
plt.title("The relationship between Storage and and price.")

# Scatter plot with matplot to find the relationship between weight and price.
plt.figure(figsize=(8,6))
plt.scatter(df['Weight'],df["Price"])
plt.title("The relationship between Weight and Price")
plt.xlabel("Price")
plt.ylabel("Weight")


plt.show()

