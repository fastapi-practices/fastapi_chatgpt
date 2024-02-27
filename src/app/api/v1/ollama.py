#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

import msgspec.json

from fastapi import APIRouter, Query
from ollama import AsyncClient
from starlette.responses import StreamingResponse

from app.common.response import ResponseModel
from app.core.conf import settings
from app.schemas.ollama import OllamaMessages

router = APIRouter()


@router.post('/chat', summary='ChatGPT')
async def ollama_chat(messages: OllamaMessages) -> ResponseModel:
    result = await AsyncClient().chat(
        model=settings.OLLAMA_MODEL, messages=[{'role': messages.role, 'content': messages.content}]
    )
    return ResponseModel(data=result)


@router.post('/chat-stream', summary='ChatGPT 流式响应')
async def ollama_chat_stream(messages: OllamaMessages):
    async def event_stream():
        async for result in await AsyncClient().chat(
            model=settings.OLLAMA_MODEL,
            messages=[{'role': messages.role, 'content': messages.content}],
            stream=True,
        ):
            text_line = msgspec.json.encode(result)
            yield f'{text_line}\n\n'

    return StreamingResponse(event_stream(), media_type='text/event-stream')


@router.get('/list', summary='本地离线模型列表')
async def ollama_list() -> ResponseModel:
    data = await AsyncClient().list()
    return ResponseModel(data=data)


@router.post('/pull', summary='拉取离线模型')
async def ollama_pull(model: Annotated[str, Query()]) -> ResponseModel:
    data = await AsyncClient().pull(model)
    return ResponseModel(data=data)


@router.delete('/delete', summary='删除本地离线模型')
async def ollama_delete(model: Annotated[str, Query()]) -> ResponseModel:
    data = await AsyncClient().delete(model)
    return ResponseModel(data=data)
