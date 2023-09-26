# Python image to use.
FROM python:latest

# Set the working directory to /app
WORKDIR /home/peter_duronelly/forecast_app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
ENTRYPOINT ["python", "forecast.py"]