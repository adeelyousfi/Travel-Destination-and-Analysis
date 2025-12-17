import pandas as pd
import numpy as np

# === Load Data ===
file_path = "../data/31octdata.csv"   # adjust if your file is elsewhere
df = pd.read_csv(file_path)

print("🔍 Dataset loaded successfully!")
print(f"📊 Rows: {len(df)}, Columns: {len(df.columns)}")

# === Step 1: Remove exact duplicate rows ===
initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"🗑️ Exact duplicates removed: {initial_rows - len(df)}")

# === Step 2: Remove near-duplicates (same city_name + hotel_name) ===
before = len(df)
df = df.drop_duplicates(subset=['city_name', 'hotel_name'], keep='first')
print(f"🏨 Duplicate hotels per city removed: {before - len(df)}")

# === Step 3: Clean link_domain column ===
df['link_domain'] = df['link_domain'].astype(str)
df['link_domain'] = df['link_domain'].str.extract(r'(booking\.com|agoda\.com|expedia\.com|hotels\.com)', expand=False)
df['link_domain'].fillna('other', inplace=True)

# === Step 4: Standardize text casing ===
df['city_name'] = df['city_name'].astype(str).str.title().str.strip()
df['hotel_name'] = df['hotel_name'].astype(str).str.title().str.strip()
df['rating_category'] = df['rating_category'].astype(str).str.lower().str.strip()
df['availability_status'] = df['availability_status'].astype(str).str.lower().str.strip()

# === Step 5: Clean hotel_rating column ===
df['hotel_rating'] = pd.to_numeric(df['hotel_rating'], errors='coerce')
invalid_ratings = df['hotel_rating'].isna().sum()
df.dropna(subset=['hotel_rating'], inplace=True)
df = df[df['hotel_rating'].between(0, 10)]
print(f"⭐ Invalid hotel_rating entries removed: {invalid_ratings}")

# === Step 6: Clean num_reviews ===
df['num_reviews'] = pd.to_numeric(df['num_reviews'], errors='coerce')
before = len(df)
df.dropna(subset=['num_reviews'], inplace=True)
df = df[df['num_reviews'] >= 0]
upper_limit = df['num_reviews'].quantile(0.99)
df = df[df['num_reviews'] <= upper_limit]
print(f"💬 Removed outliers or invalid num_reviews entries: {before - len(df)}")

# === Step 7: Standardize Currency ===
df['currency'] = 'PKR'

# === Step 8: Encode categorical columns for ML ===
from sklearn.preprocessing import LabelEncoder

encoders = {}
categorical_cols = ['city_name', 'rating_category', 'availability_status', 'link_domain']
for col in categorical_cols:
    le = LabelEncoder()
    df[col + '_encoded'] = le.fit_transform(df[col])
    encoders[col] = le
print("🧠 Categorical columns encoded for ML use.")

# === Step 9: Save cleaned dataset ===
output_path = "../data/cleaned_ready_for_analysis.csv"
df.to_csv(output_path, index=False)
print(f"💾 Cleaned dataset saved to: {output_path}")

# === Step 10: Summary ===
print("\n📈 SUMMARY REPORT")
print(f"✅ Final Rows: {len(df)}")
print(f"✅ Final Columns: {len(df.columns)}")
print(f"📊 City Count: {df['city_name'].nunique()}")
print(f"🏨 Unique Hotels: {df['hotel_name'].nunique()}")
print(f"🌐 Domains: {df['link_domain'].unique()}")
print("✨ Dataset ready for Power BI, Analysis, and ML Prediction.")
