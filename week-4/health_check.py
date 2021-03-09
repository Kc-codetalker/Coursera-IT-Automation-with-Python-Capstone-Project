#!/usr/bin/env python3

import shutil
import psutil
import socket

print('The CPU usage is: ', psutil.cpu_percent(2))

# Get the disk usage statistics
# about the given path
path = "/"
stat = shutil.disk_usage(path)
disk_percent = stat.free/stat.total
print("Available disk space (%):", disk_percent)


print("Available memory (Bytes):", psutil.virtual_memory().available)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(hostname, local_ip)