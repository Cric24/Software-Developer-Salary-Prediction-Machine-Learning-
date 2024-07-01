import streamlit as st
import random  # Import the random module to select a random response

# Define a dictionary of questions and their corresponding answers
qa_pairs = {
    "hi": ["Hello! How can I help you?", "Hi there! What can I assist you with?", "Hi! What brings you here today?", "Hey! What's up?"],
    "how are you?": ["I'm doing well, thanks for asking!", "I'm fine, how about you?", "All good, thank you!"],
    "what is a programming language?": "A programming language is a formal language comprising a set of instructions that produce various kinds of output.",
    "what is software development?": "Software development is the process of conceiving, specifying, designing, programming, documenting, testing, and bug fixing involved in creating and maintaining applications, frameworks, or other software components.",
    "what is version control?": "Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.",
    "what is object-oriented programming (OOP)?": "Object-oriented programming (OOP) is a programming paradigm based on the concept of 'objects', which can contain data and code: data in the form of fields (often known as attributes), and code in the form of procedures (often known as methods).",
    "what is a database?": "A database is an organized collection of data, typically stored and accessed electronically from a computer system.",
    "what is a web framework?": "A web framework is a software framework that is designed to support the development of web applications including web services, web resources, and web APIs.",
    "what is agile?": "Agile is a methodology used in software development that emphasizes flexibility, customer collaboration, and incremental delivery of software.",
    "what is test-driven development (TDD)?": "Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: first the developer writes an automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards.",
    "what is continuous integration (CI)?": "Continuous Integration (CI) is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily - leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible.",
    "what is bug?": "In software development, a bug is an error, flaw, failure, or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways.",
}

# Function to handle user queries and provide answers
def answer_question(question):
    question = question.lower()
    if question in qa_pairs:
        answer = qa_pairs[question]
        if isinstance(answer, list):
            return random.choice(answer)  # Return a random response from the list of responses
        else:
            return answer
    else:
        return "Sorry, I don't have an answer to that question."

# Function to display the chat interface
def chat_interface():
    st.title("Ask Questions about Software Development")

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input("You:")
    if st.button("Send"):
        answer = answer_question(question)
        st.session_state.chat_history.append(f"You: {question}")
        st.session_state.chat_history.append(f"Dhoni Bot: {answer}")

    st.text_area("Chat History", value="\n".join(st.session_state.chat_history), height=300, max_chars=None, key=None)
    if st.button("Clear History"):
        st.session_state.chat_history = []

# Main function
if __name__ == "__main__":
    chat_interface()
