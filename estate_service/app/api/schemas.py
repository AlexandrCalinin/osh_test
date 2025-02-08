from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class RoomResponse(BaseModel):
    id: UUID
    type: str
    size: float
    property_id: UUID

    class Config:
        from_attributes = True


class PropertyCreate(BaseModel):
    name: str
    address: str
    price: float
    square: int


class PropertyUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    price: Optional[float] = None
    square: Optional[int] = None


class PropertyResponse(BaseModel):
    id: UUID
    name: str
    address: str
    price: float
    square: int
    rooms: Optional[List[RoomResponse]] = None

    class Config:
        from_attributes = True


class PaginatedResponse(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    page_size: int
    data: List[PropertyResponse]
