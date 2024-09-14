FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the contents of the 'flask_project' directory to /app in the container
COPY flask_project/ /app

EXPOSE 5000
CMD ["python", "app.py"]