#!/usr/bin/env python

from os import environ
from flask_script import Manager, Server
from subprocess import Popen

SQL_CONTAINER_NAME = 'blob_sql_dev'
SQL_PORT = '5433'
SQL_DB_NAME = 'blob_db_dev'
SQL_USER = 'blob_user'
SQL_PASSWORD = 'test_blob_pw'


def update_environment():
    """
    :return: no return
    """
    environ['BLOB_SQL_DB_PORT'] = SQL_PORT
    environ['BLOB_SQL_DB_NAME'] = SQL_DB_NAME
    environ['BLOB_SQL_USER'] = SQL_USER
    environ['BLOB_SQL_PASSWORD'] = SQL_PASSWORD

update_environment()


from blob_server.app import create_app
from blob_server.app_config import DevConfig
from blob_server.docker import start_sql, stop_sql, remove_sql


app = create_app(DevConfig)
manager = Manager(app)

manager.add_command('runserver', Server(host='0.0.0.0', port=8080))


@manager.command
def start():
    process = Popen(['docker-compose', 'up'], env=dict(environ))
    process.communicate()


@manager.command
def stop():
    process = Popen(['docker-compose', 'down'], env=dict(environ))
    process.communicate()


@manager.command
def rebuild():
    process = Popen(['docker-compose', 'build'], env=dict(environ))
    process.communicate()

if __name__ == '__main__':
    manager.run()
