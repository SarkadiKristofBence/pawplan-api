from fastapi import FastAPI
from routes import planner

app = FastAPI(title="PawPlan API")

app.include_router(Planner.router)


app = FastAPI()

@app.get("/")
def root():
    return {"message": "PawPlan API is live!"}
