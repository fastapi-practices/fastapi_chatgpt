#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.common.open_interpreter import open_interpreter
from app.common.response import ResponseModel
from app.schemas.interpreter import InterpreterMessage

router = APIRouter()


@router.post('/chat', summary='ChatGPT')
def interpreter_chat(message: InterpreterMessage) -> ResponseModel:
    result = open_interpreter.chat(message)
    return ResponseModel(data=result)


@router.post('/chat-stream', summary='ChatGPT 流式响应')
def interpreter_chat_stream(message: InterpreterMessage) -> StreamingResponse:
    def event_stream():
        for result in open_interpreter.chat(message, stream=True):
            yield f'{result}\n\n'

    return StreamingResponse(event_stream(), media_type='text/event-stream')


@router.get('/history', summary='历史消息')
def interpreter_history() -> ResponseModel:
    return ResponseModel(data=open_interpreter.messages)


@router.post('/reset', summary='重置上下文')
def interpreter_reset() -> ResponseModel:
    open_interpreter.reset()
    return ResponseModel()
