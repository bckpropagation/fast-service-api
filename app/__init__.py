from flask_restplus import Api
from flask import Blueprint


from .main.controller.restaurants_controller import api as restaurants_ns
from .main.controller.menu_controller import api as menu_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns


__version__ = "v1"
blueprint = Blueprint("restaurants_api", __name__)
api = Api(
	blueprint,
	version="1.0",
	title="Fast service API",
	description="Fast service API"
)


api.add_namespace(restaurants_ns, path=f"/api/{__version__}")
api.add_namespace(menu_ns, path=f"/api/{__version__}/restaurants")
api.add_namespace(user_ns, path="/user")
api.add_namespace(auth_ns)
