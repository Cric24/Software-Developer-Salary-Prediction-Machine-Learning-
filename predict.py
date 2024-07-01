import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data['model']
le_country = data['le_country']
le_dev = data['le_dev']
le_education = data['le_education']

def show_predict():
    st.title("Salary Prediction")
    
    st.write("""### Please enter the required information to predict the salary""")
    
    
    countries = (
'United States of America',                               
'Germany',                                                  
'United Kingdom of Great Britain and Northern Ireland',     
'Canada',                                                   
'India',                                                    
'France',                                                   
'Brazil',                                                   
'Netherlands',                                              
'Australia',                                                
'Spain',                                                    
'Poland',                                                    
'Sweden',                                                    
'Italy',                                                     
'Switzerland',                                               
'Denmark',                                                   
'Norway',                                                    
'Israel',                                                    
'Portugal',                                                  
'Austria',                                                   
'Finland',                                                   
'Russian Federation',                                        
'Belgium',                                                   
'Ukraine',                                                                                               
'New Zealand',                                               
'Turkey',                                                    
'Greece',                                                    
'South Africa',                                              
'Romania',                                                   
'Mexico',                                                                                                    
'Ireland',                                                   
'Colombia',                                                  
'Argentina',                                                 
'Bulgaria',                                                 
'Pakistan',                                                                                
'Serbia',                                                    
'Japan',                                                                                                     
'China',                                                     
'Indonesia',                                                 
'Bangladesh',                                                
'Croatia',                                                  
'Slovenia',                                                  
'Singapore',                                                 
'Slovakia',                                                
'Chile',                                                     
'Estonia',                                                  
'Philippines',                                             
'Malaysia',                                                 
'Viet Nam',
'Taiwan',  
'Nigeria',
'Latvia',  
'Georgia', 
'Sri Lanka',
    )
    
    dev_types = (
        'Developer, full-stack',
        'Developer, front-end',
        'Developer, back-end',
        'Data scientist or machine learning specialist',
        'Engineer, data',
        'Developer, mobile',
        'Developer, desktop or enterprise applications',
        'Engineer, site reliability',
        'Other',
        'Other (please specify):',
        'Developer, embedded applications or devices',
        'Engineering manager',
        'DevOps specialist',
        'Developer, QA or test',
        'Academic researcher',
        'Data or business analyst',
        'Educator',
        'Senior Executive (C-Suite, VP, etc.)',
        'Developer, game or graphics',
        'Cloud infrastructure engineer'
    )
    
    education = (
        "Master's degree", 
        "Bachelor's degree", 
        'Less than a Bachelors',
    )
    
    country = st.selectbox("Country", countries)
    dev_type = st.selectbox("Type of job", dev_types)
    education = st.selectbox("Education Level", education)
    
    experience = st.slider("Years of Experience", 0, 20, 3)
    
    ok = st.button("Calculate Salary")
    
    if ok:
        X = np.array([[country, dev_type, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_dev.transform(X[:,1])
        X[:, 2] = le_education.transform(X[:,2])
        X = X.astype(float)
        
        salary = regressor.predict(X)
        st.subheader(f"THE ESTIMATED SALARY IS ${salary[0]:.2f}")
    
        
    st.write("""**DISCLAIMER:** This Prediction is done using a Survey Data Collected on Stackoverflow in 2023 so the Estimated Salary is with respect to exchange rates at the time of the survey.""")
        
