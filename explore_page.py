import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    
    return categorical_map

def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral degree' in x:
        return 'Post graduate'
    return 'Less than a Bachelors'


@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel","YearsCodePro","Employment","ConvertedComp","CompFreq", "UndergradMajor"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == 'Employed full-time']
    df = df.drop("Employment", axis=1)
    
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    return df

df = load_data()

def show_explore():
    st.title("Explore Mean Salary ")

    st.write(
        """
    Stack overflow survey 2023
    """
    )


    

    st.write("""
             Mean salary based on Countries
             """
             )
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.area_chart(data) 

    st.write("""
             Mean salary based on Experience
             """
             )
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
    

    st.write("""
             Mean salary based on Period
             """
             )
    data = df.groupby(["CompFreq"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data) 

    st.write("""
             Mean salary based on Undergrade Major
             """
             )
    data = df.groupby(["UndergradMajor"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data) 




