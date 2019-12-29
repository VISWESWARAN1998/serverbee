# SWAMI KARUPPASWAMI THUNNAI

from flask import Flask
from auth.auth_view import auth
from memory.memory_bp import memory
from network.network_bp import network

app = Flask(__name__)
app.secret_key = "SERVER_BEE_DEFAULT_KEY_PLEASE_CHANGE"

app.register_blueprint(auth)
app.register_blueprint(memory)
app.register_blueprint(network)


if __name__ == "__main__":
    app.run(debug=True)