from fastapi import FastAPI
from quotes import get_quotes as quotes


app = FastAPI()
@app.get("/quotes")
def get_quotes():
    return {"quotes": quotes()}
@app.get("/")
def slsash():
    return {"message": "Welcome to the Quotes API. Use /quotes to get quotes."}
    