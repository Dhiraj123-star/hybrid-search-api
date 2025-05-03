# 🐍 Use official Python 3.12 slim image
FROM python:3.12-slim

# 🏷️ Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 🗂️ Set working directory
WORKDIR /app

# 📦 Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 🧪 Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copy application source code
COPY . .

# 🚀 Expose port
EXPOSE 8000

# 🏃 Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
