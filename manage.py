from flask_script import Manager, Server
from blob_server.app import create_app
from blob_server.app_config import DevConfig

app = create_app(DevConfig)
manager = Manager(app)

manager.add_command('runserver', Server(host='0.0.0.0', port=8080))

if __name__ == '__main__':
    manager.run()
