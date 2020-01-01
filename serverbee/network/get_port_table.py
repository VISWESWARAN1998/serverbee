# SWAMI KARUPPASWAMI THUNNAI

import psutil


def port_table():
    port_data = []
    for i in psutil.net_connections():
        payload = [i.pid, i.laddr.port, i.status]
        port_data.append(payload)
    return port_data