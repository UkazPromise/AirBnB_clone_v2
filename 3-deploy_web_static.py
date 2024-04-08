#!/usr/bin/python3
"""Create and distribute an archive to web servers"""
import os.path
import time
from fabric.api import local, run, put, env

env.hosts = ['54.236.33.47', '35.175.135.250']


def do_pack():
    """Generate a .tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = time.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static/".format(archive_path))
        return archive_path
    except Exception as e:
        print("Error occurred during archive creation:", e)
        return None


def do_deploy(archive_path):
    """Distribute an archive to web servers"""
    if not os.path.isfile(archive_path):
        print("Archive file not found.")
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/" + file_name.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_name))
        print("Deployment done")
        return True
    except Exception as e:
        print("Error occurred during deployment:", e)
        return False


def deploy():
    """Create and distribute an archive to web servers"""
    try:
        archive_path = do_pack()
        if archive_path:
            return do_deploy(archive_path)
        else:
            print("Archive creation failed.")
            return False
    except Exception as e:
        print("Deployment failed:", e)
        return False
