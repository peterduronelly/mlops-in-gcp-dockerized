# Run Jupyter Notebook From Custom Containers
When creating a new notebook workbench you can select your own custom container as an environment. There are two ways to build a custom container
1. **Derivative container**: modify an Google-provided existing conainer image: https://cloud.google.com/deep-learning-containers/docs/derivative-container
2. **Custom container**: build your own container from scratch: https://cloud.google.com/vertex-ai/docs/workbench/managed/custom-container

Note: the second option does not work as implied by the documentation, so the exact workflow is still undefined. The first one, though,  works just perfect. 

Once you created the Dockerfiles, run the following commands:   

`docker build . -f Dockerfile -t "gcr.io/${GOOGLE_CLOUD_PROJECT}/derivative-container:latest"`

The way to create this managed notebook instance from the console is straightforward from the documentation. (I think most of the time we create these kinds of objects from the console anyway.) It is possible though to do it from the CLI:   

`gcloud notebooks instances create derivative-container-instance --container-repository=gcr.io/${GOOGLE_CLOUD_PROJECT}/derivative-container --container-tag=latest --machine-type=e2-standard-2 --location=us-central1-a`

