from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PawPlan API is live!"}
