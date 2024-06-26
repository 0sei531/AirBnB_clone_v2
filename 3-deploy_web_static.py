#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed:
            print("Failed to create versions directory")
            return None

    if local("tar -cvzf {} web_static".format(file)).failed:
        print("Failed to create tar.gz archive")
        return None

    print("Archive created:", file)
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        True if the deployment was successful, False otherwise.
    """
    if not os.path.isfile(archive_path):
        print("Archive not found:", archive_path)
        return False

    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        print("Failed to upload archive to remote server")
        return False

    commands = [
        "rm -rf /data/web_static/releases/{}/".format(name),
        "mkdir -p /data/web_static/releases/{}/".format(name),
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name),
        "rm /tmp/{}".format(file),
        "mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name),
        "rm -rf /data/web_static/releases/{}/web_static".format(name),
        "rm -rf /data/web_static/current",
        "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)
    ]

    for command in commands:
        if run(command).failed:
            print("Command failed:", command)
            return False

    print("Deployment successful")
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)

