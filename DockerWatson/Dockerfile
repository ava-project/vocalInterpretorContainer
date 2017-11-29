# Use an official Python runtime as a parent image
FROM python:3.6

# create working directory
RUN mkdir -p /Watson

# Set the working directory to /Sphinx
WORKDIR /Watson

# Add the working directory
ADD . /Watson

# Install any needed packages specified for python and pocketsphinx
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential swig libpulse-dev git perl bison apt-utils

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Set the author
MAINTAINER AVA_Watson<ava_2018@labeip.epitech.eu>

CMD ["python3.6","-m","ava_server"]
