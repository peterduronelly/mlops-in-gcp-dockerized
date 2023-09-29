# Run your code by using simply using Docker

It is possible to build your image locally and run your code using docker commands from Cloud Shell. There are two problems with this approach:
1. Auto-authentication will not work.
2. You image will be lost when you stop the shell instance.  <br>

Fortunately both issues can be solves easily. Let's see, however, how it exactly works. 

### Authentication using a json file for credentials

You need to create a key file by going to **APIs & Services** > **Credentials** > click your service account email > **KEYS** > **ADD KEYS** > select **json**. You will be prompted to download the json file onto your local machine. Once you have the file upload it to the directory of your script. If you are syncing with a version control system don't forget to add the file to `.gitignore`. 

Before initalizing your BigQuery Client, create a `google.auth.credentials.Credentials` object and add to your Client:
```Python
credentials = service_account.Credentials.from_service_account_file(
    'cred.json', scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
bq = bigquery.Client(credentials=credentials, project=credentials.project_id,)
```

### Store your container image in Artifact Registry

`Artifact Registry` is the repository for various artifacts *and* containers (replacing Container Registry). The best way to place your container is to build it using `Cloud Build`. 

`gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/quickstart-image .`

Make sure you include the last dot at the end of the command! 


### Build and run your container locally

If, however, you are kust setting up a transitory container, you can so by running
`docker image build -t forecast:0.1 .`

'*forecast:01*' is the name of the container image, and watch for the dot at the end of the command again. 

To run your container type
`docker run forecast:0.1`. 

Existing images can be listed using
`docker images`