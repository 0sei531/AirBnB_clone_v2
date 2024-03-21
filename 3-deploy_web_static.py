#!/usr/bin/python3
"""
Script for managing deployment of web applications using Fabric.
"""

from fabric.api import env, local, run, put
from datetime import datetime
import os
import re

env.hosts = ['3.236.9.233', '44.200.93.43']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(datetime.strftime(
                                                   datetime.now(),
                                                   "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static"
                   .format(filename))
    if result.failed:
        return None
    return filename


def do_deploy(archive_path):
    """Distributes an archive to a web server"""
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False
    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """Creates and distributes an archive to a web server"""
    filepath = do_pack()
    if filepath is None:
        return False
    return do_deploy(filepath)


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'
          .format(number))
    releases_path = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'
        .format(releases_path, number))


if __name__ == "__main__":
    deploy()

