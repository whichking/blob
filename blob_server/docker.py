
from time import sleep
from typing import Union

import docker
from docker.errors import NotFound


def start_sql(name: str, db_name: str, local_port: Union[str, int]) -> None:
    """Start the SQL container

    :param name: the name of the SQL container
    :param db_name: the desired name of the SQL DB
    :param local_port: the local port where the DB should be exposed
    """
    client = docker.from_env()
    try:
        container = client.containers.get(name)
    except docker.errors.NotFound:
        container = client.containers.run(
            'postgres:9.6',
            name=name,
            detach=True,
            ports={5432: local_port},
            environment={'POSTGRES_PASSWORD': 'test_blob_pw',
                         'POSTGRES_USER': 'blob_user',
                         'POSTGRES_DB': db_name}
        )
        sleep(5)
    container.start()


def stop_sql(name: str) -> None:
    """Stop the SQL container

    :param name: the name of the SQL container
    """
    client = docker.from_env()
    try:
        container = client.containers.get(name)
    except docker.errors.NotFound:
        pass
    else:
        container.stop(timeout=5)


def remove_sql(name: str) -> None:
    """Remove the SQL container

    :param name: the name of the SQL container
    """
    client = docker.from_env()
    try:
        container = client.containers.get(name)
    except docker.errors.NotFound:
        pass
    else:
        stop_sql(name)
        container.remove()
