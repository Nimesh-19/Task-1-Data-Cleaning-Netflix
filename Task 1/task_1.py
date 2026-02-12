'''
Task 1: Data Cleaning and Preprocessing
Objective: Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats).
Tools: Excel / Python (Pandas)
'''

import pandas as pd

df =  pd.read_csv("Task 1/netflix_titles.csv")
print(df.head())

print("Dataset Info:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Not Specified")
df["rating"] = df["rating"].fillna("Not Rated")

df = df.dropna(subset=["title"])


text_columns = ["type", "country", "rating"]

for col in text_columns:
    df[col] = df[col].str.lower().str.strip()


df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

df.columns = df.columns.str.lower().str.replace(" ", "_")

df["release_year"] = df["release_year"].astype(int)

print(df.info())

df.to_csv("cleaned_netflix_dataset.csv", index=False)
