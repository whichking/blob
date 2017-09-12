#!/usr/bin/env python

from os import environ
from flask_script import Manager, Server

SQL_CONTAINER_NAME = 'blob_sql_dev'
SQL_PORT = '5433'
SQL_DB_NAME = 'blob_db_dev'


def update_environment():
    """
    :return: no return
    """
    environ['BLOB_SQL_DB_PORT'] = SQL_PORT
    environ['BLOB_SQL_DB_NAME'] = SQL_DB_NAME

update_environment()


from blob_server.app import create_app
from blob_server.app_config import DevConfig
from blob_server.docker import start_sql, stop_sql, remove_sql


app = create_app(DevConfig)
manager = Manager(app)

manager.add_command('runserver', Server(host='0.0.0.0', port=8080))


@manager.command
def start():
    start_sql(SQL_CONTAINER_NAME, SQL_DB_NAME, SQL_PORT)


@manager.command
def stop():
    stop_sql(SQL_CONTAINER_NAME)


@manager.command
def remove():
    remove_sql(SQL_CONTAINER_NAME)

if __name__ == '__main__':
    manager.run()
