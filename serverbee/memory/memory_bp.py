# SWAMI KARUPPASWAMI THUNNAI

from flask import Blueprint, render_template, request, redirect, url_for
from auth.helper import server_bee_token
from memory.memory import primary_memory_usage, secondary_memory_usage, hard_disk_information
from memory.memory import process_memory_usage, terminate_process

memory = Blueprint("memory", __name__)


@memory.route("/memory", endpoint="memory")
@server_bee_token
def render_dashboard():
    pm_usage = primary_memory_usage()
    sm_usage = secondary_memory_usage()
    return render_template("memory.html", pm_usage=pm_usage, sm_usage=sm_usage,
                           hard_disk_information=hard_disk_information(), process_memory_usage=process_memory_usage())


@memory.route("/kill_process", endpoint="kill_process", methods=["POST"])
@server_bee_token
def kill_process():
    process_id = request.form["process_id"]
    terminate_process(process_id)
    return redirect(url_for("memory.memory"))