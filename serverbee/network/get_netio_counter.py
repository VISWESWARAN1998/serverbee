# SWAMI KARUPPASWAMI THUNNAI

import psutil


def get_net_io_counter():
    net_io_counter = dict()
    counters = psutil.net_io_counters()
    net_io_counter["bytes_sent"] = counters.bytes_sent
    net_io_counter["bytes_received"] = counters.bytes_recv
    net_io_counter["packets_sent"] = counters.packets_sent
    net_io_counter["packets_received"] = counters.packets_recv
    return net_io_counter

    