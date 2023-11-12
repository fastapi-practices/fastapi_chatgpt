#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse

from app.common.interpreter import interpreter

router = APIRouter()


@router.get('/chat', summary='ChatGPT')
async def chatgpt(message: Annotated[str, Query()]):
    def event_stream():
        for result in interpreter.chat(message, stream=True):
            yield f'data: {result}\n\n'

    return StreamingResponse(event_stream(), media_type='text/event-stream')
