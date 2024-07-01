
import streamlit as st
from datetime import datetime

def feedback_form():
    st.title("Feedback Form")

    # Collect user feedback
    feedback = st.text_area("Please provide your feedback:")

    # Add a button to submit feedback
    if st.button("Submit Feedback"):
        # Process the feedback (store it in a file in this example)
        save_feedback(feedback)
        st.success("Thank you for your feedback!")

def save_feedback(feedback):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("feedback.txt", "a") as file:
        file.write(f"{timestamp}: {feedback}\n")
