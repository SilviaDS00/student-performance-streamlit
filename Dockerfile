FROM python:3.8
RUN pip install streamlit pandas scikit-learn matplotlib seaborn
COPY src/app.py /app/
COPY model/student_model.pkl /app/model/student_model.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]