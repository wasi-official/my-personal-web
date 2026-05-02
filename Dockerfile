# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port $PORT available to the world outside this container
EXPOSE $PORT

# Run gunicorn when the container launches
CMD gunicorn app:app --bind 0.0.0.0:$PORT