from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class RoomCreate(BaseModel):
    type: str
    size: float
    property_id: UUID


class RoomResponse(BaseModel):
    id: UUID
    type: str
    size: float
    property_id: UUID


class RoomUpdate(BaseModel):
    type: Optional[str]
    size: Optional[float]


class RoomDelete(BaseModel):
    id: UUID