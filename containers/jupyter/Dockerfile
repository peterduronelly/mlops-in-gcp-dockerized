FROM --platform=linux/amd64 ubuntu:22.04

RUN apt-get -y update
RUN apt-get install -y --no-install-recommends \
python3-pip \
pipx \
git \
make \
jq

RUN pip install \
jupyterlab==3.3.0 \
prophet==1.1.4 \
numpy \
pandas \
pyarrow \
fastapi \
pystan \
joblib

# Create a link that points to the right python bin directory
RUN ln -s /usr/bin/python3.9 /usr/bin/python
