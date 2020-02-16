from flask_restplus import Api
from flask import Blueprint


from .main.controller.restaurants_controller import api as restaurants_ns
from .main.controller.menu_controller import api as menu_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns


__version__ = "v1"
url_prefix = f"/api/{__version__}"
blueprint = Blueprint(
	"restaurants_api",
	__name__
)
api = Api(
	blueprint,
	version="1.0",
	title="Fast service API",
<<<<<<< Updated upstream
	description="Fast service API",
<<<<<<< Updated upstream
	doc="/api/doc"
=======
	catch_all_404s=True
=======
	description="Fast service API<style>.models {display: none !important}</style>",
	doc="/api/doc"
>>>>>>> Stashed changes
>>>>>>> Stashed changes
)


api.add_namespace(restaurants_ns, path=f"{url_prefix}/restaurants")
api.add_namespace(menu_ns, path=f"{url_prefix}/restaurants")
api.add_namespace(auth_ns, path=f"{url_prefix}/auth")
api.add_namespace(user_ns, path=f"{url_prefix}/user")
