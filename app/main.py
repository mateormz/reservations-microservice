from fastapi import FastAPI
from .routes import router as reservation_router

app = FastAPI()

app.include_router(reservation_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Reservations microservice!"}