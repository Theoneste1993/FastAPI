from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello all": "World"}
import pandas as pd
