# 💻 Laptop Prices and Types Analysis
## 📊 Overview

- This project focuses on analyzing a dataset of laptops collected from various brands to identify patterns based on hardware specifications, screen resolution, weight, price, and more. The goal is to explore how various features affect laptop pricing and popularity using data cleaning and visualization techniques.

## 📁 Dataset

- Source: Kaggle

- **Link: https://www.kaggle.com/datasets/ehtishamsadiq/uncleaned-laptop-price-dataset?select=laptopData.csv**

## 🧹 Exploratory Data Analysis (EDA)

- To perform this analysis, I used the Kaggle API to fetch the dataset programmatically. The original dataset includes the following features:

## 📌 Attributes:

- Company, TypeName, Inches, ScreenResolution, Cpu, Ram, Memory, Gpu, OpSys, Weight, Price

## 🧼 Cleaning Steps:

- Corrected spelling errors

- Converted data types (e.g., removed units from RAM and Weight)

- Extracted new columns from composite fields (e.g., separated Memory into Storage and Storage Type)

- Removed missing values and unnecessary columns

## 📁 Project Structure
- LaptopAndPrices.py        # Main script for data cleaning and visualization  
- uncleaned_laptop.csv      # Original dataset file

## 📊 Visualizations
### 1. Most Used Operating Systems (Bar Chart)
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/d1bd38ea-2345-4cc2-beff-3a21bbaa5402" />

### 2. Most Common Screen Resolutions (Bar Chart)
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/83277ff9-3d98-4aaf-83c4-37c0efd2d76c" />

### 3. Top 5 Screen Resolutions by Operating System (Stacked Bar Chart)
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/efcefe10-0f38-4871-bddd-7c74aa754ae0" />

### 4. Price vs. Storage (Scatter Plot)

- Assumption of positive trend between storage capacity and laptop price
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/c62897fc-8fe6-459b-a539-bc1fe9e4d539" />

### 5. Price vs. Weight (Scatter Plot)

- Assumption correlation between laptop weight and price
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/378ef86c-3954-4b7a-bd67-6c767773d21e" />


## ⚙️ Methodology

- Used Pandas for data cleaning and transformation

- Visualized insights using Matplotlib and Seaborn

- Fetched data directly via Kaggle API

- Engineered two new features:

- Storage (in GB)

- Storage Type (HDD, SSD, Hybrid, etc.)

## ✅ Results & Insights

- Windows is the most commonly used OS (over 1000 entries)

- Full HD is the most popular screen resolution (~400 occurrences)

- Unknown Screen Resolutions appear frequently across OS types, but Full HD dominates among Windows devices

- Storage shows a positive correlation with Price

- Weight also appears to influence Price, assuming heavier laptops with higher specs cost more

## 📚 Learnings

- Strengthened my skills in data wrangling using pandas

- Gained experience in building visual insights from raw data

- Practiced using real-world messy data and deriving structure from it

- Learned how to use Kaggle’s API for accessing datasets programmatically
