from fastapi import APIRouter, HTTPException
from .models import get_all_reservations_from_db , create_timeslot, get_timeslot, create_reservation, get_reservation, get_timeslots_by_field
from .schemas import TimeSlotCreate, ReservationCreate

router = APIRouter()

# TimeSlots Endpoints
@router.post("/timeslots/", response_model=str)
async def create_time_slot(timeslot: TimeSlotCreate):
    return create_timeslot(timeslot)

@router.get("/timeslots/{field}", response_model=list)
async def get_field_timeslots(field: str):
    timeslots = get_timeslots_by_field(field)
    if not timeslots:
        raise HTTPException(status_code=404, detail="No available timeslots")
    return timeslots

# Reservations Endpoints
@router.post("/reservations/", response_model=str)
async def create_reservation_endpoint(reservation: ReservationCreate):
    return create_reservation(reservation)

@router.get("/reservations/{id}", response_model=dict)
async def get_reservation_endpoint(id: str):
    reservation = get_reservation(id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.get("/reservations/", response_model=list)
async def get_all_reservations():
    reservations = get_all_reservations_from_db()  
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found")
    return reservations