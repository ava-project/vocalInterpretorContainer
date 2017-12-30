# Use of latest version of debian as a parent image
FROM ubuntu:zesty

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
RUN apt-get -y install python python-dev python-pip
RUN apt-get -y install git perl bison apt-utils wget
RUN apt-get -y install build-essential swig libpulse-dev unzip

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip numpy scipy setuptools wheel
RUN pip install --upgrade tornado pocketsphinx

#RUN git clone --recursive https://github.com/cmusphinx/pocketsphinx-python/
#RUN cd pocketsphinx-python && python3.6 setup.py install

# Make sphinxtrain installations
RUN ./installbase.sh
RUN ./installtrain.sh
RUN ./installpocketsphinx.sh

# Set the author
MAINTAINER AVA_Sphinx<ava_2018@labeip.epitech.eu>

# Env variables
ENV PATH /usr/local/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/lib
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig

