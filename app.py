import streamlit as st
from auth import register_user, login_user

st.set_page_config(page_title="Enterprise Transmission System", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid Credentials")

def register_page():
    st.title("Register")

    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")

    if st.button("Register"):
        success = register_user(username, password)
        if success:
            st.success("Registration Successful")
        else:
            st.error("Username already exists")

if not st.session_state.logged_in:
    menu = st.sidebar.selectbox("Select Option", ["Login", "Register"])

    if menu == "Login":
        login_page()
    else:
        register_page()

else:
    st.title("Power Transmission Intelligence System")
    st.success("Logged In Successfully")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("Use sidebar to navigate modules.")
