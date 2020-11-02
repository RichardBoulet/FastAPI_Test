from fastapi import FastAPI
from model import predict, convert


app = FastAPI()

        
# Routes

@app.get("/")
def pong():
    return {"ping":"pong!"}


	
@app.get('/predict')
def get_prediction():
	
	prediction_list = predict()
	
	prediction_convert = convert(prediction_list)
	
	return 'test'
	
	
