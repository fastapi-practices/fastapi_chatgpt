#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any

from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: int = 200
    msg: str = 'OK'
    data: Any = None
