# Python image to use.
FROM python:3.10

# Set the working directory to /
WORKDIR /

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /forecast_app
COPY . .

# Run forecast.py when the container launches
ENTRYPOINT ["python", "forecast.py"]