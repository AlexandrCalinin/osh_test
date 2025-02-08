import math
from typing import Union

from loguru import logger
from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from estate_service.app.api.schemas.property_schemas import PropertyCreate, PropertyUpdate
from estate_service.app.api.schemas.room_schemas import RoomCreate, RoomUpdate
from estate_service.app.database.models import Property, Room


def upload_instance_to_db(data: Union[PropertyCreate, RoomCreate], session: Session, table: str):
    try:
        if table == "property":
            instance = Property(
                name=data.name,
                address=data.address,
                price=data.price,
                square=data.square
            )
        elif table == "room":
            instance = Room(
                type=data.type,
                size=data.size,
                property_id=data.property_id
            )
        else:
            raise Exception

        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance

    except Exception as e:
        session.rollback()
        logger.error(f"An error occurred while creating Instance: {e}")
        raise HTTPException(status_code=400, detail=f"Error creating Instance: {e}")


def get_instance_by_id_db(instance_id: UUID, session: Session, table: Union[Property, Room]):
    try:
        instance = session.query(table).filter(table.id == instance_id).first()

        if not instance:
            raise HTTPException(status_code=404, detail="Instance not found")

        return instance
    except Exception as e:
        session.rollback()
        logger.error(f"An error occurred while getting Instance by id: {e}")
        raise HTTPException(status_code=400, detail=f"Error getting Instance by id: {e}")


def update_instance_db(instance_id: UUID, instance_data: Union[PropertyUpdate, RoomUpdate],
                       session: Session, table: Union[Property, Room]):
    try:
        instance = session.query(table).filter(table.id == instance_id).first()

        if not instance:
            raise HTTPException(status_code=404, detail="Not found")

        update_data = instance_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(instance, field, value)

        session.commit()
        session.refresh(instance)

        return instance

    except Exception as e:
        session.rollback()
        logger.error(f"Error updating Instance: {e}")
        raise HTTPException(status_code=500, detail=f"Error updating Instance: {e}")


def delete_instance_db(instance_id: UUID, session: Session, table: Union[Property, Room]):
    try:
        instance = session.query(table).filter(table.id == instance_id).first()

        if not instance:
            raise HTTPException(status_code=404, detail="Instance not found")

        session.delete(instance)
        session.commit()

        return {"id": instance_id}

    except Exception as e:
        session.rollback()
        logger.error(f"Error deleting Instance: {e}")
        raise HTTPException(status_code=500, detail=f"Error deleting Instance: {e}")


def get_properties_paginated(session: Session, page: int, per_page: int):
    try:
        offset = (page - 1) * per_page
        total = session.query(Property).count()
        properties = session.query(Property).offset(offset).limit(per_page)

        if not properties:
            raise HTTPException(status_code=404, detail="Property not found")

        return {"total_items": total, "total_pages": math.ceil(total / per_page),
                "current_page": page, "page_size": per_page, "data": properties}
    except Exception as e:
        logger.error(f"Error retrieving properties: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving properties")