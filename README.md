# COVID-19 Global Data Tracker

## 📌 Project Overview

The **COVID-19 Global Data Tracker** is a data analysis and visualization project that explores global trends in COVID-19 cases, deaths, and vaccinations. Built using Python and real-world data from [Our World in Data](https://ourworldindata.org/covid-data), this project demonstrates how to extract insights from time series data and present findings using charts, maps, and narrative reporting.

## 🎯 Objectives

* Import and clean real-world COVID-19 data
* Analyze trends in cases, deaths, and vaccinations
* Compare data across multiple countries
* Create clear and informative visualizations
* Communicate key insights effectively in a Jupyter Notebook

## 📂 Project Structure

```
COVID-19-Global-Data-Tracker/
│
├── owid-covid-data.csv         # Main dataset (downloaded from OWID)
├── covid19_global_tracker.ipynb # Jupyter notebook with full analysis
├── README.md                   # Project description and instructions
└── output/                     # (Optional) Folder for exported charts or reports
```

## 📊 Tools & Libraries

* **Python 3.7+**
* **Pandas** – data handling
* **Matplotlib / Seaborn** – data visualization
* **Plotly Express** – interactive maps

## 🔧 How to Run

1. Clone this repository or download the files manually.
2. Download the latest `owid-covid-data.csv` from:
   [https://covid.ourworldindata.org/data/owid-covid-data.csv](https://covid.ourworldindata.org/data/owid-covid-data.csv)
3. Place the CSV file in the project root directory.
4. Open the Jupyter Notebook `covid19_global_tracker.ipynb`.
5. Run each cell in order to load data, clean it, and generate visualizations.

## 🌍 Countries Analyzed

This project focuses on:

* 🇰🇪 Kenya
* 🇮🇳 India
* 🇺🇸 United States

These can be changed by modifying the `countries` list in the notebook.

## 📌 Key Features

* Time series plots for total and new cases
* Vaccination progress visualizations
* Death rate computation and analysis
* Optional interactive choropleth map of global case counts
* Markdown cells with insights and summary

## 📈 Sample Insights

* The U.S. had the highest total cases during the observed period.
* India experienced major spikes in mid-2021.
* Kenya had relatively lower case numbers but also slower vaccination uptake.

## 📤 Export Options

You can export the final notebook as a PDF or HTML:

* In Jupyter: `File → Export Notebook As → PDF` or `HTML`

## 🧠 Learning Outcomes

By completing this project, you'll gain experience with:

* Real-world data cleaning and preprocessing
* Time-series data analysis
* Creating compelling charts
* Reporting findings for presentation or publication

## 📃 License

This project is open for educational purposes. The dataset is sourced from [Our World in Data](https://ourworldindata.org/covid-data).

---
