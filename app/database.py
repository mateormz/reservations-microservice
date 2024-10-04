import os
from pymongo import MongoClient

# Configuración de la conexión a MongoDB
MONGO_DETAILS = os.getenv("//localhost:27017")
client = MongoClient(MONGO_DETAILS)

# Acceso a la base de datos y las colecciones
db = client["reservas_db"]
reservations_collection = db["reservations"]
timeslots_collection = db["timeslots"]