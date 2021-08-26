#!/usr/bin/python3
'''module for do_pack()'''


def do_pack():
    '''packs contents of /webstatic into .tgz'''
    from datetime import datetime
    from fabric.api import local
    from os import path

    if path.exists("./versions") is False:
        local("mkdir versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return(file_name)
    except Exception:
        return(None)
