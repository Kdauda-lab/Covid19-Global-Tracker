# COVID-19 Global Data Tracker

# 📦 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 📥 2. Load Data
df = pd.read_csv("owid-covid-data.csv")

# 🔍 3. Data Exploration
print("Columns:", df.columns.tolist())
print("\nPreview:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

# 🧹 4. Data Cleaning
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]
df['date'] = pd.to_datetime(df['date'])
df = df.dropna(subset=['date', 'total_cases', 'total_deaths'], how='any')
df.fillna(0, inplace=True)

# ➗ Calculate Death Rate
df['death_rate'] = df['total_deaths'] / df['total_cases']

# 📈 5. Total Cases Over Time
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.show()

# 📉 6. Daily New Cases Comparison
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)
plt.title("Daily New Cases Comparison")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.show()

# 💉 7. Vaccination Progress
plt.figure(figsize=(12, 6))
for country in countries:
    subset = df[df['location'] == country]
    plt.plot(subset['date'], subset['total_vaccinations'], label=country)
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.show()

# 🗺️ 8. Choropleth Map (Latest Date)
latest = df[df['date'] == df['date'].max()]
latest = latest[['iso_code', 'location', 'total_cases']].dropna()
fig = px.choropleth(latest,
                    locations='iso_code',
                    color='total_cases',
                    hover_name='location',
                    title='Global COVID-19 Cases (Latest)',
                    color_continuous_scale='Reds')
fig.show()

# 📝 9. Insights (Markdown Suggestion)
"""
### Key Insights
- 🇺🇸 The US has the highest case count among the selected countries.
- 🇮🇳 India experienced sharp case rises during mid-2021.
- 🇰🇪 Kenya showed slower growth in both cases and vaccinations.

### Observations
- Death rate trends differ by country.
- Vaccination efforts align with declining new cases.
"""
