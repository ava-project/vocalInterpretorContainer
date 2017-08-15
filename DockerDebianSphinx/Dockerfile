# Use of latest version of debian as a parent image
FROM python:3.6

# create working directories
RUN mkdir -p /Sphinx
RUN mkdir -p /Sphinx/Mounted

# Set the working directory to /Sphinx
WORKDIR /Sphinx

# Add the working directory
ADD . /Sphinx

# Install any needed packages specified for python and pocketsphinx
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python-pip python-dev
RUN apt-get -y install build-essential swig libpulse-dev git perl bison apt-utils

# Install any needed packages numpy and scipy
RUN apt-get install -y python-numpy python-scipy

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make sphinxtrain installations
RUN ./installbase.sh
RUN ./installtrain.sh

# Set the author
MAINTAINER AVA_Sphinx<ava_2018@labeip.epitech.eu>
