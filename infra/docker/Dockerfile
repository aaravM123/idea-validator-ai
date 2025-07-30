# Step 1: Use an official Python image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy your app folder
COPY ./app ./app

# Step 5: Set the default command to run FastAPI
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
