#!/usr/bin/python3
"""
A Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import env, run, put, local
import os


env.hosts = ['34.229.12.144', '107.20.20.164']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ 
    Deploys an archive to web servers.
    This function takes the path to an archive and deploys it to web servers.
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        name_without_ext = file_name.split('.')[0]
        release_path = f"/data/web_static/releases/{name_without_ext}/"
        put(archive_path, f"/tmp/{file_name}")
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{file_name} -C {release_path}")
        run(f"rm /tmp/{file_name}")
        run(f"mv {release_path}web_static/* {release_path}")
        run(f"rm -rf {release_path}web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_path} /data/web_static/current")

        print("New version deployed!")
        return True
    except:
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        archive_path = sys.argv[1]
        has_deployed = do_deploy(archive_path)
        if has_deployed:
            print("Deployment successful.")
        else:
            print("Deployment failed.")
