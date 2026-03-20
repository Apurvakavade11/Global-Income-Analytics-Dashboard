import streamlit as st
import pandas as pd
import sqlite3

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Global Income Dashboard", layout="wide")

# ---------------- PROFESSIONAL CSS ----------------
st.markdown("""
<style>

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #1f4e79;
}

/* Sidebar text (ALL WHITE) */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Radio buttons text */
div[role="radiogroup"] label {
    color: white !important;
    font-size: 18px !important;
}

/* Sidebar title (Navigation) */
section[data-testid="stSidebar"] label {
    color: white !important;
    font-size: 20px !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS feedback(name TEXT, message TEXT)")

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
def login_page():
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<h1>🌍 Global Income Dashboard</h1>", unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)

        menu = ["Login", "Register"]
        choice = st.radio("", menu, horizontal=True)

        if choice == "Login":
            st.subheader("🔐 Login")

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
                data = c.fetchone()

                if data:
                    st.session_state.logged_in = True
                    st.success("Login Successful")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

        elif choice == "Register":
            st.subheader("📝 Register")

            new_user = st.text_input("Username")
            new_pass = st.text_input("Password", type="password")

            if st.button("Register"):
                c.execute("INSERT INTO users VALUES (?,?)", (new_user, new_pass))
                conn.commit()
                st.success("Account Created! Please login.")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MAIN APP ----------------
def main_app():
    st.markdown("<h1>🌍 Global Income Inequality Dashboard</h1>", unsafe_allow_html=True)

    menu = ["🏠 Home", "📊 Dashboard", "📥 Download Data", "💬 Feedback", "🚪 Logout"]
    choice = st.sidebar.radio("Navigation", menu)

    # ---------------- HOME ----------------
    if choice == "🏠 Home":
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("📌 About Project")
            st.write("""
            This project analyzes global income inequality using GDP and Gini Index.
            It helps understand wealth distribution across countries.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🎯 Objectives")
            st.write("""
            - Analyze income inequality  
            - Compare countries  
            - Identify trends  
            - Visualize disparities  
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

        col3, col4, col5 = st.columns(3)

        with col3:
            st.markdown('<div class="card">📊 Data: World Bank</div>', unsafe_allow_html=True)

        with col4:
            st.markdown('<div class="card">⚙️ Tools: Python, Power BI</div>', unsafe_allow_html=True)

        with col5:
            st.markdown('<div class="card">🚀 Output: Dashboard + Web App</div>', unsafe_allow_html=True)

    # ---------------- DASHBOARD ----------------
    elif choice == "📊 Dashboard":
        st.subheader("Dashboard Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.image("screenshots/page1_overview.png", use_container_width=True)

        with col2:
            st.image("screenshots/page2_comparison.png", use_container_width=True)

        st.markdown("---")
        st.image("screenshots/page3_trends.png", use_container_width=True)

    # ---------------- DOWNLOAD ----------------
    elif choice == "📥 Download Data":
        st.subheader("Download Dataset")

        try:
            df = pd.read_csv("../data/cleaned_income_data.csv")

            st.dataframe(df.head(), use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name="income_data.csv",
                mime="text/csv"
            )

        except:
            st.error("File not found. Place cleaned_income_data.csv in streamlit folder.")

    # ---------------- FEEDBACK ----------------
    elif choice == "💬 Feedback":
        st.subheader("Feedback")

        name = st.text_input("Your Name")
        message = st.text_area("Your Feedback")

        if st.button("Submit"):
            c.execute("INSERT INTO feedback VALUES (?,?)", (name, message))
            conn.commit()
            st.success("Feedback submitted!")

    # ---------------- LOGOUT ----------------
    elif choice == "🚪 Logout":
        st.session_state.logged_in = False
        st.rerun()

# ---------------- APP FLOW ----------------
if st.session_state.logged_in:
    main_app()
else:
    login_page()