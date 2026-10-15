from fastapi import FastAPI

app = FastAPI(
    title="DeadlineOS API",
    description="Academic Task & Deadline Intelligence",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DeadlineOS",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}