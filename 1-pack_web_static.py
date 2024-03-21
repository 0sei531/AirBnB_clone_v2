#!/usr/bin/python3
"""
Distributes an archive to web servers and sets up a web server for deployment
"""

from fabric.api import *
from datetime import datetime
import os

# Server information
env.hosts = ['54.144.136.64', '100.24.236.179']
env.user = 'ubuntu'

def do_pack():
    '''
    Generates a tgz archive from the
    contents of the web_static folder
    '''
    try:
        local('mkdir -p versions')
        datetime_format = '%Y%m%d%H%M%S'
        archive_path = 'versions/web_static_{}.tgz'.format(
            datetime.now().strftime(datetime_format))
        local('tar -cvzf {} web_static'.format(archive_path))
        print('web_static packed: {} -> {}'.format(archive_path,
              os.path.getsize(archive_path)))
        return archive_path
    except:
        return None

def do_deploy(archive_path):
    '''
    Deploy archive to web servers
    '''
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed to web servers!')
        return True
    except:
        return False

def setup_web_server():
    '''
    Sets up a web server for deployment of web_static
    '''
    sudo('apt-get -y update')
    sudo('apt-get -y install nginx')
    sudo('mkdir -p /data/web_static/shared/')
    sudo('mkdir -p /data/web_static/releases/test/')
    with cd('/data/web_static/releases/test/'):
        sudo('echo "<html><head></head><body>Holberton School</body></html>" > index.html')
    sudo('ln -sf /data/web_static/releases/test/ /data/web_static/current')
    sudo('chown -R ubuntu:ubuntu /data/')
    sudo('sed -i "61i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default')
    sudo('service nginx restart')
    print('Web server setup completed!')

# Combined function to execute both tasks
def deploy_web_app():
    # Generate archive
    archive_path = do_pack()
    if archive_path:
        print("Archive generated:", archive_path)
        # Deploy archive to web servers
        if do_deploy(archive_path):
            print("Deployment to web servers successful!")
        else:
            print("Deployment to web servers failed.")
    else:
        print("Archive generation failed.")

if __name__ == "__main__":
    deploy_web_app()
    setup_web_server()

