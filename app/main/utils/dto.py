from collections import OrderedDict
from flask_restplus import Namespace, fields, Model


class GenericResponse:
	resp = OrderedDict()
	resp["status"] = fields.String(
		description="Operation status"
	)

	resp["message"] = fields.String(
		description="Operation description"
	)

class MenuDto:
	api = Namespace(
		"menu",
		description="Information of restaurant menu"
	)

	menu = api.model(
		"menu",
		{
			"id": fields.Integer(
				description="Dish id"
			),
			"name": fields.String(
				description="Dish name"
			),
			"type": fields.String(
				description="Dish type"
			),
			"price": fields.Float(
				description="Dish price"
			)
		}
	)

	dish = api.inherit(
		"dish",
		menu,
		{
			"description": fields.String(
				description="Dish description"
			)
		}
	)


class RestaurantsDto:
	api = Namespace(
		"restaurants",
		description="Information of registered restaurants."
	)

	restaurant = api.model(
		"restaurant",
		{
			"id": fields.Integer(
				description="Restaurant id number"
			),
			"name": fields.String(
				description="Restaurant name"
			),
			"hours": fields.String(
				description="Restaurant work hours"
			),
			"menus": fields.List(
				fields.Nested(MenuDto.menu)
			)
		}
	)


class AuthDto:
	api = Namespace(
		"auth",
		description="Authentication information",
		validate=True
	)
<<<<<<< Updated upstream

	auth = api.model(
		"auth",
		{
			"email": fields.String(
				required=True,
				description="User email address"
			),
			"passwd": fields.String(
				required=True,
				description="User password"
			)
		}
	)


class UserDto:
	api = Namespace(
		"user",
		description="User information"
	)

	user = api.model(
		"user",
		{
			"public_id": fields.String(
				description="User public id",
				readonly=True
			),
=======
<<<<<<< Updated upstream
	
	full_model = min_model
	full_model["menus"] = fields.List(
		fields.Nested(MenuDto.menu)
	)

	restaurant = api.model(
		"restaurant",
		full_model
=======

	login_resp = GenericResponse.resp.copy()
	login_resp["Authorization"] = fields.String(
		description="Logged in user token"
	)

	login_resp = api.model(
		"log_resp",
		login_resp
	)


class UserDto:
	api = Namespace(
		"User",
		description="User information"
	)

	__user_base_model = api.model(
		"Base",
		{
>>>>>>> Stashed changes
			"first_name": fields.String(
				required=True,
				description="User first name"
			),
			"last_name": fields.String(
				required=True,
				description="User last name"
<<<<<<< Updated upstream
			),
=======
			)
		}
	)

	user_info = api.clone(
		"user",
		__user_base_model,
		{
			"public_id": fields.String(
				description="User public id",
				readonly=True
			)
		}
	)

	new_user = api.clone(
		"new_user",
		__user_base_model,
		{
>>>>>>> Stashed changes
			"email": fields.String(
				required=True,
				description="User email"
			),
			"passwd": fields.String(
				required=True,
				description="User password",
<<<<<<< Updated upstream
				format="password"
			)
		}
=======
				format="password",
			)
		}
>>>>>>> Stashed changes
	)

	fail_resp = api.model(
		"fail",
		GenericResponse.resp.copy()
	)

	login_resp = GenericResponse.resp.copy()
	login_resp["public_id"] = fields.String(
		description="User public Id"
	)

	login_resp = api.model(
		"auth_resp",
		login_resp
>>>>>>> Stashed changes
	)
