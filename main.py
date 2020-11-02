from fastapi import FastAPI
from model import predict, convert
from starlette.responses import JSONResponse


app = FastAPI()

        
# Routes

@app.get("/")
def pong():
    return {"ping":"pong!"}


	
@app.get('/predict/{ticker}')
def get_prediction(ticker):

	prediction_list = predict(ticker)
	
	prediction_convert = convert(prediction_list)
	
	return JSONResponse(prediction_convert)
	
	
