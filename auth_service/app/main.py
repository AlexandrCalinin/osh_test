import uvicorn
import sys

from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
    allow_credentials=True
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="API docs"
    )

logger.remove()
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
logger.add("auth_service.log", format="{time} {level} {message}", level="DEBUG")


if __name__ == "__main__":
    try:
        logger.info("Auth service is starting...")
        uvicorn.run("auth_service.app.main:app", host="127.0.0.1", port=8001, reload=True)
    except OSError as os_error:
        logger.critical(f"Server startup failed: {os_error.strerror} (Code: {os_error.errno})", exc_info=True)
    except SQLAlchemyError as db_error:
        logger.critical(f"Database connection failed: {str(db_error)}", exc_info=True)
    except Exception as unknown_error:
        logger.critical(f"Unexpected error: {str(unknown_error)}", exc_info=True)
