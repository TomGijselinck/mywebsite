############################################################
# Dockerfile to run my django website
# Based on Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu

MAINTAINER Tom Gijselinck

# append Ubuntu's universe repository to the default list of application sources 
# list of the base image
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main \
          universe" >> /etc/apt/sources.list

# Update the default application repository sources list
RUN apt-get update

# Install some usefull tools in this container.
RUN apt-get install -y tar \
                       git \
                       curl \
                       vim \
                       wget

# Install server and database software
RUN apt-get install -y gunicorn
RUN apt-get install -y sqlite
RUN apt-get update
RUN apt-get install -y nginx

# Install python etc.
RUN apt-get install -y python \
                       python-dev \
                       python-distribute \
                       python-pip

# Add all application source files (from the git repo).
ADD . /app

# install requirements
RUN pip install -r /app/requirements.txt

COPY nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default

# Port to expose
EXPOSE 8001

RUN python /app/manage.py collectstatic --noinput

# Directory to execute CMD commands
WORKDIR /app

# Run server when starting the container
CMD service nginx start && \
    gunicorn --bind 0.0.0.0:8000 mywebsite.wsgi:application --log-level=DEBUG
