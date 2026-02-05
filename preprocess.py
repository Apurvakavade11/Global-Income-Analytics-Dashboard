import pandas as pd

# -----------------------------
# Load World Bank datasets
# -----------------------------
gini = pd.read_csv("data/gini.csv", skiprows=4)
gdp = pd.read_csv("data/gdp.csv", skiprows=4)

# -----------------------------
# Keep only required years
# -----------------------------
years = [str(y) for y in range(2000, 2023)]

gini = gini[["Country Name", "Country Code"] + years]
gdp = gdp[["Country Name", "Country Code"] + years]

# -----------------------------
# Convert wide data to long format
# -----------------------------
gini_long = gini.melt(
    id_vars=["Country Name", "Country Code"],
    var_name="Year",
    value_name="Gini_Index"
)

gdp_long = gdp.melt(
    id_vars=["Country Name", "Country Code"],
    var_name="Year",
    value_name="GDP_per_Capita"
)

# -----------------------------
# Merge datasets
# -----------------------------
merged = pd.merge(
    gini_long,
    gdp_long,
    on=["Country Name", "Country Code", "Year"]
)

# -----------------------------
# Data cleaning
# -----------------------------
merged.dropna(inplace=True)
merged["Year"] = merged["Year"].astype(int)

# -----------------------------
# Save cleaned data
# -----------------------------
merged.to_csv("data/cleaned_income_data.csv", index=False)

print("✅ Data preprocessing completed successfully")
