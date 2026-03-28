# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install uv (dependency manager) and project dependencies
RUN pip install uv && uv sync

# Expose port
EXPOSE 8000

# Run the server with uvicorn
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]