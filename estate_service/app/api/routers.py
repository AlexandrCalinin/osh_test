from loguru import logger
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from uuid import UUID

from estate_service.app.database.database import get_db
from estate_service.app.api.schemas import PropertyCreate, PropertyResponse
from estate_service.app.api.services import upload_property_to_db, get_property_by_id_db

router = APIRouter(prefix="/estate")


@router.post("/property", response_model=PropertyCreate, status_code=201)
async def create_property(property_data: PropertyCreate, session: Session = Depends(get_db)):
    """Create new property"""
    try:
        uploaded_property = upload_property_to_db(property_data=property_data, session=session)

        if uploaded_property:
            return uploaded_property
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The property wasn't created due to an error: {e}")
        return {"error": f"The property wasn't created due to an error: {e}"}


@router.get("/property/{property_id}", response_model=PropertyResponse, status_code=200)
async def get_property_by_id(property_id: UUID, session: Session = Depends(get_db)):
    """Get only one property by id"""
    try:
        response = get_property_by_id_db(property_id=property_id, session=session)

        if response:
            return response
        else:
            raise ValueError
    except ValueError as e:
        logger.error(f"The property wasn't got due to an error: {e}")
        return {"error": f"The property wasn't got due to an error: {e}"}

# @router.get("/", status_code=200, response_model=PaginatedResponse)
# async def get_properties(session: Session = Depends(get_db)) -> PaginatedResponse:
#     """Get all properties from database"""
#     pass