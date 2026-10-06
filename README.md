# Week 3: Python & Data Wrangling Assignment

This repository contains the solution for the Week 3 assignment on Data Wrangling and Visualization using *Pandas, **Matplotlib, and **Seaborn*.

## 📁 Repository Structure
* data.csv - The raw fitness and health tracking dataset.
* assignment.py - The Python script containing data cleaning, filtering, and visualization code.
* README.md - Project documentation and summary report.

---

## 🛠️ Data Wrangling & Cleaning Tasks Performed

### 1. Handled Missing Values
* *Calories Column:* Checked for missing entries and filled them using the statistical *median* of the column to prevent data skewness from outliers.
* *Date Column:* Dropped rows where the Date field was missing (e.g., Row 24) as it is a critical index for timeseries analysis.
* *Format Standardization:* Handled date formatting errors (e.g., converting text/integer date 20201226 in Row 28 into standard YYYY-MM-DD timestamp format).

### 2. Row Filtering & Outlier Removal
* Identified an extreme outlier in the Duration column where a workout session was recorded as *450 minutes* (Row 9).
* Filtered the dataset to only include realistic workout durations between *30 and 120 minutes* for accurate performance analysis.

### 3. Feature Engineering (Created New Columns)
* Created a new performance metric column named *Pulse_Intensity_Ratio* using the formula:
  \[\text{Pulse Intensity Ratio} = \left( \frac{\text{Pulse}}{\text{Maxpulse}} \right) \times 100\]
  This helps analyze how close a workout session came to the user's maximum cardiovascular limit.

---

## 📊 Data Visualizations (Matplotlib & Seaborn)

The script automatically generates three dynamic plots using Seaborn's whitegrid theme:
1. *Histogram:* Shows the distribution and density of calories burned across all sessions.
2. *Scatter Plot:* Visualizes the bivariate relationship between workout *Duration* and *Calories Burned, color-coded by **Pulse* rates.
3. *Bar Plot:* Displays the daily chronological trend of the *Maximum Pulse* throughout the month.