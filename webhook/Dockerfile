FROM python:3.11-slim

# Install Docker CLI and other dependencies
RUN apt-get update && apt-get install -y docker.io python3-pip && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the webhook script
COPY . .

# Run the webhook
CMD ["python", "webhook.py"]

