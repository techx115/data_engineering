# Use an official Python image with pre-installed data science packages
FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

# Install necessary Python libraries
RUN pip install -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy your application code to the container
COPY . /app

#ENV CMAKE_ARGS="-DLLAMA_METAL=on"
#
#RUN pip install wurlitzer pandas duckdb==0.9.2

# Set the entry point to your application
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]