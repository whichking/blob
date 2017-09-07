import docker
from docker.errors import NotFound


def start_sql(name: str, db_name: str, local_port: int) -> None:
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
            'postgres',
            name=name,
            detach=True,
            ports={3306: local_port},
            environment={'POSTGRES_PASSWORD': 'test_pg_pw',
                         'POSTGRES_USER': 'pg_user',
                         'POSTGRES_DB': db_name}
        )
    else:
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
