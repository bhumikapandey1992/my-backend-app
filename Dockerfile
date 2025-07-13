# Stage 1: Build the python dependencie
FROM python:3.11-slim-bullseye AS build 

# Set environment variables for python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container for this stage
WORKDIR /app

# Install system dependencies required for mysqlclient and other build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file into the container
COPY requirements.txt .

# Install python dependencies listed in requirements.txt
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the final image
FROM python:3.11-slim-buster

# Set the working directory for the final image
WORKDIR /app

# Copy the isntalled python dependencies fromt he build stage to the final image
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy django project into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the django applicating using gunicorn
CMD ["gunicorn","myproject.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "300", "--workers", "3"]
