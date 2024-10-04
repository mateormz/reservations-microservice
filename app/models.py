from bson import ObjectId
from .database import reservations_collection, timeslots_collection
from .schemas import ReservationCreate, TimeSlotCreate

# TimeSlots CRUD

def create_timeslot(timeslot: TimeSlotCreate):
    timeslot_data = timeslot.dict()
    result = timeslots_collection.insert_one(timeslot_data)
    return str(result.inserted_id)

def get_timeslot(id: str):
    return timeslots_collection.find_one({"_id": ObjectId(id)})

def get_timeslots_by_field(field: str):
    timeslots = timeslots_collection.find({"field": field, "status": "available"})
    
    result = []
    for timeslot in timeslots:
        timeslot["_id"] = str(timeslot["_id"])  # Convertir ObjectId a string
        result.append(timeslot)
    
    return result

# Reservations CRUD

def create_reservation(reservation: ReservationCreate):
    reservation_data = reservation.dict()
    result = reservations_collection.insert_one(reservation_data)
    timeslots_collection.update_one(
        {"_id": ObjectId(reservation.timeslot_id)}, {"$set": {"status": "reserved"}}
    )
    return str(result.inserted_id)

def get_reservation(id: str):
    reservation = reservations_collection.find_one({"_id": ObjectId(id)})
    if reservation:
        reservation["_id"] = str(reservation["_id"])  # Convertir ObjectId a string
    return reservation

def get_reservations_by_field(field: str):
    return list(reservations_collection.find({"field": field}))
