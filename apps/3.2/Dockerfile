FROM python:3.4.5-slim

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

## make a local directory
RUN mkdir /counter_app

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /counter_app

# copy the local requirements.txt to the /code directory
ADD requirements.txt .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# now copy all the files in this directory to /code
ADD . .

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD ["python", "manage.py", "runserver"]
