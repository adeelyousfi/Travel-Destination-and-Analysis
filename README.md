
# Travel Destination Analysis - Hotel Rating & Price Analysis

## Project Overview

This project automates the collection and analysis of hotel data from Booking.com using Python web scraping. It applies machine learning (Linear Regression) to analyze pricing trends and presents interactive visualizations using Microsoft Power BI.

**Goal:** Help travelers and analysts understand hotel pricing patterns, service availability, and the relationship between hotel ratings and prices across different cities.

---

## Key Features

- **Automated Web Scraping:** Python scripts using Requests + BeautifulSoup to extract hotel data (price, rating, location, services) from Booking.com
- **Data Preprocessing:** Cleaned and standardized data using Pandas (handled missing prices, removed duplicates, standardized currency to USD)
- **Machine Learning:** Linear Regression to analyze relationship between price, rating, and city
- **Interactive Dashboard:** Power BI visualizations including bar charts, maps, scatter plots, and dynamic filters
- **End-to-End Workflow:** Web scraping → Data cleaning → ML analysis → Visualization

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Web Scraping | Python, Requests, BeautifulSoup |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn (Linear Regression) |
| Visualization | Microsoft Power BI |
| Version Control | Git, GitHub |

---

## Project Structure

```
Travel-Destination-and-Analysis/
├── anaylsis.py              # ML analysis script
├── cleaner.py               # Data cleaning script
├── cleaner_next_stage.py    # Advanced cleaning
├── merge_csv_files.py       # Data merging utility
├── final.csv                # Cleaned dataset
└── README.md                # Project documentation
```

---

## Data Collection Methodology

### Initial Challenges
- Multiple hotel websites provided incomplete or unstructured data
- Some platforms restricted access or lacked pagination

### Why Booking.com Was Selected
- Well-structured hotel listing cards
- Key attributes available: price, rating, location, services
- Supports pagination for large-scale data collection
- Global city coverage

---

## Data Preprocessing Steps

1. Missing prices handled using realistic imputation
2. All prices standardized to USD for consistency
3. Duplicate city entries removed
4. Partial results saved periodically to prevent data loss
5. Data types standardized for numerical analysis

---

## Machine Learning Analysis

### Algorithm Used: Linear Regression

**Why Linear Regression?**
- Simple and easy to interpret
- Suitable for numerical prediction tasks
- Efficient for large datasets
- Helps identify relationships between variables

**Key Findings:**
- Hotel prices tend to increase with higher ratings
- Prices vary significantly by city (popular cities = higher prices)
- Weak to moderate relationship between ratings and review counts

---

## Power BI Dashboard

The interactive dashboard includes:

| Visual Element | Purpose |
|----------------|---------|
| Card visuals | Total hotels, average rating |
| Bar charts | Compare hotels across cities and rating categories |
| Map visual | Geographical distribution of hotels |
| Scatter plot | Relationship between ratings and reviews |
| Slicers | Dynamic filtering by city, rating, price |

---

## Results & Insights

- Some cities have significantly higher hotel concentration
- High hotel ratings do not always correspond to large number of reviews
- Rating categories provide clear classification of hotel quality
- Hotel availability varies across locations and categories

---

## How to Run This Project

### Prerequisites

```bash
pip install requests beautifulsoup4 pandas scikit-learn numpy
```

### Run Data Cleaning

```bash
python cleaner.py
python cleaner_next_stage.py
```

### Run Machine Learning Analysis

```bash
python anaylsis.py
```

### View Power BI Dashboard

1. Open Power BI Desktop
2. Load `final.csv`
3. Explore the pre-built visuals or create your own

---

## Contributors

| Name | Role |
|------|------|
| Muhammad Sarim (2212152) | Data Collection, Web Scraping |
| Adeel Hasan Yousfi (2212242) | Data Preprocessing, ML Analysis, Power BI Dashboard |

**Submitted to:** Sir Ahsan Nisar

---

## What This Project Demonstrates

| Skill | Evidence |
|-------|----------|
| Python Web Scraping | Requests + BeautifulSoup scripts |
| Data Cleaning | Pandas preprocessing code |
| Machine Learning | Linear Regression with Scikit-learn |
| Data Visualization | Power BI dashboard |
| End-to-End Project | Complete workflow from scraping to insights |
| Collaboration | Two-person team with clear role division |

---

## Future Improvements

- Add more cities and hotels to dataset
- Experiment with advanced ML models (Random Forest, XGBoost)
- Deploy Power BI dashboard online for public access
- Automate weekly data updates

---

## References

- [Booking.com](https://www.booking.com) - Primary data source
- Python Software Foundation - Python for Data Analysis
- Microsoft Power BI Documentation
