# SWAMI KARUPPASWAMI THUNNAI

import sqlite3


def get_connection():
    connection = sqlite3.connect("server_bee.sqlite3")
    return connection