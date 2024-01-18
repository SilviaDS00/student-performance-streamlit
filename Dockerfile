FROM python:3.8
RUN pip install streamlit pandas scikit-learn==1.2.2 joblib==1.3.2
COPY src/app.py /app/
COPY model/student_model.pkl /app/model/student_model.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]