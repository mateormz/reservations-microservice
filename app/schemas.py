from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TimeSlotBase(BaseModel):
    id: str
    date: datetime
    start_time: str
    end_time: str
    status: str
    field: str

class TimeSlotCreate(TimeSlotBase):
    pass

class TimeSlot(TimeSlotBase):
    id: str

    class Config:
        orm_mode = True


class ReservationBase(BaseModel):
    zonedatetime: datetime
    user: str
    field: str

class ReservationCreate(ReservationBase):
    timeslot_id: str

class Reservation(ReservationBase):
    id: str
    timeslot: TimeSlot

    class Config:
        orm_mode = True
