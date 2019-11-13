# SWAMI KARUPPASWAMI THUNNAI

from flask import Flask
from auth.auth_view import auth
from dashboard.dashboard_bp import dashboard

app = Flask(__name__)
app.secret_key = "SERVER_BEE_DEFAULT_KEY_PLEASE_CHANGE"

app.register_blueprint(auth)
app.register_blueprint(dashboard)


if __name__ == "__main__":
    app.run(debug=True)