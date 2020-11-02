from fastapi import FastAPI
#from pydantic import BaseModel
#from api_model import convert, predict

app = FastAPI()

        
# Routes

@app.get("/")
def pong():
    return {"ping":"pong!"}



#@app.post('/predict', response_model = StockOut, status_code = 200)
#def get_prediction(payload: StockIn):
    
#    ticker = payload.ticker
    
#    prediction_list = predict(ticker)
    
#    if not prediction_list:
#        raise HTTPException(status_code = 400, detail = "Model Not Found")
        
#    response_object = {"ticker": ticker,"forecast": convert(prediction_list)}
    
#    return response_object
	
	
