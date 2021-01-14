FROM python:3.8.5-buster
LABEL author="Richard Crouch"
LABEL description="Light measurement microservice"

# Generate logs in unbuffered mode
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update
RUN apt-get -y install libusb-1.0.0 libusb-1.0.0-dev

# Install Python dependencies
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

EXPOSE 9503

# run Python unbuffered so the logs are flushed
#CMD ["python3", "-u", "light_service.py"]
CMD ["tail", "-f", "/dev/null"]
