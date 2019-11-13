# SWAMI KARUPPASWAMI THUNNAI

from flask import Blueprint
from auth.helper import server_bee_token

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard", endpoint="dashboard")
@server_bee_token
def render_dashboard():
    return "T"