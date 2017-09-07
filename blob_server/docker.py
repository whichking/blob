import docker
from docker.errors import NotFound


def start_sql(name, db_name, local_port):
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
                         'POSTGRES_DB': 'db_name'}
        )
    else:
        container.start()


def stop_sql(name):
    client = docker.from_env()
    try:
        container = client.containers.get(name)
    except docker.errors.NotFound:
        pass
    else:
        container.stop(timeout=5)


def remove_sql(name):
    client = docker.from_env()
    try:
        container = client.containers.get(name)
    except docker.errors.NotFound:
        pass
    else:
        stop_sql(name)
        container.remove()
