from loguru import logger
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from uuid import UUID

from estate_service.app.database.database import get_db
from estate_service.app.api.schemas.property_schemas import PropertyCreate, PropertyResponse, PropertyUpdate, \
    PaginatedResponse, PropertyDelete
from estate_service.app.api.services import (
    upload_instance_to_db, get_instance_by_id_db,
    update_instance_db, delete_instance_db, get_properties_paginated
)
from estate_service.app.database.models import Property


router = APIRouter(prefix="/estate")


@router.post("/property", response_model=PropertyResponse, status_code=201)
async def create_property(property_data: PropertyCreate, session: Session = Depends(get_db)) -> PropertyCreate:
    """Create new property"""
    try:
        uploaded_property = upload_instance_to_db(data=property_data, session=session, table="property")

        if uploaded_property:
            return uploaded_property
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The property wasn't created due to an error: {e}")
        return {"error": f"The property wasn't created due to an error: {e}"}


@router.get("/property/{property_id}", response_model=PropertyResponse, status_code=200)
async def get_property_by_id(property_id: UUID, session: Session = Depends(get_db)) -> PropertyResponse:
    """Get only one property by id"""
    try:
        response = get_instance_by_id_db(instance_id=property_id, session=session, table=Property)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The property wasn't got due to an error: {e}")
        return {"error": f"The property wasn't got due to an error: {e}"}


@router.put("/property/{property_id}", response_model=PropertyUpdate, status_code=200)
async def update_property(property_id: UUID, property_data: PropertyUpdate,
                          session: Session = Depends(get_db)) -> PropertyUpdate:
    """Update property by id"""
    try:
        response = update_instance_db(instance_id=property_id, instance_data=property_data,
                                      session=session, table=Property)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The property wasn't updated due to an error: {e}")
        return {"error": f"The property wasn't updated due to an error: {e}"}


@router.delete("/property/{property_id}", response_model=PropertyDelete)
async def delete_property(property_id: UUID, session: Session = Depends(get_db)):
    """Delete property by id"""
    try:
        response = delete_instance_db(instance_id=property_id, session=session, table=Property)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The property wasn't deleted due to an error: {e}")
        return {"error": f"The property wasn't deleted due to an error: {e}"}


@router.get("/", status_code=200, response_model=PaginatedResponse)
async def get_properties_paginated(session: Session = Depends(get_db), page: int = 1,
                                   per_page: int  = 10) -> PaginatedResponse:
    """Get all properties paginated from database"""
    try:
        response = get_properties_paginated(session=session, page=page, per_page=per_page)

        if response["data"]:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The paginated properties weren't got due to an error: {e}")
        return {"error": f"The paginated properties weren't got due to an error: {e}"}