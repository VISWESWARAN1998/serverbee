# SWAMI KARUPPASWAMI THUNNAI

from flask import render_template
from flask import Blueprint
from auth.helper import server_bee_token

network = Blueprint("network", __name__)


@network.route("/network", endpoint="network")
@server_bee_token
def render_network():
    return render_template("network.html")