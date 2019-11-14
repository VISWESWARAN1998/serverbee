# SWAMI KARUPPASWAMI THUNNAI

from flask import Blueprint, render_template
from auth.helper import server_bee_token
from dashboard.memory import primary_memory_usage, secondary_memory_usage, hard_disk_information
from dashboard.memory import process_memory_usage

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard", endpoint="dashboard")
@server_bee_token
def render_dashboard():
    pm_usage = primary_memory_usage()
    sm_usage = secondary_memory_usage()
    process_mem_usage = process_memory_usage()
    return render_template("dashboard/dashboard.html", pm_usage=pm_usage, sm_usage=sm_usage,
                           hard_disk_information=hard_disk_information(), process_memory_usage=process_memory_usage())