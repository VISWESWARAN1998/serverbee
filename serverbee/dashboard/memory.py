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
        used += psutil.disk_usage(partition.device).used
        free += psutil.disk_usage(partition.device).free
    return {"used": used, "free": free}


def hard_disk_information():
    partitions = psutil.disk_partitions()
    hard_disk_information_table = []
    for partition in partitions:
        device = partition.device
        mount_point = partition.mountpoint
        fs_type = partition.fstype
        opts = partition.opts
        disk_usage = psutil.disk_usage(device)
        total = disk_usage.total
        used = disk_usage.used
        free = disk_usage.free
        info = {"device": device, "mount_point": mount_point, "fs_type": fs_type, "opts": opts, "total": total,
                "used": used, "free": free}
        hard_disk_information_table.append(info)
    return hard_disk_information_table


