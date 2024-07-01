import streamlit as st
import requests
from bs4 import BeautifulSoup

def display_interview_questions():
    # URL of the page containing software developer interview questions
    url = "https://www.geeksforgeeks.org/software-developer-interview-questions/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <h2> tags containing questions
    questions = soup.find_all("h2")

    # Filter questions and store in a list
    filtered_questions = []
    for question in questions:
        text = question.text.strip()
        if "Python3" not in text:  # Exclude questions containing "Python3"
            filtered_questions.append(text)

    # Exclude the first 10 questions
    filtered_questions = filtered_questions[10:]

    # Display questions in Streamlit
    st.title("Software Developer Interview Questions")
    for index, question in enumerate(filtered_questions, start=1):
        st.write(f"Question {index}: {question}")

# Call the method to display questions when the script runs
if __name__ == "__main__":
    display_interview_questions()
