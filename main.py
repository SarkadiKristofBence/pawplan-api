from fastapi import FastAPI
from routes import planner

app = FastAPI(title="PawPlan API")

app.include_router(planner.router)


app = FastAPI()

@app.get("/")
def root():
    return {"message": "PawPlan API is live!"}
