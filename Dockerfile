FROM python:3.8

# Crea y activa el entorno virtual
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
WORKDIR /app

# Instala las bibliotecas
RUN pip install --upgrade pip
RUN pip install streamlit pandas scikit-learn matplotlib seaborn joblib

# Copia la aplicación y el modelo
COPY src/app.py /app/
COPY model/student_model.pkl /app/model/student_model.pkl

# Configura el directorio de trabajo y el punto de entrada
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
