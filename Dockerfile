FROM python:3.11-slim

WORKDIR /app

COPY ./streamlit.py /app/app.py

RUN pip install --no-cache-dir streamlit

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]