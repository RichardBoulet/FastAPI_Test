from fastapi import FastAPI
from model import predict, convert


app = FastAPI()

        
# Routes

@app.get("/")
def pong():
    return {"ping":"pong!"}


	
@app.get('/predict/{ticker}')
def get_prediction(ticker):
	
	prediction_list = predict(ticker)
	
	prediction_convert = convert(prediction_list)
	
	return {'ticker': ticker, 'forecast': prediction_convert}
	
	
