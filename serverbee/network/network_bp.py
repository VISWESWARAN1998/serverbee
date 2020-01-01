# SWAMI KARUPPASWAMI THUNNAI

from flask import render_template
from flask import Blueprint
from auth.helper import server_bee_token
from network.get_netio_counter import get_net_io_counter

network = Blueprint("network", __name__)


@network.route("/network", endpoint="network")
@server_bee_token
def render_network():
    return render_template("network.html", net_io_counter=get_net_io_counter())