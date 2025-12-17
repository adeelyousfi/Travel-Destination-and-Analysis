import pandas as pd
import numpy as np

# -----------------------------
# 1. Load Dataset
# -----------------------------
file_path = "1411.csv"     # change path if needed
df = pd.read_csv(file_path)

print("Initial Shape:", df.shape)
print(df.head())


# -----------------------------
# 2. Remove Columns You Mentioned
# -----------------------------
cols_to_remove = ['rating_category_cleaned', 'is_popular', 'is_top_rated']

for col in cols_to_remove:
    if col in df.columns:
        df.drop(columns=[col], inplace=True)

print("After Removing Unwanted Columns:", df.shape)


# -----------------------------
# 3. Remove Duplicate Rows
# -----------------------------
df = df.drop_duplicates()
print("After Removing Duplicates:", df.shape)


# -----------------------------
# 4. Check Missing Values
# -----------------------------
print("Missing Values Before Cleaning:\n", df.isnull().sum())

# Drop rows if essential data missing
essential_cols = ['city', 'rating']  # adjust if needed
df = df.dropna(subset=[col for col in essential_cols if col in df.columns])

# Fill numeric NaN using median
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill categorical NaN using mode
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing Values After Cleaning:\n", df.isnull().sum())


# -----------------------------
# 5. Standardize Text Columns
# -----------------------------
def clean_text(text):
    if isinstance(text, str):
        return text.strip().lower()
    return text

text_columns = ['city', 'country', 'location', 'hotel_name']  # only if exist
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].apply(clean_text)


# -----------------------------
# 6. Remove Invalid & Dirty Data
# -----------------------------
# Rating should be 0–5
if 'rating' in df.columns:
    df = df[(df['rating'] >= 0) & (df['rating'] <= 5)]

# Remove empty city names
if 'city' in df.columns:
    df = df[df['city'].notna() & (df['city'] != "")]

print("After Removing Invalid Data:", df.shape)


# -----------------------------
# 7. Convert Data Types
# -----------------------------
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

if 'price' in df.columns:
    df['price'] = pd.to_numeric(df['price'], errors='coerce')


# -----------------------------
# 8. Outlier Removal (IQR)
# -----------------------------
def remove_outliers(df, col):
    if col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        return df[(df[col] >= lower) & (df[col] <= upper)]
    return df

df = remove_outliers(df, 'price')

print("After Removing Outliers:", df.shape)


# -----------------------------
# 9. Final Cleanliness Check
# -----------------------------
print("\nFinal Missing Values:\n", df.isnull().sum())
print("\nFinal Data Types:\n", df.dtypes)
print("\nFinal Shape:", df.shape)

# Save cleaned file
df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as cleaned_dataset.csv")
