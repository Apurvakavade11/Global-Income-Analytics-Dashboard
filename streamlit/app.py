import streamlit as st

st.set_page_config(page_title="Global Income Inequality Dashboard", layout="wide")

st.title("🌍 Global Income Inequality Analytics Dashboard")

st.markdown("""
This project analyzes global income inequality using World Bank data
such as **Gini Index** and **GDP per capita**.
""")

st.header("📊 Dashboard Preview")

st.image("../screenshots/page1_overview.png", caption="Global Income Inequality Overview", use_container_width=True)
st.image("../screenshots/page2_comparison.png", caption="Country-wise Comparison", use_container_width=True)
st.image("../screenshots/page3_trends.png", caption="Income Inequality Trends Over Time", use_container_width=True)

st.header("🔍 Key Insights")
st.markdown("""
- Income inequality differs significantly across countries  
- Higher GDP does not always indicate lower inequality  
- Developing countries tend to show higher Gini Index values  
""")

st.header("🛠 Tools Used")
st.markdown("""
- Power BI  
- Python  
- Streamlit  
- World Bank Open Data  
""")
