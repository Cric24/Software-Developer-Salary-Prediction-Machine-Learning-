import streamlit as st
import openai

# Set the OpenAI API key
api_key = "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"
openai.api_key = api_key

def generate_job_listings():
    st.title("Software Developer Job Listings")
    
    # Define the prompt asking for software developer jobs
    prompt = "Generate software developer job listings."

    # Generate text based on the prompt using the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the Davinci model
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=200,  # Maximum length of the generated text
        n=5,  # Number of completions to generate
        stop=None,  # Stop generating when encountering this token
    )

    # Display the generated job listings in Streamlit
    for i, completion in enumerate(response['choices'], 1):
        st.subheader(f"Job Listing {i}")
        st.write(completion['message']['content'].strip())

