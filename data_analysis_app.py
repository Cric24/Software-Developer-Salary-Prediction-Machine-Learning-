import streamlit as st
import pandas as pd

def data_analysis(file):
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(file)

    # Display the uploaded data
    st.write("Uploaded Data:")
    st.write(df)

def csv():
    st.title("Data Upload and Analysis")

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data_analysis(uploaded_file)

if __name__ == "__main__":
    csv()
