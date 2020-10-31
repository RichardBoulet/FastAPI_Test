from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from api_model import convert, predict

app = FastAPI()


class StockIn(BaseModel):
    ticker: str
        
class StockOut(StockIn):
    forecast: dict
        
# Routes

@app.get('/ping')
async def pong():
    
    return{'ping':'pong!'}



@app.post('/predict', response_model = StockOut, status_code = 200)
def get_prediction(payload: StockIn):
    
    ticker = payload.ticker
    
    prediction_list = predict(ticker)
    
    if not prediction_list:
        raise HTTPException(status_code = 400, detail = "Model Not Found")
        
    response_object = {"ticker": ticker,"forecast": convert(prediction_list)}
    
    return response_object



@app.get('/results')
async def prediction_results():
    
    ticker = 'MSFT'
    
    prediction_list = predict(ticker)
    
    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    
    return response_object