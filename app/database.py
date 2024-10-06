import os
from pymongo import MongoClient

# Configuración de la conexión a MongoDB
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)

# Acceso a la base de datos y las colecciones
db = client["reservas_db"]
reservations_collection = db["reservations"]
timeslots_collection = db["timeslots"]
