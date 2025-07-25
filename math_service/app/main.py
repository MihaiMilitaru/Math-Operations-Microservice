
from fastapi import FastAPI
from app.controllers import router as math_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Math Operations Microservice")

app.include_router(math_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
