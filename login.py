import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from predict import show_predict
from voice import run_voice_feedback  
from explore_page import show_explore
from check import currency_converter

from data_analysis_app import csv
from skillquiz import quiz
from interview import Question
from job import generate_job_listings
from chatbot import chat_interface



# Check if the Firebase app is already initialized
if not firebase_admin._apps:
    # Initialize the Firebase app
    cred = credentials.Certificate(r"C:\Users\Ext\Desktop\salary-prediction\authentication-47928-firebase-adminsdk-lhzxj-4b676cb6a0.json")
    firebase_admin.initialize_app(cred)

    

# Function to perform signup
def signup(email, password):
    # Check if the password meets the required criteria
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    
    try:
        user = auth.create_user(email=email, password=password)
        return "Your user ID is: " + user.uid
    except auth.EmailAlreadyExistsError:
        return "Email already exists"

# Function to perform login
def login(email, password):
    try:
        # Authenticate user with Firebase Authentication
        user = auth.get_user_by_email(email)
        if user:
            # Sign in user with provided email and password
            user = auth.update_user(user.uid, password=password)
            return user.uid, user.email
    except auth.UserNotFoundError:
        return "User not found", ""
    except ValueError:
        return "Incorrect password", ""

# Function to check if the user is logged in
def is_logged_in():
    return "user_id" in st.session_state

def main():
    

    # If user is not logged in, show signup and login forms
    if not is_logged_in():
        # Signup form
        with st.sidebar.form("signup_form"):
            st.write("Sign Up")
            email_signup = st.text_input("Email (signup)", key="signup_email")
            password_signup = st.text_input("Password (signup)", type="password", key="signup_password")
            signup_button = st.form_submit_button("Signup")
        
        if signup_button:
            signup_result = signup(email_signup, password_signup)
            st.sidebar.write(signup_result)
        
        # Login form
        with st.sidebar.form("login_form"):
            st.write("Login")
            email_login = st.text_input("Email (login)", key="login_email")
            password_login = st.text_input("Password (login)", type="password", key="login_password")
            login_button = st.form_submit_button("Login")
        
        if login_button:
            login_result, email = login(email_login, password_login)
            if login_result and login_result != "Incorrect password":
                if login_result != "User not found":
                    st.session_state["user_id"] = login_result
                    st.session_state["user_email"] = email
                    st.sidebar.success("Login successful!")
                else:
                    st.sidebar.error("Login failed. Please check your email and password.")
                
            else:
                st.sidebar.error("Login failed. Please check your email and password.")
    else:
        st.sidebar.write("Logged in as:", st.session_state["user_email"])

    # Render dropdown with all options if logged in, else only show Predict
    if is_logged_in():
        selected_page = st.sidebar.selectbox("Select Page", ["Predict", "Explore", "Currency Converter", "Feedback", "Data Analysis", "Skill Quiz", "Interview Questions", "Chat"])
    else:
        selected_page = "Predict"

    # Render content based on the selected page
    if selected_page == "Predict":
        show_predict()
    elif selected_page == "Explore":
        show_explore()
    elif selected_page == "Currency Converter":
        currency_converter()
    elif selected_page == "Feedback":
        run_voice_feedback()
   
    elif selected_page == "Data Analysis":
        csv()
    elif selected_page == "Skill Quiz":
        quiz()
    elif selected_page == "Interview Questions":
        Question()
   
    elif selected_page == "Chat":
        chat_interface()
if __name__ == "__main__":
    main()
