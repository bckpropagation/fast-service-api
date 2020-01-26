from flask_restplus import Namespace, fields


class MenuDto:
	api = Namespace(
		"menu",
		description="Information of restaurant menu"
	)

	min_model = {
		"id": fields.Integer(
			description="Dish id"
		),
		"name": fields.String(
			description="Dish name"
		),
		"type": fields.String(
			description="Dish type"
		)
	}

	menu = api.model(
		"menu",
		min_model
	)

	full_model = min_model
	full_model["description"] = fields.String(
		description="Dish description"
	)
	dish = api.model(
		"dish",
		full_model
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
			"first_name": fields.String(
				required=True,
				description="User first name"
			),
			"last_name": fields.String(
				required=True,
				description="User last name"
			),
			"email": fields.String(
				required=True,
				description="User email"
			),
			"passwd": fields.String(
				required=True,
				description="User password",
				format="password"
			)
		}
	)
