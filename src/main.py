# coding: utf-8
import os
import logging
from flask import Flask
from flask_cors import CORS
from views.supplier_prices_charges import supplier_prices_charges_blueprint


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                        os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info('Starting app')
    app = Flask(__name__)
    app.register_blueprint(supplier_prices_charges_blueprint)
    CORS(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
