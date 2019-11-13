# SWAMI KARUPPASWAMI THUNNAI

import time
import hashlib
import bcrypt
import jwt
from functools import wraps
from flask import session, redirect
from database.get_connection import get_connection


def generate_hash(password):
    sha512 = hashlib.sha512(password.encode("utf8")).hexdigest()
    password_hash = bcrypt.hashpw(sha512.encode("utf-8"), bcrypt.gensalt())
    return password_hash.decode("utf8")


def verify_password(password, original_password_hash):
    sha512 = hashlib.sha512(password.encode("utf8")).hexdigest()
    if not bcrypt.checkpw(sha512.encode("utf8"), original_password_hash.encode("utf8")):
        return False
    return True


def generate_token(user_id, password_hash):
    payload = {"user": user_id, "expiry": time.time()+300}
    encoded_payload = jwt.encode(payload, password_hash)
    return encoded_payload.decode("utf8")


def server_bee_token(_function):
    @wraps(_function)
    def wrapper_function(*args, **kwargs):
        if "server_bee_token" not in session:
            return redirect("/")
        try:
            decoded_token = jwt.decode(session["server_bee_token"], verify=False)
            expiry = decoded_token["expiry"]
            if time.time() > expiry:
                return redirect("/")
            user_id = decoded_token["user"]
        except KeyError:
            return redirect("/")
        except jwt.DecodeError:
            return redirect("/")
        # If the token has a valid expiry date
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("select password from server_bee_credential where id=? limit 1", (user_id, ))
            result = cursor.fetchone()
            if result is None:
                return redirect("/")
            password = result[0]
        finally:
            cursor.close()
            connection.close()
        try:
            jwt.decode(session["server_bee_token"], password)
        except jwt.DecodeError:
            return redirect("/")
        return _function(*args, **kwargs)
    return wrapper_function
