#!/usr/bin/env python
# coding: utf-8

# # Model to test deploying to fastapi

# In[7]:


# Imports
import datetime as dt
from pathlib import Path

import joblib
import pandas as pd
import yfinance as yf
from fbprophet import Prophet


# In[8]:

# Setting base directory and the current date
# DIR = Path(__file__).resolve(strict = True).parent

DIR = Path(__file__).resolve(strict=True).parent

TODAY = dt.date.today()


# In[9]:


# Training function for tickers


def train(ticker):

    # Need conditional try/except here for impossible ticker????
    # Also look at dynamic date range up to a few yrs?? Need to time runs with large datasets
    # , and also yfinance API limits. 
    
    data = yf.download(ticker, "2020-01-01", TODAY.strftime("%Y-%m-%d"))
    data.head()
    data["Adj Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

    df_forecast = data.copy()
    df_forecast.reset_index(inplace=True)
    df_forecast["ds"] = df_forecast["Date"]
    df_forecast["y"] = df_forecast["Adj Close"]
    df_forecast = df_forecast[["ds", "y"]]

    # Check Prophet docs to see how calculated and seasonality args
    model = Prophet()
    model.fit(df_forecast)

    joblib.dump(model, Path(DIR).joinpath(f"{ticker}.joblib"))


# In[14]:


# Prediction function

def predict(ticker, days = 7):
    
    ticker_file = Path(DIR).joinpath(f'{ticker}.joblib')
    
    if not ticker_file.exists():
        return False
    
    model = joblib.load(ticker_file)
    
    future = TODAY + dt.timedelta(days = days)
    
    
    # Look at adjusting for training with dynamic range in train and predict functions.
    dates = pd.date_range(start = '2020-01-01', end = future.strftime('%m/%d/%Y'))
    
    df = pd.DataFrame({'ds': dates})
    
    forecast = model.predict(df)
    
    model.plot(forecast).savefig(f'{ticker}_plot.png')
    model.plot_components(forecast).savefig(f'{ticker}_plot_components.png')
    
    return forecast.tail(days).to_dict('records')   
    


# In[ ]:


def convert(prediction_list):
    
    output = {}
    
    for data in prediction_list:
        date = data['ds'].strftime('%m/%d/%Y')
        output[date] = data['trend']
    
    return output


