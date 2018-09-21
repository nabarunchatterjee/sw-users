#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.database import init_db

def create_app():
    init_db()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User Management Service'})
    return app

app =  create_app()
