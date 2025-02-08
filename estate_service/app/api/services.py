from loguru import logger
from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from estate_service.app.api.schemas import PropertyCreate
from estate_service.app.database.models import Property


def upload_property_to_db(property_data: PropertyCreate, session: Session):
    """
    Create a new property record in the database.
    """
    try:
        property_submission = Property(
            name=property_data.name,
            address=property_data.address,
            price=property_data.price,
            square=property_data.square
        )

        session.add(property_submission)
        session.commit()
        session.refresh(property_submission)
        return property_submission

    except Exception as e:
        session.rollback()
        logger.error(f"An error occurred while creating Property: {e}")
        raise HTTPException(status_code=400, detail=f"Error creating property: {e}")


def get_property_by_id_db(property_id: UUID, session: Session):
    try:
        property_instance = session.query(Property).filter(Property.id == property_id).first()

        if not property_instance:
            raise HTTPException(status_code=404, detail="Property not found")

        return property_instance
    except Exception as e:
        session.rollback()
        logger.error(f"An error occurred while getting Property by id: {e}")
        raise HTTPException(status_code=400, detail=f"Error getting property by id: {e}")


def get_all_properties_from_db(session: Session):
    """
    Retrieve all property records from the database.
    """
    try:
        properties = session.query(Property).all()
        return properties
    except Exception as e:
        logger.error(f"Error retrieving properties: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving properties")