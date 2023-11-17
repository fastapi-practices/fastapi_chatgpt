#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uvicorn

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from app.api.routers import v1
from app.common.log import log
from app.common.response import ResponseModel
from app.core.conf import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOCS_URL,
    openapi_url=settings.OPENAPI_URL,
)


app.include_router(v1)


@app.exception_handler(Exception)
async def openai_auth_exception_handler(request: Request, exc: Exception):
    import traceback

    log.error(f'❌: {traceback.format_exc()}')
    return JSONResponse(
        status_code=500,
        content=ResponseModel(code=500, msg=str(exc)).model_dump(),
    )


if __name__ == '__main__':
    try:
        log.info(
            """\n
 /$$$$$$$$                   /$$      /$$$$$$  /$$$$$$$  /$$$$$$
| $$_____/                  | $$     /$$__  $$| $$__  $$|_  $$_/
| $$    /$$$$$$   /$$$$$$$ /$$$$$$  | $$  | $$| $$  | $$  | $$  
| $$$$$|____  $$ /$$_____/|_  $$_/  | $$$$$$$$| $$$$$$$/  | $$  
| $$__/ /$$$$$$$|  $$$$$$   | $$    | $$__  $$| $$____/   | $$  
| $$   /$$__  $$ |____  $$  | $$ /$$| $$  | $$| $$        | $$  
| $$  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$  | $$| $$       /$$$$$$
|__/   |_______/|_______/    |___/  |__/  |__/|__/      |______/

            """
        )
        uvicorn.run(
            app='main:app',
            host=settings.UVICORN_HOST,
            port=settings.UVICORN_PORT,
            reload=settings.UVICORN_RELOAD,
        )
    except Exception as e:
        log.error(f'❌ FastAPI start filed: {e}')
