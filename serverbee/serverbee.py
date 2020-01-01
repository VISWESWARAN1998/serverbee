# SWAMI KARUPPASWAMI THUNNAI

from flask import Flask, request, redirect, render_template
from auth.auth_view import auth
from memory.memory_bp import memory
from network.network_bp import network
from auth.helper import server_bee_token, generate_hash
from database.get_connection import get_connection

app = Flask(__name__)
app.secret_key = "SERVER_BEE_DEFAULT_KEY_PLEASE_CHANGE"

app.register_blueprint(auth)
app.register_blueprint(memory)
app.register_blueprint(network)


@app.route("/change_password")
@server_bee_token
def change_password():
    return render_template("auth/password_change.html")


@app.route("/confirm_change_password", methods=["POST"])
@server_bee_token
def confirm_change():
    default_username = "admin"
    new_password = request.form["new_password"]
    password_hash = generate_hash(new_password)
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("delete from server_bee_credential where username=?", (default_username, ))
        connection.commit()
        cursor.execute("insert into server_bee_credential values(null, ?, ?)",
                       (default_username, password_hash))
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)