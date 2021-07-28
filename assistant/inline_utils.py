# Copyright (C) 2020-2021 by TeamTezer@Github, < https://github.com/TeamTezer >.
#
# This file is part of < https://github.com/TeamTezer/TezerUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamTezer/blob/master/LICENSE >
#
# All rights reserved.

import logging
import re
import string
from random import choice
import sys
#import datetime
from datetime import datetime
from os import environ, execle, path, remove
import platform
from bot_utils_files.Localization.engine import language_string
import re
import socket
import time
import uuid
import psutil
from pyrogram import __version__
import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import requests
from bs4 import BeautifulSoup
from pyrogram import __version__, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)
from tinydb import Query, TinyDB
from main_startup.core.startup_helpers import run_cmd
from main_startup import CMD_LIST, XTRA_CMD_LIST, Tezer, bot, friday_version
from main_startup.config_var import Config
from youtubesearchpython import SearchVideos
from main_startup.helper_func.basic_helpers import (
    cb_wrapper,
    humanbytes,
    get_all_pros,
    inline_wrapper,
    paginate_help,
)

import os
from main_startup.helper_func.assistant_helpers import _dl, down
