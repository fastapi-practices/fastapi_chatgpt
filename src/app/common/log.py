#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import os

import loguru

from loguru import logger

from app.core import path_conf


class Logger:
    @staticmethod
    def log() -> loguru.Logger:
        if not os.path.exists(path_conf.LogPath):
            os.mkdir(path_conf.LogPath)

        # 日志文件
        log_file = os.path.join(path_conf.LogPath, 'fastapi_scheduler.log')

        # loguru日志
        # more: https://github.com/Delgan/loguru#ready-to-use-out-of-the-box-without-boilerplate
        logger.add(
            log_file,
            encoding='utf-8',
            level='DEBUG',
            rotation='10 MB',
            retention='7 days',
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )

        return logger


log = Logger().log()
