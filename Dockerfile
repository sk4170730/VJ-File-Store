# Don't Remove Credit @
# Subscribe YouTube @ | Doubt @

FROM python:3.10-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update & install only required packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git \
        ffmpeg \
        libsm6 \
        libxext6 && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user (security best practice)
RUN useradd -m -s /bin/bash appuser

# Set work directory
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy bot files
COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Start bot
CMD ["python", "bot.py"]
