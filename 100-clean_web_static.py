#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['54.236.33.47', '35.175.135.250']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    try:
        number = int(number)
    except ValueError:
        print("Error: 'number' must be an integer.")
        return

    if number <= 0:
        number = 2
    else:
        number += 1

    try:
        local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    except Exception as e:
        print("Local cleanup error:", e)

    path = '/data/web_static/releases'
    try:
        run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
    except Exception as e:
        print("Remote cleanup error:", e)
