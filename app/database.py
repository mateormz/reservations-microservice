import os
from pymongo import MongoClient

# Configuración de la conexión a MongoDB
mongo_uri = "mongodb://44.209.40.209:27017/reservas_db"
client = MongoClient(mongo_uri)

# Acceso a la base de datos y las colecciones
db = client["reservas_db"]
reservations_collection = db["reservations"]
timeslots_collection = db["timeslots"]