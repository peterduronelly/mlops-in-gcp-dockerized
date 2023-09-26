## IMPORTS
from google.cloud import bigquery
import pandas as pd
import pmdarima as pm
import logging
from pmdarima.model_selection import train_test_split

## GET DATA

bq = bigquery.Client()

q = """
SELECT * FROM st-data-project.fx_data.eurusd_hourly
"""

df_fx = bq.query(q).to_dataframe()
df_fx.sort_values(by = 'ts', inplace = True)

## BUILD MODEL

train, test = train_test_split(df_fx.close, train_size=df_fx.shape[0]//4*3)
model = pm.auto_arima(train)

forecasts = model.predict(12)

new_ts = [df_fx.ts.iloc[-1] + pd.Timedelta(hours = x) for x in range(1,13)]

## PRESENT RESULTS

logging.info('Forecasts are ready.')
print(pd.DataFrame({'ts': new_ts, 'close': forecasts}))