#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.database import init_db

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User Management Service'})
    app.run(port=8080)


if __name__ == '__main__':
    init_db()
    main()
