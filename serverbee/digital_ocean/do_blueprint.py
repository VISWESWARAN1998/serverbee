# SWAMI KARUPPASWAMI THUNNAI

from flask import Blueprint
from flask import render_template, request, redirect
from auth.helper import server_bee_token
from database.get_connection import get_connection

do_bp = Blueprint("do", __name__)


@do_bp.route("/set_digital_ocean_token")
@server_bee_token
def do_token():
    return render_template("do_set_token.html")


@do_bp.route("/set_do_token", methods=["POST"])
@server_bee_token
def set_token():
    token = request.form["token"]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("delete from digital_ocean")
        cursor.execute("insert into digital_ocean values(?)", (token, ))
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return redirect("/digital_ocean")


