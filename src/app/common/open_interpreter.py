#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from interpreter.core.core import OpenInterpreter as _OpenInterpreter

from app.core.conf import settings


class OpenInterpreter(_OpenInterpreter):
    def __init__(self):
        super().__init__()
        self.offline = True
        self.auto_run = settings.INTERPRETER_AUTO_RUN
        self.max_output = settings.INTERPRETER_MAX_OUTPUT
        # LLM
        self.llm.model = f'ollama_chat/{settings.OLLAMA_MODEL}'
        self.llm.api_base = settings.INTERPRETER_API_BASE
        self.llm.temperature = settings.INTERPRETER_TEMPERATURE
        self.llm.max_tokens = settings.INTERPRETER_MAX_TOKENS
        self.llm.max_budget = settings.INTERPRETER_MAX_BUDGET
        self.llm.context_window = settings.INTERPRETER_CONTEXT_WINDOW


open_interpreter = OpenInterpreter()
