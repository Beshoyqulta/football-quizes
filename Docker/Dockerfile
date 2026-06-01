# 1. Use an official, lightweight Python runtime as a parent image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container first
# (This allows Docker to cache installed packages if requirements don't change)
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code into the container
COPY . .

# 6. Expose the port FastAPI will run on
EXPOSE 8000

# 7. Command to run the Uvicorn ASGI server when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]