import streamlit as st
import openai
from webscrapp import display_interview_questions  # Import the display_interview_questions function



# Main code block
def Question():
    

    # Call the function to display existing questions
    display_interview_questions()

    st.title("Generate Interview Questions for Software Developers")
    
    # button to trigger question generation
    if st.button("Generate Questions"):
        # Call the function to generate questions
        generated_questions = generate_questions()

        # Display the generated questions in Streamlit
        st.title("Newly Generated Interview Questions")
        for index, question in enumerate(generated_questions):
            st.write(f"{question}")

if __name__ == "__main__":
    Question()
