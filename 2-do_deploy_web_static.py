#!/usr/bin/python3
"""
A Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import env, run, put, local
import os

env.hosts = ['34.229.12.144', '107.20.20.164']  # Example IP addresses
env.user = "ubuntu"

def do_deploy(archive_path):
    """
    Deploys an archive to web servers.
    - Returns False if the file at the path archive_path doesn’t exist
    - Uploads the archive to the /tmp/ directory of the web server
    - Uncompresses the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    - Deletes the archive from the web server
    - Deletes the symbolic link /data/web_static/current from the web server
    - Creates a new symbolic link /data/web_static/current on the web server, linked to the new version of your code
    - Returns True if all operations have been done correctly, otherwise returns False
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
