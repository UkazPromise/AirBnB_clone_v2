#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import env, put, run, sudo
from fabric.contrib.files import exists
import os

env.hosts = ['54.236.33.47', '35.175.135.250']

def do_deploy(archive_path):
    """Function to deploy"""
    if not exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = os.path.basename(archive_path).split('.')[0]
    name = tmp.split('/')[1]
    dest = os.path.join(data_path, name)

    try:
        put(archive_path, '/tmp')
        sudo('mkdir -p {}'.format(dest))
        sudo('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        sudo('rm -f /tmp/{}.tgz'.format(name))
        sudo('mv {}/web_static/* {}/'.format(dest, dest))
        sudo('rm -rf {}/web_static'.format(dest))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {} /data/web_static/current'.format(dest))
        return True
    except fabric.exceptions.NetworkError:
        print("Error: Could not connect to host.")
    except fabric.exceptions.CommandExecutionError:
        print("Error: Command execution failed.")
    return False
