import pandas as pd
import os

# Get the current script folder
base_dir = os.path.dirname(os.path.abspath(__file__))

# ✅ Correct CSV file path inside data folder
csv_path = os.path.join(base_dir, '..', 'data', 'booking_hotels_merged.csv')

# Read the CSV
df = pd.read_csv(csv_path)

# Fill missing or empty 'currency' values with 'PKR'
if 'currency' in df.columns:
    df['currency'] = df['currency'].fillna('PKR')
    df['currency'] = df['currency'].replace('', 'PKR')
    print("✅ Filled missing currency values with 'PKR'.")
else:
    print("⚠️ Column 'currency' not found in the CSV file.")

# Save cleaned CSV
output_path = os.path.join(base_dir, '..', 'data', 'booking_hotels_merged_cleaned.csv')
df.to_csv(output_path, index=False)

print(f"✅ Cleaning complete! File saved as: {output_path}")
