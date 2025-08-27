# Dockerfile for python app with SkyWalking Python agent
# Uses official SkyWalking Python base image with gRPC protocol and Python 3.10
FROM apache/skywalking-python:1.2.0-grpc-py3.10-slim

# Set working directory
WORKDIR /app

# Install application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# The base image defines ENTRYPOINT ["sw-python"]
# Use CMD to start the application under the SkyWalking agent
CMD ["python", "main.py"]
