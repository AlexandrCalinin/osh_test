import os
import sys

from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL_ESTATE")

if not DATABASE_URL:
    logger.critical("DATABASE_URL wasn't found in .env file")
    sys.exit(1)

try:
    engine = create_engine(DATABASE_URL, execution_options={"isolation_level": "READ COMMITTED"})
    session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
    Base = declarative_base()
    logger.info("Database connection successfully established")
except Exception as e:
    logger.critical(f"Failed to connect to database: {e}")
    sys.exit(1)

def get_db():
    db = session_local()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
    finally:
        db.close()
