from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Open EDA Library Generator",
        "version": "0.1"
    }
