FROM python:3.7-alpine

# Set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
WORKDIR /usr/src/expertapp

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application's code
COPY . /usr/src/expertapp

ENTRYPOINT [ "python3" ]

# Run the app
CMD ["./expertsystem/evalengine.py"]