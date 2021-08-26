#!/usr/bin/python3
'''module for do_pack()'''
from datetime import datetime
from fabric.api import local, put, run, env
from os import path
from os.path import exists
env.hosts = ['ubuntu@104.196.35.45', 'ubuntu@34.73.125.171']


def deploy():
    '''deploys fabric methods'''
    return(do_deploy(do_pack()))


def do_pack():
    '''packs contents of /webstatic into .tgz'''

    if path.exists("./versions") is False:
        local("mkdir versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return(file_name)
    except Exception:
        return(None)


def do_deploy(archive_path):
    '''deploys content of web_static file to servers'''
    if archive_path is None or exists(archive_path) is False:
        return(False)
    try:
        archive_name = archive_path.split("/")[1].split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(archive_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(archive_name, archive_name))
        run("rm /tmp{}.tgz".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases{}/"
            .format(archive_name, archive_name))
        run("rm -rf /data/web_static/releases/{}/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(archive_name))
        return (True)
    except Exception:
        return (False)
