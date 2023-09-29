# mlops-in-gcp-dockerized
Dockerized ML solution on GCP

This repository is a work in progress, starting with a basic forecast exercise. The modelling per se is not important, this repo is focused on the workflow, not on a reliable forecasting tool. 
˛

### Workflow to build image with Cloud Build

- Create your script
- Add Dockerfile & credentials
- Authenticate by running `gcloud auth login`
- Run `gcloud builds submit --tag gcr.io/$DEVSHELL_PROJECT_ID/forecast:0.1`
