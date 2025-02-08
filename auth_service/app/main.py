import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

from auth_service.app.api.routers import router


app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(router)

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


if __name__ == "__main__":
    uvicorn.run("auth_service.app.main:app", host="127.0.0.1", port=8001, reload=True)