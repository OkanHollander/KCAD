# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory's contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose port 80 for the web server to listen on
EXPOSE 80

# Define the command to run the web server when the container starts
CMD ["python", "webapp.py"]
