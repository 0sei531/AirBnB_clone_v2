#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    formatted_date = dt.strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(formatted_date)
    
    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = local("tar -cvzf {} web_static".format(file_path), capture=True)
    
    if result.failed:
        print("Failed to create archive:", result)
        return None
    else:
        print("Archive created successfully:", file_path)
        return file_path

