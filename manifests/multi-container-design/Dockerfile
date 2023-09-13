# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application to the /app/ directory
ADD ["app.py", "/app/"]

# Create the logs directory
RUN mkdir /app/logs/

# Define the command to run the web server when the container starts
CMD ["python", "app.py"]
