#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    try:
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        now = datetime.now()
        output = f"versions/web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
        print(f"Packing web_static to {output}")
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print(f"web_static packed: {output} -> {size} Bytes")
        return output
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
