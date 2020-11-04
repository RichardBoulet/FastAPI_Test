from iris import Iris
from fastapi import FastAPI, Query
from typing import List
from pydantic import BaseModel
import json


app = FastAPI(debug = True)

iris = Iris()


@app.get('/')
def proper_root():

	return {'ERROR': 'Use GET /predict instead of root route!'}


@app.post('/predict/')
def predict(features = Query(None)):
	
	features = json.loads(features)
			
	prediction = iris.classify(features)
			
	return {'results': prediction}
	
