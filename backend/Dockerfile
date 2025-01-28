# backend/Dockerfile
FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Remove collectstatic from Dockerfile
# This should be done after environment is fully configured

# # Add these lines
# RUN python manage.py collectstatic --noinput
