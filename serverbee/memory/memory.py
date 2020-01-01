# SWAMI KARUPPASWAMI THUNNAI

import psutil


def primary_memory_usage():
    mem_dict = dict(psutil.virtual_memory()._asdict())
    return mem_dict


def secondary_memory_usage():
    partitions = psutil.disk_partitions()
    free = 0
    used = 0
    for partition in partitions:
        used += psutil.disk_usage(partition.mountpoint).used
        free += psutil.disk_usage(partition.mountpoint).free
    return {"used": used, "free": free}


def hard_disk_information():
    partitions = psutil.disk_partitions()
    hard_disk_information_table = []
    for partition in partitions:
        device = partition.device
        mount_point = partition.mountpoint
        fs_type = partition.fstype
        opts = partition.opts
        disk_usage = psutil.disk_usage(mount_point)
        total = disk_usage.total
        used = disk_usage.used
        free = disk_usage.free
        info = {"device": device, "mount_point": mount_point, "fs_type": fs_type, "opts": opts, "total": total,
                "used": used, "free": free}
        hard_disk_information_table.append(info)
    return hard_disk_information_table


def process_memory_usage():
    process_mem_table = []
    for process in psutil.process_iter():
        try:
            process_id = process.pid
            name = process.name()
            memory_percent = process.memory_percent()
            memory = process.memory_info()
            memory = memory.rss
            info = {"id": process_id, "name": name, "memory_percent": memory_percent, "memory": memory}
            process_mem_table.append(info)
        except psutil.AccessDenied:
            pass
    return process_mem_table


def terminate_process(process_id):
    try:
        process_id = int(process_id)
    except ValueError:
        return None
    except TypeError:
        return None
    process = psutil.Process(pid=process_id)
    process.terminate()


def process_memory_graph():
    usage = process_memory_usage()
    graph = dict()
    for i in usage:
        if i["name"] in graph:
            graph[i["name"]] += i["memory"]
        else:
            graph[i["name"]] = i["memory"]

    header = []
    content = []
    for i in graph:
        header.append(i)
        content.append(graph[i])
    payload = [header, content]
    return payload

