# SWAMI KARUPPASWAMI THUNNAI

from flask import Blueprint
from flask import render_template, request, redirect
from auth.helper import server_bee_token
from database.get_connection import get_connection
from digital_ocean.digiatl_ocean import DigitalOcean

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


@do_bp.route("/digital_ocean")
@server_bee_token
def do_page():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select token from digital_ocean limit 1")
        result = cursor.fetchone()
        if result is None:
            return redirect("/set_digital_ocean_token")
        token = result[0]
        do_api = DigitalOcean(token=token)
    finally:
        cursor.close()
        connection.close()
    return render_template("digital_ocean.html", balance=do_api.get_balance(), droplets=do_api.get_droplets())


