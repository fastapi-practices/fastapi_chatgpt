#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from pathlib import Path

BasePath = Path(__file__).resolve().parent.parent.parent

# 日志文件路径
LogPath = os.path.join(BasePath, 'app', 'log')
