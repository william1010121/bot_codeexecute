# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install gcc and g++ for compiling C++ code
RUN apt-get update && apt-get install -y gcc g++

# Install the Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Copy the .env file into the container
COPY .env .env

# Command to run the bot
CMD ["python", "bot.py"]
