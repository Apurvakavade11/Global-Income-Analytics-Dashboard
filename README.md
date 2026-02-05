# Interactive Analytics Dashboard for Global Income Distribution

## Problem Statement
This project analyzes global income inequality using World Bank data.
An interactive Power BI dashboard is created and integrated with a Streamlit web application
to visualize income distribution, Gini Index trends, and GDP comparisons across countries.

---

## Tech Stack
- Python (Pandas, NumPy)
- Power BI
- Streamlit
- Git & GitHub
- World Bank Open Data

---

## Project Structure
Global-Income-Analytics-Dashboard/
├── data/
│ ├── gini.csv
│ ├── gdp.csv
│ └── cleaned_data.csv
├── powerbi/
│ └── Income_Inequality_Dashboard.pbix
├── preprocess.py
├── streamlit/
│ ├── app.py
│ └── requirements.txt
├── screenshots/
│ ├── page1_overview.png
│ ├── page2_comparison.png
│ ├── page3_trends.png
├── README.md


---

## Dashboard Preview

### Overview Page
![Overview](screenshots/page1_overview.png)

### Country Comparison Page
![Comparison](screenshots/page2_comparison.png)

### Trends Analysis Page
![Trends](screenshots/page3_trends.png)

---

## How to Run the Streamlit App

1. Install required libraries:
```bash
pip install -r streamlit/requirements.txt


## 🌐 Live Demo
Streamlit App: https://global-income-analytics-dashboard-jyocnpj5namrw5myxlaqcd.streamlit.app/
