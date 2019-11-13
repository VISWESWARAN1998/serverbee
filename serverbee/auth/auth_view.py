# SWAMI KARUPPASWAMI THUNNAI

from flask import Blueprint
from auth.login import render_login, perform_login

auth = Blueprint("auth", __name__)

auth.add_url_rule("/", view_func=render_login)
auth.add_url_rule("/login", view_func=perform_login, methods=["POST"])