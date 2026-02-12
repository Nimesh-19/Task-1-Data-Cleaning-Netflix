'''
Task 1: Data Cleaning and Preprocessing
Objective: Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats).
Tools: Excel / Python (Pandas)
'''
#Import Libraries
import pandas as pd

#Load Dataset
df =  pd.read_csv("netflix_titles.csv")
print(df.head())

#Initial Inspection
print("Dataset Info:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

#Remove Duplicate Rows
df = df.drop_duplicates()

#Handle Missing Values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Not Specified")
df["rating"] = df["rating"].fillna("Not Rated")

#Drop rows where title is missing (critical column)
df = df.dropna(subset=["title"])

#Standardize Text Values
text_columns = ["type", "country", "rating"]

for col in text_columns:
    df[col] = df[col].str.lower().str.strip()

#Convert Date Format
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

#Rename Column Headers
df.columns = df.columns.str.lower().str.replace(" ", "_")

#Fix Data Types
df["release_year"] = df["release_year"].astype(int)

print(df.info())
#Save Cleaned Dataset
df.to_csv("cleaned_netflix_dataset.csv", index=False)
