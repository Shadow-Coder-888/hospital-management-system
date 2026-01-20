from fastapi import FastAPI

app = FastAPI(title="Hospital Management System")

@app.get("/")
def health_check():
    return {"status": "ok"}
