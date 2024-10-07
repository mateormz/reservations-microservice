from fastapi import FastAPI
from .routes import router as reservation_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir cualquier origen
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir todos los orígenes
    allow_credentials=True,  # Si las solicitudes incluyen credenciales (cookies, tokens, etc.)
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todas las cabeceras
)

app.include_router(reservation_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Reservations microservice!"}
