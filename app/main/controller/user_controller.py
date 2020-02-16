from flask import request
from flask_restplus import Resource
from typing import Dict

from ..utils.dto import UserDto
from ..service.user_service import (
	get_user_by_public_id,
	create_user
)


api = UserDto.api
<<<<<<< Updated upstream
_user = UserDto.user
=======
_user = UserDto.user_info
_new_user = UserDto.new_user
_login_resp = UserDto.login_resp
_fail_resp = UserDto.fail_resp
>>>>>>> Stashed changes


@api.route("/<string:public_id>")
@api.param("public_id", "User id")
class SingleUser(Resource):
	@api.doc("Get user information")
<<<<<<< Updated upstream
	@api.marshal_with(_user, mask="public_id, first_name, last_name, email")
	def get(self: "SingleUser", public_id: str) -> Dict[str, str]:
=======
	@api.marshal_with(_user)
	def get(self, public_id: str) -> Dict[str, str]:
		"""
		Returns a user information.
		"""
>>>>>>> Stashed changes
		return get_user_by_public_id(public_id)


@api.route("")
class NewUser(Resource):
<<<<<<< Updated upstream
	@api.doc("Register new user")
	@api.response(201, "User created")
	@api.response(401, "User user exists")
	@api.expect(_user, validate=True)
	def post(self: "NewUser") -> Dict[str, str]:
=======
	@api.doc(
		"Register new user",
		responses={
			201: ("User created", _login_resp),
			401: ("User exists", _fail_resp)
		}
	)
	@api.expect(_new_user, validate=True)
	def post(self) -> Dict[str, str]:
		"""
		Register a new user.
		"""
>>>>>>> Stashed changes
		response_object = create_user(data=request.json)
		return response_object
