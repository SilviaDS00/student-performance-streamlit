import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("model/student_model.pkl")

st.title("Prediction of students' academic performance")

gender = st.selectbox("Gender: ", ["female", "male"])
level_education = st.selectbox("Level of education: ", ["some college", "associate's degree", "some high school", 
                                                        "bachelor's degree", "master's degree", "high school"])

prepatation_course = st.checkbox("Preparation course completed ", value=False)
math_score = st.number_input("Math score: ", min_value=0, max_value=100)
reading_score = st.number_input("Reading score: ", min_value=0, max_value=100)
writing_score = st.number_input("Writing score: ", min_value=0, max_value=100)

if prepatation_course:
    prepatation_course = "completed"
else:
    prepatation_course = "none"

st.divider()

if st.button("Predict"):
    X = pd.DataFrame([[gender, level_education, prepatation_course, math_score, reading_score, writing_score]],
                    columns=["gender", "parental level of education", "test preparation course", "math score", "reading score", "writing score"])
    X = X.replace(["female", "male"], [1, 0])
    X = X.replace(["some college", "associate's degree", "some high school", "bachelor's degree", "master's degree", "high school"], 
                  [0, 1, 2, 3, 4, 5])
    X = X.replace(["completed", "none"], [1, 0])
    
    X_original = X.copy()
    prediction = clf.predict(X)[0]
    
    if prediction < 50:
        prediction = "low score, you need to study more!"
    elif prediction >= 50 and prediction < 80:
        prediction = "medium score, you can do it better!"
    else:
        prediction = "high score! Congratulations!"
        
    st.text(f"You have a {prediction}!")