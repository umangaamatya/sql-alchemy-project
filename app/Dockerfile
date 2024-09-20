# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
RUN mkdir -p /app
WORKDIR /app

COPY . .

# Install any necessary dependencies
RUN pip install -r requirements.txt
