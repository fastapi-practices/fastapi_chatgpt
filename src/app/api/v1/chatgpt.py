#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse

from app.common.interpreter import interpreter
from app.common.response import ResponseModel

router = APIRouter()


@router.get('/chat', summary='ChatGPT')
async def chatgpt(message: Annotated[str, Query()]):
    # TODO: Check openai_auth before chat
    def event_stream():
        for result in interpreter.chat(message, display=False, stream=True):
            yield f'data: {result}\n\n'

    return StreamingResponse(event_stream(), media_type='text/event-stream')


@router.get('/chat/once', summary='ChatGPT once')
async def chatgpt_once(message: Annotated[str, Query()]):
    answer = interpreter.chat(message, display=False)
    return ResponseModel(data=answer)


@router.get('/history', summary='ChatGPT History')
async def history() -> ResponseModel:
    return ResponseModel(data=interpreter.messages)


@router.get('/reset', summary='Reset ChatGPT')
async def reset() -> ResponseModel:
    interpreter.reset()
    return ResponseModel(msg='Reset ChatGPT successfully.')
