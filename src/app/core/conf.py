#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # FastAPI Settings
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'FastAPI'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'FastAPI ChatGPT API'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOCS_URL: str | None = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # ollama
    OLLAMA_MODEL: str = 'gemma:2b'

    # Interpreter
    INTERPRETER_AUTO_RUN: bool = False
    INTERPRETER_MAX_OUTPUT: int = 2200
    INTERPRETER_API_BASE: str = 'http://localhost:11434'  # ollama serve address
    INTERPRETER_TEMPERATURE: int | float = 0
    INTERPRETER_MAX_TOKENS: int | None = 100
    INTERPRETER_MAX_BUDGET: int | float | None = None
    INTERPRETER_CONTEXT_WINDOW: int = 3000


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
