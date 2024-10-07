from fastapi import FastAPI
from .routes import router as reservation_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(reservation_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Reservations microservice!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=[""],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=[""],  # Permitir todas las cabeceras
)