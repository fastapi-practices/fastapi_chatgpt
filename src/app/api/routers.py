#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.api.v1.chatgpt import router as chatgpt_router
from app.core.conf import settings

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(chatgpt_router, prefix='/chatgpt', tags=['chatgpt'])
