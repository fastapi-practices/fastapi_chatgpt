#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from interpreter.core.core import Interpreter as _Interpreter

from app.core.conf import settings


class Interpreter(_Interpreter):
    def __init__(self):
        super().__init__()
        self.local = settings.LOCAL
        self.auto_run = settings.AUTO_RUN
        self.debug_mode = settings.DEBUG_MODE
        self.max_output = settings.MAX_OUTPUT
        self.conversation_history = settings.CONVERSATION_HISTORY
        self.model = settings.MODEL
        self.temperature = settings.TEMPERATURE
        self.context_window = settings.CONTEXT_WINDOW
        self.max_tokens = settings.MAX_TOKENS
        self.max_budget = settings.MAX_BUDGET
        self.api_base = settings.API_BASE
        self.api_key = settings.API_KEY


interpreter = Interpreter()
