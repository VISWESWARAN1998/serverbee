# SWAMI KARUPPASWAMI THUNNAI

from flask import request, render_template, redirect, url_for, session
from database.get_connection import get_connection
from auth.helper import generate_hash, verify_password, generate_token


def render_login():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("create table if not exists server_bee_credential(id integer primary key autoincrement, "
                       "username text, password text);")
        cursor.execute("select count(id) as count from server_bee_credential")
        result = cursor.fetchone()
        if result[0] == 0:
            default_username = "admin"
            default_password = generate_hash(default_username)
            cursor.execute("insert into server_bee_credential values(null, ?, ?)",
                           (default_username, default_password))
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return render_template("auth/login.html", version=0.1)


def perform_login():
    username = request.form["username"]
    password = request.form["password"]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select id, password from server_bee_credential where username=? limit 1", (username, ))
        result = cursor.fetchone()
        if result is None:
            return redirect("/")
        original_password_hash = result[1]
        if not verify_password(password, original_password_hash):
            return redirect("/")
        session["server_bee_token"] = generate_token(result[0], original_password_hash)
        return redirect(url_for("dashboard.dashboard"))
    finally:
        cursor.close()
        connection.close()