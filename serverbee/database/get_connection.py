# SWAMI KARUPPASWAMI THUNNAI

import sqlite3
from sys import platform


def get_connection():
    if "linux" in platform:
        connection = sqlite3.connect("/var/www/serverbee/serverbee/server_bee.sqlite3")
    else:
        connection = sqlite3.connect("server_bee.sqlite3")
    return connection