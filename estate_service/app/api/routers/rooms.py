from loguru import logger
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from uuid import UUID

from estate_service.app.database.database import get_db
from estate_service.app.api.services import (
    upload_instance_to_db, get_instance_by_id_db,
    update_instance_db, delete_instance_db
)
from estate_service.app.api.schemas.room_schemas import RoomDelete, RoomUpdate, RoomResponse, RoomCreate
from estate_service.app.database.models import Room


router = APIRouter(prefix="/estate")


@router.post("/room", response_model=RoomResponse, status_code=201)
async def create_room(room_data: RoomCreate, session: Session = Depends(get_db)):
    """Create new room"""
    try:
        uploaded_instance = upload_instance_to_db(data=room_data, session=session, table="room")

        if uploaded_instance:
            return uploaded_instance
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The room wasn't created due to an error: {e}")
        return {"error": f"The room wasn't created due to an error: {e}"}


@router.get("/room/{room_id}", response_model=RoomResponse, status_code=200)
async def get_room_by_id(room_id: UUID, session: Session = Depends(get_db)):
    """Get only one room by id"""
    try:
        response = get_instance_by_id_db(instance_id=room_id, session=session, table=Room)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The room wasn't got due to an error: {e}")
        return {"error": f"The room wasn't got due to an error: {e}"}


@router.put("/room/{room_id}", response_model=RoomUpdate, status_code=200)
async def update_room(room_id: UUID, room_data: RoomUpdate, session: Session = Depends(get_db)):
    """Update room by id"""
    try:
        response = update_instance_db(instance_id=room_id, instance_data=room_data,
                                      session=session, table=Room)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The room wasn't got due to an error: {e}")
        return {"error": f"The room wasn't got due to an error: {e}"}


@router.delete("/room/{room_id}", response_model=RoomDelete, status_code=200)
async def delete_room(room_id: UUID, session: Session = Depends(get_db)):
    """Delete room by id"""
    try:
        response = delete_instance_db(instance_id=room_id, session=session, table=Room)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The room wasn't got due to an error: {e}")
        return {"error": f"The room wasn't got due to an error: {e}"}
