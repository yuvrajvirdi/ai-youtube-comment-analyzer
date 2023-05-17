# base image
FROM python:3.8.5

# setting work dir
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt .

# install dependencies
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# copy application code into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Start the Flask application
CMD . venv/bin/activate && python main.py