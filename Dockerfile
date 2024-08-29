FROM python:3.9-slim-buster

WORKDIR /app

COPY src/ /app/src
COPY tests/ /app/tests
COPY games.log /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/report_generator.py"]