# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Install system dependencies and setup environment
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy the current directory contents into the container at /app
COPY . /app/

# Step 5: Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Set environment variable to ensure Python output is logged to the terminal
ENV PYTHONUNBUFFERED 1

# Step 7: Expose port 8000 for the Django application
EXPOSE 8000

# Step 8: Run database migrations
RUN python manage.py migrate

# Step 9: Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# Step 10: Create the superuser (optional, but can be configured for admin use)
# Uncomment the next line if you want to automatically create a superuser on build
# RUN python manage.py createsuperuser --noinput --username admin --email admin@example.com

# Step 11: Start the Django development server on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]