from flask import Blueprint
from flask_restx import Api

from . import example


def init_routers(app):
    blueprint = Blueprint('api', __name__, url_prefix='')
    api = Api(blueprint, 
              title=f'Ml service API',
              description=f'API for ML service',
              doc='/swagger')
    
    api.add_namespace(example.api)

    app.register_blueprint(blueprint)

