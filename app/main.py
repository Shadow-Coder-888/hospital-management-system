from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Hospital Management System")

Base.metadata.create_all(bind=engine)

@app.get("/")
def health():
    return {"status": "ok"}
