from fastapi import FastAPI
from model import predict, convert


app = FastAPI()

        
# Routes

@app.get("/")
def pong():
    return {"ping":"pong!"}


	
