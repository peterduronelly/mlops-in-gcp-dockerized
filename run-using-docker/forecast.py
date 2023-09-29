## IMPORTS
from google.cloud import bigquery
import pandas as pd
import pmdarima as pm
import logging
from pmdarima.model_selection import train_test_split
from google.oauth2 import service_account
import warnings
warnings.filterwarnings('ignore')

logging.basicConfig(
    format="%(asctime)s - %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)

## GET CREDENTIALS
# If you run your solution from the Cloud shell, you need to get credentials to authenticate. 
# In many other cases, for instance when you run your app from Cloud Run, you are authenticated automatically from your project.

# If you do need credentials, then go to APIs & Services > Credentials > click your service account email > KEYS > ADD KEYS > select json
# Define your 'credentials' variable. 
"""credentials = service_account.Credentials.from_service_account_file(
    'cred.json', scopes=["https://www.googleapis.com/auth/cloud-platform"],
)"""

## GET DATA

logging.info("Starting...")

# If you need to provide credentials info: use the following syntax.
# bq = bigquery.Client(credentials=credentials, project=credentials.project_id,)

# For Cloud Run BQ Client will authenticate automatically.

bq = bigquery.Client()

q = """
SELECT * FROM st-data-project.fx_data.eurusd_hourly
"""

result = bq.query(q)
df_fx = result.to_dataframe()
df_fx.sort_values(by = 'ts', inplace = True)

logging.info('Data collected: %d rows.', df_fx.shape[0])

## BUILD MODEL

logging.info('Building model.')

train, test = train_test_split(df_fx.close, train_size=df_fx.shape[0]//4*3)
model = pm.auto_arima(train)

logging.info('Model ready, predicting.')

forecasts = model.predict(12)

new_ts = [df_fx.ts.iloc[-1] + pd.Timedelta(hours = x) for x in range(1,13)]

## PRESENT RESULTS

logging.info('Forecasts are ready.')
print(pd.DataFrame({'ts': new_ts, 'close': forecasts}))