import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("1411.csv")

# Columns
rating_col = 'hotel_rating'
reviews_col = 'num_reviews'
city_col = 'city_name'
hotel_col = 'hotel_name'

# =============================
# 1. Bar Chart: Top 10 Hotels by Number of Reviews
# =============================
df[reviews_col] = pd.to_numeric(df[reviews_col], errors='coerce')
df_top_reviews = df.dropna(subset=[reviews_col])
top_hotels = df_top_reviews.sort_values(reviews_col, ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=reviews_col, y=hotel_col, data=top_hotels, palette="Blues_d")
plt.title("Top 10 Hotels by Number of Reviews", fontsize=16)
plt.xlabel("Number of Reviews", fontsize=14)
plt.ylabel("Hotel Name", fontsize=14)
plt.tight_layout()
plt.show()

# =========================================
# 2. Bar Chart: Top 10 Cities by Number of Hotels
# =========================================
top_cities = df[city_col].value_counts().head(10).reset_index()
top_cities.columns = [city_col, 'hotel_count']

plt.figure(figsize=(10,6))
sns.barplot(x='hotel_count', y=city_col, data=top_cities, palette="viridis")
plt.title("Top 10 Cities by Number of Hotels", fontsize=16)
plt.xlabel("Number of Hotels", fontsize=14)
plt.ylabel("City", fontsize=14)
plt.tight_layout()
plt.show()

# =========================================
# 3. Scatter Plot: Hotel Rating vs Number of Reviews (Top 50 Hotels)
# =========================================
# Ensure numeric
df[rating_col] = pd.to_numeric(df[rating_col], errors='coerce')
df_scatter = df.dropna(subset=[reviews_col, rating_col])

# Take top 50 hotels by number of reviews
top_hotels_scatter = df_scatter.sort_values(reviews_col, ascending=False).head(50)

plt.figure(figsize=(18,10))  # Full-page size

# Use distinct colors per city
unique_cities = top_hotels_scatter[city_col].unique()
palette = sns.color_palette("tab20", n_colors=len(unique_cities))

sns.scatterplot(
    x=reviews_col,
    y=rating_col,
    hue=city_col,
    data=top_hotels_scatter,
    s=150,        # larger points
    alpha=0.8,
    palette=palette
)

plt.title("Hotel Rating vs Number of Reviews (Top 50 Hotels)", fontsize=20)
plt.xlabel("Number of Reviews", fontsize=16)
plt.ylabel("Hotel Rating", fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12, title="City")
plt.grid(True)
plt.tight_layout()
plt.show()
