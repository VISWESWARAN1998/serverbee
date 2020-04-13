# SWAMI KARUPPASWAMI THUNNAI

from database.get_connection import get_connection


def do_init():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("create table if not exists digital_ocean(token text);")
        connection.commit()
    finally:
        cursor.close()
        connection.close()