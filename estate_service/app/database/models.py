from sqlalchemy import Column, text, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Property(Base):
    __tablename__ = "properties"

    id = Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    name = Column("name", String(100), nullable=False)
    address = Column("address", String(64), nullable=False)
    price = Column("price", Float, nullable=False)
    square = Column("square", Integer(), nullable=False)

    rooms = relationship("Room", back_populates="property", cascade="all, delete")


class Room(Base):
    __tablename__ = "rooms"

    id = Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"))
    type = Column("type", String(32), nullable=False)
    size = Column("size", Float, nullable=False)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id", ondelete="CASCADE"))

    property = relationship("Property", back_populates="rooms")
