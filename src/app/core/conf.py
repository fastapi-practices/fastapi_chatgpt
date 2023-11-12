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
    DESCRIPTION: str = 'FastAPI ChatGPT'
    DOCS_URL: str | None = f'{API_V1_STR}/docs'
    REDOCS_URL: str | None = f'{API_V1_STR}/redocs'
    OPENAPI_URL: str | None = f'{API_V1_STR}/openapi'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # ChatGPT Settings
    LOCAL: bool = False
    AUTO_RUN: bool = False
    DEBUG_MODE: bool = False
    MAX_OUTPUT: int = 2000

    # Conversation history
    CONVERSATION_HISTORY: bool = False

    # LLM Settings
    API_BASE: str = ''
    API_KEY: str = ''
    MODEL: str = 'gpt-3.5-turbo'
    TEMPERATURE: float = 0.6
    CONTEXT_WINDOW: int = 16000
    MAX_TOKENS: int = 100
    MAX_BUDGET: float = 0.01


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
