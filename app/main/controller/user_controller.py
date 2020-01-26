from flask import request
from flask_restplus import Resource
from typing import Dict

from ..utils.dto import UserDto
from ..service.user_service import (
	get_user_by_public_id,
	create_user
)


api = UserDto.api
_user = UserDto.user


@api.route("/<string:public_id>")
@api.param("public_id", "User id")
class SingleUser(Resource):
	@api.doc("Get user information")
	@api.marshal_with(_user, mask="public_id, first_name, last_name, email")
	def get(self: "SingleUser", public_id: str) -> Dict[str, str]:
		return get_user_by_public_id(public_id)


@api.route("")
class NewUser(Resource):
	@api.doc("Register new user")
	@api.response(201, "User created")
	@api.response(401, "User user exists")
	@api.expect(_user, validate=True)
	def post(self: "NewUser") -> Dict[str, str]:
		response_object = create_user(data=request.json)
		return response_object
