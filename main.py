from fastapi import FastAPI

app = FastAPI()
        
# Routes

@app.get("/")
def pong():
    return {"ping":"pong!"}


	
