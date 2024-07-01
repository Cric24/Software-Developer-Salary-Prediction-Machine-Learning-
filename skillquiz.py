import streamlit as st

# Define the questions and their options
questions = {
    "Which of the following is a statically typed programming language?": ["Java", "Python", "JavaScript", "Ruby"],
    "What does IDE stand for in software development?": ["Integrated Development Environment", "Interpreted Development Environment", "Intelligent Design Environment", "Interactive Development Environment"],
    "Which version control system is commonly used in software development for managing source code?": ["Git", "SVN (Subversion)", "CVS (Concurrent Versions System)", "Mercurial"],
    "What does MVC stand for in web development?": ["Model View Controller", "Multiple View Configuration", "Model View Component", "Main View Configuration"],
    "Which of the following is NOT a software development methodology?": ["Spaghetti", "Waterfall", "Agile", "Scrum"],
    "What is the primary purpose of unit testing in software development?": ["To test individual units or components of code", "To test the user interface", "To test the integration of different modules", "To test the performance of the application"],
    "Which programming language is commonly used for building Android mobile applications?": ["Java", "Swift", "C#", "Kotlin"],
    "What does API stand for in software development?": ["Application Programming Interface", "Advanced Program Interaction", "Automated Program Invocation", "Application Programming Instruction"],
    "Which of the following is NOT a software testing technique?": ["Blue-box testing", "White-box testing", "Black-box testing", "Grey-box testing"],
    "Which design pattern is used to ensure that a class has only one instance and provides a global point of access to that instance?": ["Singleton", "Factory Method", "Observer", "Prototype"]
}


# Function to display the skill assessment quiz
def display_quiz(questions):
    user_responses = {}
    for question, options in questions.items():
        user_response = st.radio(question, options)
        user_responses[question] = user_response
    return user_responses

# Function to calculate and display the assessment results
def calculate_results(user_responses, questions):
    st.header("Skill Assessment Results")
    for question, user_response in user_responses.items():
        st.write(f"Question: {question}")
        st.write(f"Your Answer: {user_response}")
        correct_answer = questions[question][0]
        if user_response == correct_answer:
            st.write("Correct!")
        else:
            st.write("Incorrect")
            st.write(f"Correct Answer: {correct_answer}")

# Main code block
def quiz():
    st.title("Skill Assessment Quiz")
    st.write("Take the quiz to assess your skills in various topics.")

    # Display the quiz questions
    user_responses = display_quiz(questions)

    # Add a button to submit the answers
    if st.button("Submit Answers"):
        # Calculate and display the assessment results
        calculate_results(user_responses, questions)

if __name__ == "__main__":
    quiz()
