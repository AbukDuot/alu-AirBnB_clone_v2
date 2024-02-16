#!/usr/bin/python3
from fabric.api import local, env
from datetime import datetime

def do_pack():
    local("mkdir -p versions")
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(time_now)
    result = local("tar -czf {} web_static/".format(path))
    if result.failed:
        return None
    return path
