#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.api.v1.interpreter import router as interpreter_router
from app.api.v1.ollama import router as ollama_router
from app.core.conf import settings

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(interpreter_router, prefix='/interpreter', tags=['Interpreter'])
v1.include_router(ollama_router, prefix='/ollama', tags=['ollama'])
