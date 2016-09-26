FROM ubuntu:latest
MAINTAINER Adele Kapellusch <adelekoutia@gmail.com>
RUN apt-get update
RUN apt-get -y install sudo
RUN sudo apt-get -y install python
RUN sudo apt-get -y install libhdf5-serial-dev
RUN sudo apt-get -y install netcdf-bin
RUN sudo apt-get -y install libnetcdf-dev
RUN sudo apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN sudo pip install h5py
RUN HDF5_DIR=/usr/local/hdf5
RUN sudo pip install netcdf4
RUN sudo pip install plotly
ADD TminPlot.py TminPlot.py
ADD TmaxPlot.py TmaxPlot.py
VOLUME /data