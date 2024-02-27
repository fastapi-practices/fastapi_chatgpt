#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Literal

from pydantic import BaseModel


class OllamaMessages(BaseModel):
    role: Literal['system', 'user', 'assistant']
    content: str
    images: list[str] | None = None
