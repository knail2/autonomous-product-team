# Use an official Python image
FROM python:3.9.18-slim

# Set the working directory
WORKDIR /app

# Copy this dir to the workdir
COPY . /app

# install packages
#RUN pip install -r requirements.txt
RUN pip install --trusted-host pypi.python.org pyautogen requests
RUN apt-get update && apt-get install -y iputils-ping net-tools

# run cmd
CMD ["python", "code/basic.py"]


