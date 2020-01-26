import json

from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest


from ..utils.dto import AuthDto
from ..service.auth_service import Auth


api = AuthDto.api
_auth = AuthDto.auth


@api.route("/login")
class UserLogin(Resource):
	def validate_payload(self, func):
		try:
			super().validate_payload(func)

		except BadRequest as error:
			error.data["status"] = "fail"

			api.abort(400, **error.data)

	@api.doc("Login service")
	@api.expect(_auth, validate=True)
	def post(self):
		response = Auth.login(**api.payload)
		return response


parser = api.parser()
parser.add_argument(
	"Authorization",
	dest="auth_token",
	required=True,
	location="headers",
	help="Authorization token"
)
parser.add_argument(
	"user_id",
	dest="user_public_id",
	location="json",
	required=True,
	help="Public user id",
	nullable=False
)

@api.route("/logout")
class UserLogout(Resource):
	@api.doc("Logout service")
	def post(self):
		return Auth.logout(**parser.parse_args())
