import streamlit as st
import pandas as pd
import sqlite3

# Database connection
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

# Create tables
c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS feedback(name TEXT, message TEXT)")

st.title("🌍 Global Income Inequality Analytics Dashboard")

menu = ["Home","Dashboard","Download Data","Feedback","Login","Register"]
choice = st.sidebar.selectbox("Menu", menu)

# HOME PAGE
if choice == "Home":
    st.header("🌍 Global Income Inequality Analytics Dashboard")

    st.write("""
    This project analyzes global income inequality using economic indicators such as **GDP** and **Gini Index**.
    
    The goal of this project is to understand how income and wealth are distributed across different countries 
    and how economic growth relates to inequality levels.
    """)

    st.subheader("Project Objectives")

    st.write("""
    • Analyze global income distribution across countries  
    • Compare GDP and inequality indicators  
    • Visualize economic trends over multiple years  
    • Identify disparities between developed and developing regions  
    """)

    st.subheader("Tools Used")

    st.write("""
    • Python for data processing  
    • Power BI for dashboard visualization  
    • Streamlit for web application development  
    • World Bank Open Data as the dataset source  
    """)

    st.success("Use the navigation menu on the left to explore the dashboard, download data, and provide feedback.")

# DASHBOARD PAGE
elif choice == "Dashboard":
    st.header("Dashboard Preview")

    st.image("screenshots/page1_overview.png")
    st.image("screenshots/page2_comparison.png")
    st.image("screenshots/page3_trends.png")

# DOWNLOAD DATA
elif choice == "Download Data":
    st.header("Download Dataset")

    df = pd.read_csv("cleaned_data.csv")
    st.dataframe(df.head())

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="income_data.csv",
        mime="text/csv",
    )

# FEEDBACK
elif choice == "Feedback":
    st.header("Submit Feedback")

    name = st.text_input("Your Name")
    message = st.text_area("Your Feedback")

    if st.button("Submit"):
        c.execute("INSERT INTO feedback VALUES (?,?)",(name,message))
        conn.commit()
        st.success("Thank you for your feedback!")

# LOGIN
elif choice == "Login":
    st.header("User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        c.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
        result = c.fetchone()

        if result:
            st.success("Login Successful")
        else:
            st.error("Invalid credentials")

# REGISTER
elif choice == "Register":
    st.header("Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        c.execute("INSERT INTO users VALUES (?,?)",(new_user,new_pass))
        conn.commit()
        st.success("Account Created Successfully")